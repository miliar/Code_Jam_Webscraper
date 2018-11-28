#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXN = 1010;

int n;
int a[MAXN];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        printf("Case #%d: ", test + 1);
        scanf("%d", &n);
        forn(i, n)
            scanf("%d", &a[i]);

        int ans = 0;

        int l = 0, r = n - 1;
        forn(i, n) {
            int mpos = l;
            forab(j, l + 1, r + 1)
                if (a[j] < a[mpos])
                    mpos = j;
            if (mpos - l < r - mpos) {
                ans += mpos - l;
                forba(j, mpos + 1, l + 1)
                    swap(a[j], a[j - 1]);
                l++;
            } else {
                ans += r - mpos;
                forab(j, mpos, r)
                    swap(a[j], a[j + 1]);
                r--;
            }
        }

        printf("%d\n", ans);

    }
    return 0;
}
