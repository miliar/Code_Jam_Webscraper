#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

using namespace std;

#define SMALL 1

string i2s(int i) { ostringstream os; os << i; return os.str(); }

bool sqr(int x)
{
    int a = sqrt(x);
    return a * a == x;
}

bool pal(string s)
{
    int n = SZ(s);
    REP(i,n/2) if (s[i] != s[n-i-1]) return false;
    return true;
}

bool check(int x)
{
    if (!sqr(x)) return false;
    int a = sqrt(x);
    string s1 = i2s(x), s2 = i2s(a);
    return pal(s1) && pal(s2);
}

int main()
{
#if SMALL
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
#else
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif

    int n, a, b;
    scanf("%d", &n);
    for (int tc = 1; tc <= n; ++tc) {
        scanf("%d%d", &a, &b);
        int ans = 0;
        for (int x = a; x <= b; ++x) {
            if (check(x)) ++ans;
        }
        printf("Case #%d: %d\n", tc, ans);
    }

    return 0;
}
