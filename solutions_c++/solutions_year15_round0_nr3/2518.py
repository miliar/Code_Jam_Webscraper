#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
//#include <unordered_map>
//#include <unordered_set>
#include <stack>
#include <queue>

#include <iostream>
#include <algorithm>
#include <string>
#include <utility>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

const int QQ[4][4] =
{
        { 0, 1, 2, 3 },
        { 1, 0, 3, 2 },
        { 2, 3, 0, 1 },
        { 3, 2, 1, 0 }
};
/*const int SIGN[4][4] =
{
        { 1, 1, 1, 1 },
         { 1, -1, 1, -1},
         { 1, -1, -1, 1},
         { 1, 1, -1, -1}
};*/
const int SIGN[2][4][4] =
{
        {{ 0, 0, 0, 0 },
                 { 0, 1, 0, 1},
                 { 0, 1, 1, 0},
                 { 0, 0, 1, 1}},

        {{ 1, 1, 1, 1 },
         { 1, 0, 1, 0},
         { 1, 0, 0, 1},
         { 1, 1, 0, 0}}
};
const int DIV[2][4][4] =
{
        {{ 0, 0, 0, 0 },
                 { 1, 0, 1, 0},
                 { 1, 0, 0, 1},
                 { 1, 1, 0, 0}},

        {{ 1, 1, 1, 1 },
         { 0, 1, 0, 1},
         { 0, 1, 1, 0},
         { 0, 0, 1, 1}}
};

const int GG = 10000 + 1;

int pp[GG];

void zeroArray()
{
    memset(&pp, 0, GG * sizeof(pp[0]));
}

void printArray(int *arr)
{
    for (int i = 0; i < 10; ++i)
        printf("%d ", arr[i]);
    printf("\n");
}

int solve(int len, int times)
{
    int length = len * times;
    int a = pp[0], b, d, sa = 1, sb, sd;

    for (int i = 1; i < length; ++i)
    {
        if (a == 1 && sa == 1 && i + 1 < length)
        {
            b = pp[i];
            sb = 1;
            d = pp[i + 1];
            sd = 1;

            for (int j = i + 2; j < length; ++j)
            {
                int c = pp[j];
                sd = SIGN[sd][d][c];
                d = QQ[d][c];
            }
            if (b == 2 && sb == 1 && d == 3 && sd == 1)
                return 1;

            // Accumulate j until length - 2
            for (int j = i + 1; j + 1 < length; ++j)
            {
                int c = pp[j];
                sb = SIGN[sb][b][c];
                b = QQ[b][c];

                // Divide d by c
                sd = DIV[sd][c][d];
                d = QQ[c][d];

                if (b == 2 && sb == 1 && d == 3 && sd == 1)
                    return 1;
            }
        }
        int c = pp[i];
        sa = SIGN[sa][a][c];
        a = QQ[a][c];
    }
    return 0;
}

int main()
{
    clock_t tt = clock();
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
    {
        int len, times;
        int res;

        scanf("%d", &len);
        scanf("%d", &times);
        while (getchar() != '\n')
            ;

        for (int j = 0; j < len; ++j)
        {
            char c = getchar() - 'i' + 1;
            for (int k = 0; k < times; ++k)
                pp[j + len*k] = c;
            //printf("%d ", pp[j]);
        }
        res = solve(len, times);
        if (res == 1)
            printf("Case #%d: YES\n", i + 1);
        else
            printf("Case #%d: NO\n", i + 1);

        zeroArray();
        fflush(stdout);
    }
    tt = clock() - tt;
    //printf("Took %ld clicks/%f seconds\n", tt, ((float)tt)/CLOCKS_PER_SEC);

    return 0;
}
