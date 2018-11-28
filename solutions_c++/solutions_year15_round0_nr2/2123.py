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
        int D;
        fin >> D;
        int P[1000];
        for (int i = 0; i < D; i++)
        {
            fin >> P[i];
        }

//        int a[1000] = {0};
        int max = 0;
        for (int i = 0; i < D; i++)
        {
//            fout << P[i] << " ";
//            a[P[i]]++;
            if (max < P[i])
            {
                max = P[i];
            }
        }

        int ans = max;
        for (int i = 1; i < max; i++)
        {
            int c = 0;
            for (int k = 0; k < D; k++)
            {
                c += (P[k] + i-1) / i - 1;
            }

            if (ans > i + c)
            {
                ans = i + c;
            }
        }

        fout << "Case #" << j+1 << ": " << ans << endl;
    }

    return (0);
}
