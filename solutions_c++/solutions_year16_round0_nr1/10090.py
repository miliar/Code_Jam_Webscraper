#include <iostream>
#include <string>

bool named[10] = {false};

void seeN(int n) {
    while(n > 0) {
        named[n%10] = true;
        n = n / 10;
    }
}
int main() {
    int T, N;
    std::cin >> T;

    for(int i = 0; i < T; i++) {
        for(int j = 0; j < 10; j++) {
            named[j] = false;
        }

        std::cin >> N;

        if(N == 0) {
            std::cout << "case #" << i+1 << ": " << "INSOMNIA" << std::endl;
        } else {
            int tmpN = N;
            int tmp = N;

            bool sleep = true;
            int tries = 1;
            while(true) {
                seeN(tmpN);
                sleep = true;
                for(int j = 0; j < 10; j++) {
                    sleep = sleep & named[j];
                }
                if(sleep) {
                    std::cout << "case #" << i+1 << ": " << tmpN << std::endl;
                    break;
                } else {
                    sleep = false;
                    tries++;
                    tmpN = N * tries;
                }
            }
        }

    }

    return 0;
}
