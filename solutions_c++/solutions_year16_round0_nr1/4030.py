#include <iostream>

int main(int argc, char* argv[]) {
    int n;
    int curr;
    std::cin >> n;
    
    for (int i = 0; i < n; i++) {
        std::cin >> curr;
        std::cout << "Case #" << i + 1 << ": ";
        if (curr == 0) {
            std::cout << "INSOMNIA\n";
            continue;
        }
        int seen[10];
        for (int k = 0; k < 10; k++) {
            seen[k] = 0;
        }
        bool found = false;
        int num;
        int iter = 0;
        while (!found) {
            iter++;
            found = true;
            num = iter * curr;
            while(num > 0) {
                seen[num % 10] = 1;
                num = num / 10;
            }
            for (int k = 0; k < 10; k++) {
                if(seen[k] == 0) {
                    found = false;
                }
            }
        }
        std::cout << iter * curr << '\n';
    }
} 
