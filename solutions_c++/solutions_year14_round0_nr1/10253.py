#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main(int argc, char *argv[])
{
    int testCase = 0;
    ifstream input("A_1.in");
    input >> testCase;

    for (int c = 0; c < testCase; ++c)
    {
        int arrange1[4][4];
        int arrange2[4][4];
        int row1 = 0;
        int row2 = 0;

        input >> row1;

        for (int i = 0; i < 4; ++i)
        {
            int number = 0;
            for (int j = 0; j < 4; ++j)
            {
                input >> number;
                arrange1[i][j] = number;
            }
        }

        input >> row2;
        for (int i = 0; i < 4; ++i)
        {
            int number = 0;
            for (int j = 0; j < 4; ++j)
            {
                input >> number;
                arrange2[i][j] = number;
            }
        }

        int matches = 0;
        int match = 0;
        for (int i = 0; i < 4; ++i)
        {
            for (int j = 0; j < 4; ++j)
            {
                if (arrange1[row1 - 1][i] == arrange2[row2 - 1][j])
                {
                    ++matches;
                    match = arrange1[row1 - 1][i];
                    break;
                }
            }
        }

        cout << "Case #" << c + 1 << ": ";

        if (matches > 1)
        {
            cout << "Bad magician!" << endl;
        }
        else if (matches == 1)
        {
            cout << match << endl;
        }
        else
        {
            cout << "Volunteer cheated!" << endl;
        }
    }
    return 0;
}
