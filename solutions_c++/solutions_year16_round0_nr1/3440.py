#include <iostream>
#include <sstream>
#include <set>

typedef std::set<char> DigitsSet;

inline void setNumbers(DigitsSet& digits, const int number)
{
    std::stringstream ss_val;
    ss_val << number;
    for (auto c : ss_val.str())
    {
        digits.insert(c);
    }
}

int findLastNumberBeforeAsleep(const int startNumber)
{
    std::set<char> currentlyUsed;
    int currentNumber;
    int i = 1;
    do
    {
        currentNumber = startNumber * i;
        setNumbers(currentlyUsed, currentNumber);
        ++i;
    } while(currentlyUsed.size() != 10);

    return currentNumber;
}

int main()
{
    int T;

    std::cin >> T;
    for (auto i = 0; i < T; i++)
    {
        int N;
        std::cin >> N;

        std::cout << "Case #" << i + 1 << ": ";
        if (N != 0)
        {
            std::cout << findLastNumberBeforeAsleep(N) << std::endl;
        }
        else
        {
            std::cout << "INSOMNIA" << std::endl;
        }


    }

    return 0;
}