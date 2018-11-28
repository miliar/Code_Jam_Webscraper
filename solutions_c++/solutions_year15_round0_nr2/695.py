#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
using namespace std;

#define MAXP 1111

int n, p[MAXP];

int solve()
{
    int res = MAXP;
    for(int t = 1; t <= MAXP; t++)
    {
        int moves = 0;
        for(int i = 0; i < n; i++) moves += (p[i] + t - 1) / t - 1;
        res = min(res, moves + t);
    }
    return res;
}

int main()
{
    freopen("b2.in", "r", stdin);
    freopen("b2.out", "w", stdout);
    int testcnt;
    cin >> testcnt;
    for(int i = 1; i <= testcnt; i++)
    {
        cin >> n;
        for(int i = 0; i < n; i++) cin >> p[i];
        printf("Case #%d: %d\n", i, solve());
    }
}
