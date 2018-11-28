#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;


int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;

    char t[100][100];
    for (int tc = 0; tc < T; tc++)
    {
        int N, M;
        fin >> N >> M;
        string ret = "YES";

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                fin >> t[i][j];
            }
        }

        int row[100];
        for (int i = 0; i < N; i++)
        {
            int max = 0;
            for (int j = 0; j < M; j++)
            {
                if (max < t[i][j])
                {
                    max = t[i][j];
                }
            }
            row[i] = max;
        }

        int col[100];
        for (int i = 0; i < M; i++)
        {
            int max = 0;
            for (int j = 0; j < N; j++)
            {
                if (max < t[j][i])
                {
                    max = t[j][i];
                }
            }
            col[i] = max;
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                int a = t[i][j];
                if (row[i] > a
                    && col[j] > a)
                {
                    ret = "NO";
                }
            }
        }

        fout << "Case #" << tc+1 << ": " << ret << endl;
    }

    return (0);
}
