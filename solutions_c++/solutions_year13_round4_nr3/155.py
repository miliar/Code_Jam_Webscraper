#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

#define ll long long
#define point pair<double, double>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define uint unsigned int
#define merge botva
#define M_PI 3.14159265358979323846
#define left b1
#define right b2

#define plus botva12


const int INF = 1200000000, mod = 1000002013, maxn = 510;

int n;
int a[maxn], b[maxn], at[maxn], za[maxn], usd[maxn];
bool tcan[1 << 21];

int can() {
        memset(tcan, 0, sizeof tcan);
        tcan[0] = 1;
        int hm;
        for (int i = 0; i < (1 << n); ++i) if (tcan[i]) {
                hm = 1;
                for (int j = 0; j < n; ++j) hm += (((1 << j) & i) != 0);
                for (int j = (at[hm] ? at[hm] - 1 : 0); j < n; ++j) if (!((1 << j) & i)) {
                        int ma = 1, mb = 1;
                        for (int k = 0; k < j; ++k)
                                if (((1 << k) & i)) ma = max(ma, a[k] + 1);
                        for (int k = j + 1; k < n; ++k)
                                if (((1 << k) & i)) mb = max(mb, b[k] + 1);
                        if (ma == a[j] && mb == b[j]) tcan[i | (1 << j)] = 1;
                        if (at[hm]) break;
                }
        }
        return tcan[(1 << n) - 1];
}

int main() {
        int t;
        cin >> t;
        for (int zi = 0; zi < t; ++zi) {
                cin >> n;
                for (int i = 0; i < n; ++i)
                        scanf("%d", &a[i]);
                for (int i = 0; i < n; ++i)
                        scanf("%d", &b[i]);

                printf("Case #%d: ", zi + 1);
                memset(at, 0, sizeof at);
                memset(za, 0, sizeof za);
                memset(usd, 0, sizeof usd);
                for (int i = 1; i <= n; ++i) {
                        for (int j = 1; j <= n; ++j) {
                                if (!usd[j]) {
                                        za[i] = j;
                                        at[j] = i;
                                        usd[j] = 1;
                                        if (can()) {
                                                cout << j << " ";
                                                break;
                                        }
                                        at[j] = 0;
                                        usd[j] = 0;
                                }
                        }
                }
                cout << endl;
        }
}
