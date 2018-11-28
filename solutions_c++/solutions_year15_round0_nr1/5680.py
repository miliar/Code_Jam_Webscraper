#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cassert>
using namespace std;

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

const int N = 1005;

int n;
char s[N];

void solve()
{
    scanf("%d%s", &n, s);
    n++;

    int has = s[0] - '0';
    int added = 0;

    for (int i = 1; i < n; i++)
    {
        if (has < i)
        {
            int x = i - has;
            has += x;
            added += x;
        }
        has += s[i] - '0';
    }

    printf("%d\n", added);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double) clock() / CLOCKS_PER_SEC);

    return 0;
}
