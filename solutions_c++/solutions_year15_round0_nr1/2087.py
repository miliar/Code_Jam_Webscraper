#include <basic.h>

int main(int argc, char * argv[])
{
    int T;
    std::cin >> T;
    for (size_t t = 0; t != T; ++t)
    {
        int Sm;
        std::cin >> Sm;
        std::string S;
        std::cin >> S;

        int c = 0;
        int total = 0;
        for (size_t i = 0; i != Sm + 1; ++i)
        {
            if (total < i)
            {
                c += i - total;
                total = i;
            }
            total += (S[i] - '0');
        }
        std::cout << "Case #" << t + 1 << ": " << c << std::endl;
    }
    return 0;
}

