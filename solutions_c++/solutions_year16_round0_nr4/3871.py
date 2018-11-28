#include <iostream>

int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        int K, C, S;
        std::cin >> K >> C >> S;
        std::cout << "Case #" << (i+1) << ":";
        for (int p = 0; p < K; p++) {
            std::cout << " " << (p + 1);
        }
        std::cout << std::endl;
    }
    return 0;
}
