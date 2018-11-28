#include <iostream>

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        int max_shyness;
        std::string audience;

        std::cin >> max_shyness;
        std::cin >> audience;

        int accum_audience = 0;
        int required_audience = 0;
        for(unsigned i = 0; i < audience.size(); i++)
        {
            int num_audience = audience[i] - '0';

            if (num_audience > 0 && i > accum_audience)
            {
                required_audience += (i - accum_audience);
                accum_audience += required_audience;
            }

            accum_audience += num_audience;
        }

        std::cout << "Case #" << idx << ": " << required_audience << std::endl;
    }

    return 0;
}