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


const int INF = 1200000000, mod = 1000002013, maxn = 1006;

int dx[] = {-1, 0, 1,  0};
int dy[] = { 0, 1, 0, -1};


long double dp[1 << 21];

int x[maxn], y[maxn];

int best = -1;
int bst[maxn];
int usd[maxn], a[maxn];
int n;

struct pt {
        int x, y;
        pt() {}
        pt(int x, int y) : x(x), y(y) {}
};
 
inline int area (pt a, pt b, pt c) {
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
 
inline bool intersect_1 (int a, int b, int c, int d) {
        if (a > b)  swap (a, b);
        if (c > d)  swap (c, d);
        return max(a,c) <= min(b,d);
}
 
bool intersect (pt a, pt b, pt c, pt d) {
        return intersect_1 (a.x, b.x, c.x, d.x)
                && intersect_1 (a.y, b.y, c.y, d.y)
                && area(a,b,c) * area(a,b,d) <= 0
                && area(c,d,a) * area(c,d,b) <= 0;
}

void per(int i) {
        if (i < n) {
                for (int j = 0; j < n; ++j)
                        if (!usd[j]) {
                                usd[j] = 1;
                                a[i] = j;
                                per(i + 1);
                                usd[j] = 0;
                        }
        } else {
                int now = 0, ax, bx, ay, by;
                for (int j = 0; j < n; ++j) {
                        ax = x[a[j]], bx = x[a[(j + 1) % n]],
                        ay = y[a[j]], by = y[a[(j + 1) % n]];
                        now += ax * by - ay * bx;
                }
                for (int j = 0; j < n; ++j)
                        for (int k = 0; k < n; ++k)
                                if (j != k && (j != (k + 1) % n) && (k != ((j + 1) % n))) {
                                        if (intersect(pt(x[a[j]], y[a[j]]), pt(x[a[(j + 1) % n]], y[a[(j + 1) % n]]),
                                                      pt(x[a[k]], y[a[k]]), pt(x[a[(k + 1) % n]], y[a[(k + 1) % n]])))
                                                return;

                                }
                now = abs(now);
                if (now > best) {
                        best = now;
                        for (int j = 0; j < n; ++j) bst[j] = a[j];
                }
        }
}

int main() {
        int t, af, bf;
        cin >> t;
        string s;
        for (int zi = 0; zi < t; ++zi) {
                cin >> n;
                for (int i = 0; i < n; ++i) {
                        scanf("%d%d", &af, &bf);
                        x[i] = af; y[i] = bf;
                }
                a[0] = 0;
                usd[0] = 1;
                best = -1;
                per(1);
                printf("Case #%d: ", zi + 1);
                for (int i = 0; i < n; ++i)
                        cout << bst[i] << " ";
                cout << endl;
        }
}
