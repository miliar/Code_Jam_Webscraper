#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("B-large.txt", ios::in);
    if (!fin.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    fout.open("B-large-solution.txt", ios::out);
    if(!fout.is_open())
    {
        cerr << "Unable to open file" << endl;
        exit(10);
    }

    int testCases, n, m;
    fin >> testCases;

    for (int i = 1; i < testCases+1; i++)
    {
        fin >> n;
        fin >> m;
        int matrix[n][m];
        int count(0);

        for (int row = 0; row < n; row++)
        {
            for (int col = 0; col < m; col++)
            {
                fin >> matrix[row][col];
            }
        }

        for (int row = 0; row < n; row++)
        {
            for (int col = 0; col < m; col++)
            {
                int countV(0), countH(0);

                for (int row1 = 0; row1 < n; row1++)
                {
                    if (matrix[row][col] < matrix[row1][col])
                    {
                        countV++;
                    }
                }

                for (int col1 = 0; col1 < m; col1++)
                {
                    if (matrix[row][col] < matrix[row][col1])
                    {
                        countH++;
                    }
                }

                if (countH != 0 && countV != 0)
                {
                    count++;
                }
            }
        }

        if (count > 0)
        {
            fout << "Case #" << i << ": NO" << endl;
        }

        else
        {
            fout << "Case #" << i << ": YES" << endl;
        }

    }




    fin.close();
    fout.close();

    return 0;
}
