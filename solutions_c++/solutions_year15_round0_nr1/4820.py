#include <iostream>

int main()
{
    int testCases;
    std::cin >> testCases;

    for (int testCaseCounter = 0; testCaseCounter < testCases; testCaseCounter++)
    {
        int maxShyness;
        std::cin >> maxShyness;

        std::string shynessStr;
        std::cin >> shynessStr;

        int extras = 0;
        int people = 0;

        for (int i = 0; i <= maxShyness; i++)
        {
            int tempExtras = 0;
            if (people < i)
                tempExtras = i - people;

            extras += tempExtras;
            people += (shynessStr[i] - '0') + tempExtras;
        }

        std::cout << "Case #" << int(testCaseCounter + 1) << ": " << extras << std::endl;
    }

    return 0;
}