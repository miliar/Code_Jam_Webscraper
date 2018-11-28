#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <bitset>
#include <cstring>
#include <string>
#include <cmath>
#include <queue>
#pragma comment (linker, "/STACK:256000000")

using namespace std;
const int NMax = 150;
const int MMax = 150;
const int MAX_HEIGHT = 101;
int lawn[NMax][MMax];
int N, M;

void solve(int test)
{
    // read test input
    cin >> N >> M;
    int LawnMaxHeight = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            cin >> lawn[i][j];
            LawnMaxHeight = max(LawnMaxHeight, lawn[i][j]);
        }

    for (int height = 1; height <= LawnMaxHeight; height++)
    {
        // Check valid lines
        for (int i = 0; i < N; i++)
        {
            bool validLine = true;
            for (int j = 0; j < M; j++)
            {
                if (lawn[i][j] < height && lawn[i][j] != MAX_HEIGHT)
                {
                    cout << "Case #" << test << ": NO" << endl;
                    return;
                }
                else if (lawn[i][j] > height && lawn[i][j] != MAX_HEIGHT) 
                {
                    validLine = false;
                    break;
                }
            }
            if (validLine)
            {
                // increase the grass size to MAX.
                for (int j = 0; j < M; j++)
                    lawn[i][j] = MAX_HEIGHT;
            }            
        }
        

        // Check valid columns
        for (int j = 0; j < M; j++)
        {
            bool validColumn = true;
            for (int i = 0; i < N; i++)
            {
                if (lawn[i][j] < height && lawn[i][j] != MAX_HEIGHT)
                {
                    cout << "Case #" << test << ": NO" << endl;
                    return;
                }
                else if (lawn[i][j] > height && lawn[i][j] != MAX_HEIGHT) 
                {
                    validColumn = false;
                    break;
                }
               
            }
            if (validColumn)
            {
                // increase the grass size to MAX.
                for (int i = 0; i < N; i++)
                    lawn[i][j] = MAX_HEIGHT;
            }            
        }
    }

    // Check for grass height
    for (int i = 0; i < N; i++)
       for (int j = 0; j < M; j++)
            if (lawn[i][j] != MAX_HEIGHT)
            {
                cout << "Case #" << test << ": NO" << endl;
                return;
            }
      
    cout << "Case #" << test << ": YES" << endl; 
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cout << "Usage: %s inputfile" << argv[0];
        return 1;
    }
    freopen(argv[1], "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests = 0;
    cin >>  tests;
    for (int i = 1; i <= tests; i++)
        solve(i);

    return 0;
}