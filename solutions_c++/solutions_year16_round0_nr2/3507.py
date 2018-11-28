#include <iostream>
#include <string>
#include <sstream>
#include <set>

inline void toogleToFind(char& toFind)
{
    if (toFind == '-')
    {
        toFind = '+';
    }
    else
    {
        toFind = '-';
    }
}
int countFlipping(const std::string& stack)
{
    int count = 0;
    char toFind('-');
    const auto lastElement = stack.size() - 1;
    for (int i = lastElement; i >= 0; --i)
    {
        if (stack[i] == toFind)
        {
            ++count;
            toogleToFind(toFind);
        }
    }
    return count;
}

int main()
{
    int T;

    std::cin >> T;
    for (auto i = 0; i < T; i++)
    {
        std::string S;
        std::cin >> S;

        std::cout << "Case #" << i + 1 << ": " << countFlipping(S) << std::endl;
    }

    return 0;
}