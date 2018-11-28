#include <iostream>

int main(int argc, char** argv) {
    int times;
    std::cin >> times;

    for (int i = 0; i < times; i++) {
        int K, C, S;
        std::cin >> K >> C >> S;
        std::cout << "Case #" << i + 1 << ": ";

        for (int j = 1; j <= S; j++) {
            if (j != S) {
                std::cout << j << " ";
            } else {
                std::cout << j << std::endl;
            }
        }
    }
}
