#include <iostream>

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        int N, bits[10] = {0}, unseen = 10, iterations = 1;
        
        std::cin >> N;

        if (N == 0) {
            std::cout << "Case #" << idx << ": INSOMNIA" << std::endl;
            continue;
        }
        
        while(1) {
            int new_N = N * iterations;
            do {
                int digit = new_N % 10;

                if (bits[digit] == 0) {
                    bits[digit] = 1;
                    unseen--;
                }
                new_N /= 10;
            } while (new_N > 0);

            if (unseen == 0) break;

            iterations++;
        }
        std::cout << "Case #" << idx << ": " << N*iterations  << std::endl;
    }

    return 0;
}
