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


const int INF = 1200000000, mod = 1000002013, maxn = 510000;

long long p;

int maxpos(long long l, long long r, long long all, long long a) {
        if (l > r || r < p) return 0;
        if (l >= p) return 1;
        long long m = (l + r) / 2;
        if (maxpos(l, m, all / 2,     min(a, (all - 1) / 2))) return 1;
        if (a - 1 >= 0 && maxpos(m + 1, r, all / 2, (a - 1) / 2)) return 1;
        return 0;
}

int minpos(long long l, long long r, long long all, long long a) {
        if (l > r || l >= p) return 0;
        if (r < p) return 1;
        long long m = (l + r) / 2;
        if (minpos(m + 1, r, all / 2,     min(a, (all - 1) / 2))) return 1;
        if (a - 1 >= 0 && minpos(l, m, all / 2, (a - 1) / 2)) return 1;
        return 0;
}

int main() {
        long long n;
        int t;
        cin >> t;
        for (int zi = 0; zi < t; ++zi) {
                cin >> n >> p;
                long long l, r, m;

                printf("Case #%d: ", zi + 1);
                l = 0, r = (1ll << n) - 1;
                long long all = (1ll << n);
                while (l < r) {
                        m = (l + r + 1) / 2;
                        if (maxpos(0, all - 1, all, m))
                                r = m - 1;
                        else l = m;
                }
                cout << l << " ";
                l = 0, r = (1ll << n) - 1;
                while (l < r) {
                        m = (l + r + 1) / 2;
                        if (minpos(0, all - 1, all, all - m - 1))
                                l = m;
                        else r = m - 1;
                }
                cout << l << endl;
        }
}
