#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <memory>
#include <string.h>
#include <queue>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

const int maxn = 1005;
int a[maxn];

int f(int x) {
    return x * (x-1) / 2;
}


int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int tc; scanf("%d", &tc);
    for (int tt=1; tt<=tc; ++tt) {
        int n, m; scanf("%d %d", &n, &m);
        int total = 0;
        forn (i, n+1) a[i] = 0;
        forn (i, m) {
            int x, y, c; scanf("%d %d %d", &x, &y, &c);
            total += f(y - x) * c;
            for (int j=x-1; j<y-1; ++j)
                a[j] += c;
        }
        int res = 0;
        while (true) {
            bool any = false;
            forn (i, n) if (a[i]>0) {
                int c = a[i];
                any = true;
                int j;
                for (j=i; j<n && a[j]>0; ++j) c = min(c, a[j]);
                res += c * f(j-i);
                for (int k=i; k<j; ++k) a[k] -= c;
                i = j;
            }
            if (!any) break;
        }
        printf("Case #%d: %d\n", tt, res - total);


    }

    return 0;
}
