#include <functional>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); i++)
#define ford(i, n) for (int i = (int)(n)-1; i >= 0; i--)
#define mp make_pair
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define eq(x, y) (abs((x)-(y))<eps)
#define lt(x, y) ((x)<(y)-eps)
#define le(x, y) ((x)<=(y)+eps)
#define gt(x, y) ((x)>(y)+eps)
#define ge(x, y) ((x)>=(y)-eps)
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned int u32;
typedef double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int inf = 1e9+100500;
const int maxn = 100500;

bool pal(i64 x)
{
    string s;
    while (x) {
        s += '0'+x%10;
        x /= 10;
    }
    forn(i, s.size()/2) {
        if (s[i] != s[s.length()-i-1])
            return false;
    }
    return true;
}
bool ok(i64 x)
{
    return pal(x) && pal(x*x);
}

vector<i64> a;

void getpals()
{
    fore(i, 1, 10000005)
        if (ok(i))
           a.pb((i64)i*i);
}
int solve(i64 l, i64 r)
{
    int res = 0;
    forn(i, a.size())
        res += a[i] >= l && a[i] <= r;
    return res;
}

int main()
{
    freopen("C-large-1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    getpals();

    int t;
    cin >> t;
    forn(i, t) {
        i64 l, r;
        cin >> l >> r;
        cout << "Case #" << i+1 << ": " << solve(l, r) << endl;
    }

#ifdef HOME
    cerr << "time = " << clock()/1000 << " ms" << endl;
#endif
    return 0;
}
