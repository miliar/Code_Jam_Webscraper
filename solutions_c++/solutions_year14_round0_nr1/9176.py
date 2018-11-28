#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
    if (argc != 3)
    {
        cerr << "Invalid commandline parameters" << endl;
        return -1;
    }

    fstream input(argv[1], fstream::in);
    fstream output(argv[2], fstream::out | fstream::trunc);

    int numTestCases;
    input >> numTestCases;

    if (numTestCases < 1 || numTestCases > 100)
    {
        cerr << "Invalid number of test cases" << endl;
        return -1;
    }

    int firstRow, secondRow, card;
    int firstRowElements[4], answer;

    for (int i = 0; i < numTestCases; i++)
    {
        answer = -1;
        input >> firstRow;

        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                input >> card;
                if ((j + 1) == firstRow)
                {
                    firstRowElements[k] = card;
                }
            }
        }

        input >> secondRow;

        for (int j = 0; j < 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                input >> card;
                if ((j + 1) == secondRow)
                {
                    for (int l = 0; l < 4; l++)
                    {
                        if (firstRowElements[l] == card)
                        {
                            if (answer == -1)
                            {
                                answer = card;
                            }
                            else
                            {
                                answer = -2;
                            }
                        }
                    }
                }
            }
        }

        if (answer == -1)
        {
            output << "Case #" << (i + 1) << ": Volunteer cheated!" << endl;
        }
        else if (answer == -2)
        {
            output << "Case #" << (i + 1) << ": Bad magician!" << endl;
        }
        else
        {
            output << "Case #" << (i + 1) << ": " << answer << endl;
        }
    }
}