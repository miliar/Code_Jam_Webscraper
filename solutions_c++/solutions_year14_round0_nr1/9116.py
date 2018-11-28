#include <iostream>

using namespace std;

#define N 4 /// num rows/columns

void readRow(int row[N])
{
    int rowIndex = -1;
    cin >> rowIndex;

    int readRow[4] = { 0 };

    // reads the first selected row
    for (int i = 1; i <= N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            cin >> readRow[j];
        }
        if (i == rowIndex)
        {
            for (int j = 0; j < N; ++j)
            {
                row[j] = readRow[j];
            }
        }
    }

}


void solvePuzzle()
{
    int firstRow[4] = { 0 };
    readRow(firstRow);

    int secondRow[4] = { 0 };
    readRow(secondRow);

    int solution = -1;

    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (firstRow[i] == secondRow[j])
            {
                if (solution == -1)
                {
                    solution = firstRow[i];
                }
                else
                {
                    cout << "Bad magician!" << endl;
                    return;
                }
            }
        }
    }

    if (solution == -1)
        cout << "Volunteer cheated!" << endl;
    else
        cout << solution << endl;
}



int main()
{
    int T = 0; /// num test cases

    cin >> T;

    for (int i = 0; i < T; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solvePuzzle();

    }



    return 0;
}