#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x) * (x))
using namespace std;

int a[20000000], b[100], n;

int cal(long long x)
{
    n = 0;
    while (x)
    {
        b[++n] = x % 10;
        x /= 10;
    }
    for (int i = 1; i <= n / 2; i++)
    if (b[i] != b[n - i + 1]) return 0;
    return 1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    for (long long i = 1; i <= 10000000; ++i)
    if (cal(i) && cal(sqr(i)))
        a[i] = a[i - 1] + 1;
    else a[i] = a[i - 1];
    int m; scanf("%d", &m);
    for (int i = 0; i < m; i++)
    {
        long long s, t; cin >> s >> t;
        printf("Case #%d: %d\n", i + 1, a[(int)sqrt(t)] - a[(int)sqrt(s - 1)]);
    }
    return 0;
}
