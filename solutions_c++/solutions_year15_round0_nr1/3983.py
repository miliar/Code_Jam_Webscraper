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

const int SHY_MAX = 1000 + 1;

int nn[SHY_MAX];

int solve(int people)
{
    int res = 0, curr = nn[0];
    int i = 1;

    while (curr < people)
    {
        if (nn[i] == 0)
        {
            ++i;
        }
        else if (curr >= i)
        {
            curr += nn[i];
            ++i;
        }
        else
        {
            res += i - curr;    // Invite i - curr people
            people += i - curr;
            curr = i;
        }
    }
    return res;
}

void zeroArray()
{
    memset(&nn, 0, SHY_MAX * sizeof(nn[0]));
}

void printArray()
{
    for (int i = 0; i < 10; ++i)
        printf("%d ", nn[i]);
    printf("\n");
}

int main()
{
    //freopen("in", "r", stdin);
    //freopen("out", "w", stdout);

    int ncases;
    scanf("%d", &ncases);

    for (int i = 0; i < ncases; ++i)
    {
        int maxShyness, tmp, res;
        int people = 0;
        scanf("%d", &maxShyness);

        for (int j = 0; j <= maxShyness; ++j)
        {
            scanf("%1d", &tmp);
            nn[j] += tmp;
            people += tmp;
        }
        //printArray();
        res = solve(people);
        printf("Case #%d: %d\n", i + 1, res);

        zeroArray();
    }

    fflush(stdout);
    return 0;
}
