#include <iostream>
#include <cstdlib>

int isset[10];

void sset(int n) {
    while (n) {
        isset[n%10] = 1;
        n /= 10;
    }
}

bool isfull() {
    bool ret = true;
    for (int i = 0; i < 10; i++) {
        if (isset[i] != 1) {
            ret = false;
            break;
        }
    }
    return ret;
}

void print() {
    for (int i = 0; i < 10; i++) {
        std::cout << " " << i;
    }
    std::cout << std::endl;
    for (int i = 0; i < 10; i++) {
        std::cout << " " << isset[i];
    }
    std::cout << std::endl;
}
int main() {
    const char fail[] = "INSOMNIA";
    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, nn;
        int ct = 1;
        memset(isset, 0, 10*sizeof(int));
        std::cout << "Case #" << t << ": ";
        std::cin >> n;
        nn = n;
        if (n == 0) {
            std::cout << fail << std::endl;
            continue;
        }
        while (!isfull()) {
            sset(nn);
            //std::cout << "| " << nn << std::endl;
            //print();
            nn += n;
        }
        if (isfull())
            std::cout << nn-n << std::endl;
        else
            std::cout << fail << std::endl;
    }
    return 0;
}
