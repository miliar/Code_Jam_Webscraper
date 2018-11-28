#include <iostream>
#include <bitset>

int main()
{
    int T;
    std::cin >> T;

    for (int t = 0; t < T; t++)
    {
        int N;
        std::cin >> N;
        int NN = N;

        std::cout << "Case #" << t + 1 << ": ";

        if (N == 0)
            std::cout << "INSOMNIA\n";
        else
        {
            std::bitset<10> seen;
            unsigned long count = 0;

            while (!seen.all())
            {   
                count++;
                N = count * NN;

                int n = N;
                while (n > 0)
                {
                    int digit = n % 10;
                    n /= 10;
                    seen.set(digit, true);
                }
            }

            std::cout << N << '\n';
        }
    }
}

