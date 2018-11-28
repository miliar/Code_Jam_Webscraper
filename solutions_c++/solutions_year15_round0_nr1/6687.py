#include <iostream>

int testCase()
{
    int cmax;
    std::cin >> cmax;
    std::cin.get();
    int result = 0;
    int standing = 0;
    for (int i = 0; i <= cmax; ++i) {
        int val = std::cin.get() - '0';
        if (standing < i) {
            result += i - standing;
            standing = i;
        }
        standing += val;
    }
    return result;
}

int main()
{
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i)
        std::cout << "Case #" << (i + 1) << ": " << testCase() << std::endl;

    return 0;
}
