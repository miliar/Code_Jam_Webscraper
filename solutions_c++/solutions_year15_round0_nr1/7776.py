#include <iostream>
#include <string>

int main(void)
{
    int t;
    std::cin >> t;

    for (int tt = 0; tt < t; tt++)
    {
        int max_level;
        std::cin >> max_level;

        std::string shyness;
        std::cin >> shyness;

        int prev = 0;
        int result = 0;
        for (int level = 0; level <= max_level; level++)
        {
            result += std::max(level - prev, 0);
            prev += shyness[level] - '0' + std::max(level - prev, 0);
        }

        std::cout << "Case #" << tt + 1 << ": " << result << std::endl;
    }

    return 0;
}
