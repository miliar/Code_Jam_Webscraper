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

    int f;

    int T;
    fin >> T;
    for (int j = 0; j < T; j++)
    {
        int N;
        fin >> N;
        int m[1000];
        for (int i = 0; i < N; i++)
        {
            fin >> m[i];
        }

        int sum1 = 0;
        int sum2 = 0;
        int max = 0;
        for (int i = 0; i < N-1; i++)
        {
            if (m[i] > m[i+1])
            {
                sum1 += m[i] - m[i+1];
                if (max < m[i] - m[i+1])
                {
                    max = m[i] - m[i+1];
                }
            }
        }

        for (int i = 0; i < N-1; i++)
        {
            if (max < m[i])
            {
                sum2 += max;
            }
            else
            {
                sum2 += m[i];
            }
        }

        fout << "Case #" << j+1 << ": " << sum1 << " " << sum2 << endl;
    }

    return (0);
}
