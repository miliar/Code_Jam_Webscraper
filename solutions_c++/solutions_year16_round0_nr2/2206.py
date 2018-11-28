#include <iostream>
#include <string>
#include <vector>

using namespace std;

unsigned MinimumMoves(const string& pancakeStack)
{
    size_t numPancakes = pancakeStack.length();

    vector<unsigned> movesToMakeHappy(numPancakes + 1);
    vector<unsigned> movesToMakeSad(numPancakes + 1);

    for (size_t i = 1; i <= numPancakes; ++i)
    {
        if (pancakeStack[i - 1] == '+')
        {
            movesToMakeHappy[i] = movesToMakeHappy[i - 1];
            movesToMakeSad[i] = movesToMakeHappy[i - 1] + 1;
        }
        else
        {
            movesToMakeHappy[i] = movesToMakeSad[i - 1] + 1;
            movesToMakeSad[i] = movesToMakeSad[i - 1];
        }
    }

    return movesToMakeHappy[numPancakes];
}

int main ()
{
    unsigned numTestCases;

    cin >> numTestCases;

    for (unsigned testCase = 1; testCase <= numTestCases; ++testCase)
    {
        string pancakeStack;
        cin >> pancakeStack;

        unsigned moves = MinimumMoves(pancakeStack);

        printf_s("Case #%u: %u\n", testCase, moves);
    }

    return 0;
}
