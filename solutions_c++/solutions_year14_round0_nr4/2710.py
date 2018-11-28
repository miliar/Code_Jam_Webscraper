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

const ldb EPS = 1e-9;

const int MAXN = 1010;

int n;
ldb x[2][MAXN];
int ans[2];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        printf("Case #%d: ", test + 1);

        scanf("%d", &n);
        forn(q, 2) {
            forn(i, n) {
                double tmp;
                scanf("%lf", &tmp);
                x[q][i] = tmp;
            }
            sort(x[q], x[q] + n);
        }

        forn(q, 2) {
            ans[q] = 0;
            int i = 0, j = 0;
            while (i < n && j < n) {
                if (x[q][i] > x[1 - q][j]) {
                    j++;
                    continue;
                }
                ans[q]++;
                i++, j++;
            }
        }

        printf("%d %d\n", ans[1], n - ans[0]);

    }
    return 0;
}
