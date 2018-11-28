#include <iostream>
#include <algorithm>

int main()
{
    int T; std::cin >> T; std::cin.ignore();

    for (int i = 1; i <= T; ++i)
    {
        long long unsigned A; std::cin >> A;
        long long unsigned B; std::cin >> B;
        long long unsigned K; std::cin >> K;
        std::cin.ignore();

        unsigned count = 0;

        for (long long unsigned j = 0; j < A; j++) {
            for (long long unsigned k = 0; k < B; k++) {
                if ((j & k) < K) count++;
            }
        }

        std::cout << "Case #" << i << ": " << count << std::endl;
    }
}
