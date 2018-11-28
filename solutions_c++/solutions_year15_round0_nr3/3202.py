#include <iostream>

char multiply(char q1, char q2, int& sign)
{
    char table[4][4] = { '1', 'i', 'j', 'k',
                                     'i', '1', 'k', 'j',
                                     'j', 'k', '1', 'i',
                                     'k', 'j', 'i', '1' };

    int signTable[4][4] = { 1, 1, 1, 1,
                                        1, -1, 1, -1,
                                        1, -1, -1, 1,
                                        1, 1, -1, -1 };

    int q1v = (q1 == '1'? 0: q1 == 'i'? 1: q1 == 'j'? 2: 3);
    int q2v = (q2 == '1'? 0: q2 == 'i'? 1: q2 == 'j'? 2: 3);

    sign *= signTable[q1v][q2v];

    return table[q1v][q2v];
}

int main()
{
    int testCases;
    std::cin >> testCases;

    for (int testCaseCounter = 0; testCaseCounter < testCases; testCaseCounter++)
    {
        std::string baseStr;
        int noDigits, repetitions;

        std::cin >> noDigits >> repetitions >> baseStr;

        std::string finalStr;
        for (int i = 0; i < repetitions; i++)
            finalStr += baseStr;

        char c = '1';
        int sign = 1;

        int pos;
        for (pos = 0; pos < finalStr.size(); pos++)
        {
            c = multiply(c, finalStr[pos], sign);

            if (c == 'i' && sign == 1)
                break;
        }

        if (pos == finalStr.size())
            goto NEGATIVE;

        c = '1';
        sign = 1;

        for (pos++; pos < finalStr.size(); pos++)
        {
            c = multiply(c, finalStr[pos], sign);

            if (c == 'j' && sign == 1)
                break;
        }

        if (pos == finalStr.size())
            goto NEGATIVE;

        c = '1';
        sign = 1;

        for (pos++; pos < finalStr.size(); pos++)
            c = multiply(c, finalStr[pos], sign);

        if (c != 'k' || sign != 1)
            goto NEGATIVE;

        std::cout << "Case #" << int(testCaseCounter + 1) << ": " << "YES" << std::endl;
        goto END;

        NEGATIVE:
        std::cout << "Case #" << int(testCaseCounter + 1) << ": " << "NO" << std::endl;

        END: ;
    }

    return 0;
}