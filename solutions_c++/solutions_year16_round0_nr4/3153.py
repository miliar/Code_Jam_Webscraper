#include <iostream>
#include <cmath>

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        int K, C, S;

        std::cin >> K >> C >> S;

        std::cout << "Case #" << idx << ": ";
        if (C == 1) {
            for (int i = 1; i <= K; i++) {
                std::cout << i << " ";
            }
        } else {
            for (int i = 0; i < K; i++) {
                std::cout << i * (long long)pow(K, C - 1) + i * (long long)pow(K, C - 2) + 1 << " ";
            }
        }
        std::cout  << std::endl;
    }

    return 0;
}
