#include <basic.h>

int main(int argc, char * argv[])
{
    int T;
    std::cin >> T;
    for (size_t t = 0; t != T; ++t)
    {
        size_t D;
        std::cin >> D;

        std::vector<int> P;
        readTokens(P, D);
        //std::cout << P << std::endl;

        int max{*std::max_element(P.begin(), P.end())};
        //std::cout << max << std::endl;
        int minC = max;
        for (size_t i = 2; i < max; ++i)
        {
            int c = 0;
            for (auto p : P)
            {
                c += std::ceil(p * 1.0 / i - 1);
            }
            if (c + i < minC)
            {
                minC = c + i;
            }
        }
        std::cout << "Case #" << t + 1 << ": " << minC << std::endl;
    }
    return 0;
}

