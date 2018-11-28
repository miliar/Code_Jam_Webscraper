#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 100010;

int n, x;
int s[MAXN];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(testNum, T) {
        printf("Case #%d: ", testNum + 1);
        scanf("%d%d", &n, &x);
        forn(i, n)
            scanf("%d", &s[i]);
        sort(s, s + n);
        int ans = 0;
        int l = 0, r = n - 1;
        while (l <= r) {
            if (l != r && s[l] + s[r] <= x) {
                l++, r--;
                ans++;
            } else {
                r--;
                ans++;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
