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

const int N = 1 << 12;

map<string, int> dist;
string q[N];

void solve()
{
    string start;
    cin >> start;
    int n = (int)start.length();
    dist.clear();
    dist[start] = 0;
    int ql = 0, qr = 0;
    q[qr++] = start;

    while (ql < qr)
    {
        string v = q[ql++];
        for (int i = 0; i < n; i++)
        {
            string to = v;
            reverse(to.begin(), to.begin() + i + 1);
            for (int j = 0; j <= i; j++)
                to[j] = to[j] == '+' ? '-' : '+';
            if (dist.count(to) == 0)
            {
                dist[to] = dist[v] + 1;
                q[qr++] = to;
            }
        }
    }

    printf("%d\n", dist[string(n, '+')]);
}

int main()
{
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
    }

    eprintf("time = %.3lf\n", (double)clock() / CLOCKS_PER_SEC);

    return 0;
}
