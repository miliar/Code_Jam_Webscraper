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

int n;
int x, y;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d", &T);
    forn(t, T) {
        printf("Case #%d: ", t + 1);
        cin >> n >> x >> y;
        for(int i = 0; i < abs(x) + y; i += 2) {
            n -= 1 + 2 * i;
            if (n <= 0)
                break;
        }
        if (n <= 0) {
            printf("0.0\n");
            continue;
        }

        if (n >= 1 + 2 * (abs(x) + y)) {
            printf("1.0\n");
            continue;
        }

        if (x == 0) {
            printf("0.0\n");
            continue;
        }

        ldb ans = 0.0L, ans2 = 0.0L, cur = 1.0L;
        int z = y + 1;
        int k = abs(x) + y;
        int col = 0;

        if (n - k < z) {
            ldb cur2 = 1.0L;
            int col2 = 0;
            forab(s, k - 1, n) {
                ans2 += cur2;
                cur2 *= (s + 1) / (2.0L * (s - k + 2));
                while (col2 < k && (ans2 - 1.0L > -EPS || cur2 - 1.0L > -EPS)) {
                    col2++;
                    ans2 /= 2.0L;
                    cur2 /= 2.0L;
                }
            }
            forab(s, col2, k)
                ans2 /= 2.0L;
        }

        forab(i, 1, z + 1) {
            if (i - 1 > n - k) ans += cur;

            cur *= (n - i + 1) * 1.0L / i;
            while (col < n && (ans - 1.0L > -EPS || cur - 1.0L > -EPS)) {
                col++;
                ans /= 2.0L;
                cur /= 2.0L;
            }
        }
        forab(i, col, n)
            ans /= 2.0L;
        printf("%.10lf\n", double(1.0L - ans - ans2));

    }
    return 0;
}
