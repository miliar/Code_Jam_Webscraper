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

#define MAX(a, b) ((a)<(b) ? (b):(a))
#define MIN(a, b) ((a)< b) ? (a):(b))

const int GG = 1000 + 1;

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

int solve(int most)
{
    int turns = 0, low = most;

    while (most > 0)
    {
        //printArray();
        int a = most, b = 0, c = most / 2;

        // Next nonzero value
        for (int i = most - 1; i >= 0; --i)
        {
            if (pp[i] != 0)
            {
                b = i;
                break;
            }
        }

        // Determine whether to eat or not
        if (a > 3 && pp[a] <= a - b)
        {
            // Move pancakes
            pp[c] += pp[a];
            pp[a - c] += pp[a];

            most = max(b, max(a - c, c));
            turns += pp[a];

            //printf("Split %d into %d and %d\n", a, a-c, c);
        }
        else
        {
            // Eat
            for (int i = 1; i < most; ++i)
                pp[i] = pp[i + 1];
            --most;
            ++turns;
        }
        if (turns + most < low)         // If split too much
            low = turns + most;
    }

    return min(turns, low);
}

int solve2(int *plates, int most, int turns)
{
    if (most == 0)
        return turns;
    else if (most == 1)
        return turns + 1;

    int a = most, b = 0, c = a / 2, d;

    // Next nonzero value
    for (int i = most - 1; i >= 0; --i)
    {
        if (plates[i] != 0)
        {
            b = i;
            break;
        }
    }

    // Split
    int r1 = 999999999;
    for (c = 2; c <= a - 2; ++c)
    {
        d = max(b, max(a - c, c));

        int *pnew = new int[d + 1];
        for (int i = 0; i <= d; ++i)
            pnew[i] = plates[i];

        pnew[c] += plates[a];
        pnew[a - c] += plates[a];
        r1 = min(r1, solve2(pnew, d, turns + plates[a]));
        delete[] pnew;
    }

    // Don't split
    d = most - 1;

    int *dnew = new int[d + 1];
    for (int i = 0; i <= d; ++i)
        dnew[i] = plates[i + 1];

    int r2 = solve2(dnew, d, turns + 1);

    delete[] dnew;
    return min(r1, r2);
}

int solve2(int most)
{
    int *pnew = new int[most + 1];
    for (int i = 0; i <= most; ++i)
        pnew[i] = pp[i];

    int res = solve2(pnew, most, 0);

    delete[] pnew;
    return res;
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; ++i)
    {
        int plates, tmp, max = 0;
        int res;

        scanf("%d", &plates);

        for (int j = 0; j < plates; ++j)
        {
            scanf("%d", &tmp);
            ++pp[tmp];
            if (tmp > max)
                max = tmp;
        }
        res = solve2(max);
        printf("Case #%d: %d\n", i + 1, res);

        zeroArray();
    }

    fflush(stdout);
    return 0;
}
