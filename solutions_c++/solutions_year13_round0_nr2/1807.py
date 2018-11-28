#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <limits>
#include <string>

using namespace std;

int N, M;
int w[100][100];

bool possible()
{
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            bool vert = true;
            bool horiz = true;
            for (int k = 0; k < i; ++k)
            {
                if (w[k][j] > w[i][j])
                {
                    vert = false;
                }
            }
            for (int k = i + 1; k < N; ++k)
            {
                if (w[k][j] > w[i][j])
                {
                    vert = false;
                }
            }
            for (int k = 0; k < j; ++k)
            {
                if (w[i][k] > w[i][j])
                {
                    horiz = false;
                }
            }
            for (int k = j + 1; k < M; ++k)
            {
                if (w[i][k] > w[i][j])
                {
                    horiz = false;
                }
            }
            if (!horiz && !vert)
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    fin >> T;
    for (int i = 1; i <= T; ++i)
    {
        fin >> N >> M;
        for (int j = 0; j < N; ++j)
        {
            for (int k = 0; k < M; ++k)
            {
                fin >> w[j][k];
            }
        }
        fout << "Case #" << i << ": " << (possible() ? "YES" : "NO") << endl;
    }
    return 0;
}
