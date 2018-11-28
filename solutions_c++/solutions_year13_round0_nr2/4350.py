#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    // Create lawn
    int* Y = (int*)malloc(sizeof(int*)*100);
    int* X = (int*)malloc(sizeof(int*)*100);
    int** lawn = (int**)malloc(sizeof(int*)*100);
    for (int i = 0 ; i < 100 ; i++)
    {
        lawn[i] = (int*)malloc(sizeof(int)*100);
    }

    int tests;
    cin >> tests;
    string blank;
    getline(cin, blank);

    for (int t = 1; t <= tests; t++)
    {
        int n, m;
        cin >> n;
        cin >> m;
        getline(cin, blank);

        string result = "YES";
        for (int j = 0; j < n; j++)
        {
            Y[j] = -1;
        }
        for (int j = 0; j < m; j++)
        {
            X[j] = -1;
        }

        // Load board
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> lawn[i][j];
                if (lawn[i][j] > X[j])
                {
                    X[j] = lawn[i][j];
                }
                if (lawn[i][j] > Y[i])
                {
                    Y[i] = lawn[i][j];
                }
            }
            getline(cin, blank);
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (lawn[i][j] > X[j])
                {
                    result = "NO";
                }
                if (lawn[i][j] > Y[i])
                {
                    result = "NO";
                }
                if (lawn[i][j] != X[j] && lawn[i][j] != Y[i])
                {
                    result = "NO";
                }
            }
        }

        cout << "Case #" << t << ": " << result << "\n";
    }
}

