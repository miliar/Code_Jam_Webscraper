/*
 * File:   main.cpp
 * Author: Jon la Cour
 *
 * Created on April 13, 2013, 1:26 PM
 */

#include <fstream>
#include <sstream>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

int N, M;
bool ok;
int lawn[110][110];

bool check(int pattern, int x, int y)
{
    int checkCol = 0, checkRow = 0;
    for (int col = 0; col < M; col++)
    {
        if (lawn[x][col] <= pattern) checkCol++;
        else break;
    }

    for (int row = 0; row < N; row++)
    {
        if (lawn[row][y] <= pattern) checkRow++;
        else break;
    }

    if (checkCol == M || checkRow == N) return true;
    else return false;

}

int main()
{
    int test, count = 1;
    scanf("%d", &test);
    while (test--)
    {
        scanf("%d%d", &N, &M);

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                scanf("%d", &lawn[i][j]);
            }
        }

        ok = true;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                int pattern = lawn[i][j];
                ok = check(pattern, i, j);
                if (!ok) break;
            }
            if (!ok) break;
        }

        fstream filestr;
        filestr.open ("output.txt", fstream::in | fstream::out | fstream::app);

        std::ostringstream s;
        s << "Case #" << count++;
        std::string result = s.str() + ": ";

        if (ok)
        {
            result += "YES";
        }
        else
        {
            result += "NO";
        }

        filestr<<result<<endl;
        filestr.close();
    }
    return 0;
}
