#include <iostream>
#include <string>

int main()
{
    size_t t;
    std::cin >> t;

    for(int i = 0; i < t; ++i)
    {
        std::string s;
        size_t s_max;

        std::cin >> s_max;
        std::cin >> s;

        size_t current_sum = 0;
        size_t sum_added = 0;

        for (int j = 0; j <= s_max; ++j)
        {
            if (current_sum < j)
            {
                size_t delta = j - current_sum;
                current_sum += delta;
                sum_added += delta;
            }
            current_sum += (size_t)(s[j] - '0');
        }

        std::cout << "Case #" << i + 1 << ": " << sum_added << "\n";
    }
    return 0;
}
