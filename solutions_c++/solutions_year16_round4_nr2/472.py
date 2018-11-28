#include <cstdio>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <iostream>
#include <cassert>
#include <memory.h>
using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define pb push_back
typedef long long ll;
typedef pair<int, int> pii;
typedef long double ld;

double f[210][210];
int a[210];
vector<int> ta[100];


double solve(vector<int>& a) {
    int n, k;
    double p[210];
    scanf("%d %d", &n, &k);
    forn(i, n) scanf("%lf", &p[i]);
    sort(p, p + n);
    double ans = 0;

    if (a.empty()) {
        forn(i, k) {
            a.push_back(i);
            a.push_back(n - 1 - i);
        }
        forn(i, n - 2 * k) {
            a.push_back(k + i);
        }
    }

    int zi = 0, zj = 0;
    forn(it, 10000) {
        if (k != 0 && k != n) {
            zi = rand() % k;
            zj = k + rand() % (n - k);
        }
        swap(a[zi], a[zj]);
        f[0][0] = 1;
        int c = 0;
        forn(j, k) {
            forn(zz, c + 2) f[c+1][zz] = 0;
            for (int q = 0; q <= c; ++q) {
                f[c+1][q+1] += f[c][q] * p[a[j]];
                f[c+1][q] += f[c][q] * (1 - p[a[j]]);
            }
            c++;
        }

        if (f[c][k / 2] > ans) {
            ans = f[c][k / 2];
        } else {
            swap(a[zi], a[zj]);
        }

        if (k == 0 || k == n) break;
    }
    return ans;
}

double best[110];

int main() {
    srand(time(0));
    while (true) {
        freopen("B.in", "r", stdin);
        int tc;
        scanf("%d", &tc);
        for (int q = 1; q <= tc; q++) {
            double z = solve(ta[q - 1]);
            if (z > best[q] + 1e-7) {
                fprintf(stderr, "[%d] %.8f -> %.8f\n", q, best[q], z);
                best[q] = z;
                freopen("B.out", "w", stdout);
                for (int w = 1; w <= tc; w++) {
                    printf("Case #%d: %.8f\n", w, best[w]);
                }
                fclose(stdout);
            }
            // fprintf(stderr, "%d of %d done...\n", q, tc);
        }
        fclose(stdin);
    }
    return 0;
}
