#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int T;
    fin >> T;

    for(int testCase = 1; testCase <= T; testCase++)
    {
        char arr[4][4];

        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                fin >> arr[i][j];

                if(arr[i][j] == '\n')
                {
                    j--;
                    continue;
                }
            }
        }

        bool xWin = false;
        bool yWin = false;
        bool isFull = true;

        for(int i = 0; i < 4; i++)
        {
            // horizontal
            int xCount = 0;
            int yCount = 0;

            for(int j = 0; j < 4; j++)
            {
                if(arr[i][j] == 'X')
                    xCount++;
                else if(arr[i][j] == 'O')
                    yCount++;
                else if(arr[i][j] == 'T')
                {
                    xCount++;
                    yCount++;
                }
                else
                    isFull = false;
            }

            if(xCount == 4)
            {
                xWin = true;
            }
            else if(yCount == 4)
            {
                yWin = true;
            }
        }

        for(int i = 0; i < 4; i++)
        {
            // vertical
            int xCount = 0;
            int yCount = 0;

            for(int j = 0; j < 4; j++)
            {
                if(arr[j][i] == 'X')
                    xCount++;
                else if(arr[j][i] == 'O')
                    yCount++;
                else if(arr[j][i] == 'T')
                {
                    xCount++;
                    yCount++;
                }
                else
                    isFull = false;
            }

            if(xCount == 4)
            {
                xWin = true;
            }
            else if(yCount == 4)
            {
                yWin = true;
            }
        }

        {
            // diagnoise 1
            int xCount = 0;
            int yCount = 0;

            for(int j = 0; j < 4; j++)
            {
                if(arr[j][j] == 'X')
                    xCount++;
                else if(arr[j][j] == 'O')
                    yCount++;
                else if(arr[j][j] == 'T')
                {
                    xCount++;
                    yCount++;
                }
                else
                    isFull = false;
            }

            if(xCount == 4)
            {
                xWin = true;
            }
            else if(yCount == 4)
            {
                yWin = true;
            }
        }

        {
            // diagnoise 2
            int xCount = 0;
            int yCount = 0;

            for(int j = 0; j < 4; j++)
            {
                if(arr[3 - j][j] == 'X')
                    xCount++;
                else if(arr[3 - j][j] == 'O')
                    yCount++;
                else if(arr[3 - j][j] == 'T')
                {
                    xCount++;
                    yCount++;
                }
                else
                    isFull = false;
            }

            if(xCount == 4)
            {
                xWin = true;
            }
            else if(yCount == 4)
            {
                yWin = true;
            }
        }

        cout << "Case #" << testCase << ": ";
        fout << "Case #" << testCase << ": ";

        if(xWin)
        {
            cout << "X won";
            fout << "X won";
        }
        else if(yWin)
        {
            cout << "O won";
            fout << "O won";
        }
        else if(isFull)
        {
            cout << "Draw";
            fout << "Draw";
        }
        else
        {
            cout << "Game has not completed";
            fout << "Game has not completed";
        }

        cout << endl;
        fout << endl;
    }

    return 0;
}