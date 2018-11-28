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

vector<pair<int, int> > e[maxn];
int from[maxn], tof[maxn], lb[maxn], ub[maxn], way[maxn];

int wa[maxn];

int main() {
        int t, af, bf, n, m, p, cf, df;
        cin >> t;
        string s;
        for (int zi = 0; zi < t; ++zi) {
                cin >> n >> m >> p;
                for (int i = 0; i < n; ++i) e[i].clear();
                for (int i = 0; i < m; ++i) {
                        scanf("%d%d%d%d", &af, &bf, &cf, &df);
                        from[i] = af; tof[i] = bf; lb[i] = cf; ub[i] = df;
                }
                for (int i = 0; i < p; ++i) {
                        cin >> way[i];
                        --way[i];
                }
                int vzi;
                for (vzi = 0; vzi < p; ++vzi) {
                        int okie = 0;
                        for (int mi = 0; mi < (1 << m); ++mi) {
                                for (int j = 1; j <= n; ++j) e[j].clear();
                                for (int j = 0; j < m; ++j) {
                                        if ((1 << j) & mi)
                                                e[tof[j]].pb(mp(from[j], ub[j]));
                                        else
                                                e[tof[j]].pb(mp(from[j], lb[j]));
                                }
                                set<pair<int, int> > w;
                                w.insert(mp(0, 2));
                                for (int i = 1; i <= n; ++i)
                                        wa[i] = 1000000000;
                                wa[2] = 0;
                                while (w.size()) {
                                        int me = w.begin()->second;
                                        w.erase(w.begin());
                                        for (int i = 0; i < e[me].size(); ++i)
                                                if (wa[e[me][i].x] > wa[me] + e[me][i].y) {
                                                        w.erase(mp(wa[e[me][i].x], e[me][i].x));
                                                        wa[e[me][i].x] = wa[me] + e[me][i].y;
                                                        w.insert(mp(wa[e[me][i].x], e[me][i].x));
                                                }
                                }
                                int myc = 0;
                                for (int i = 0; i <= vzi; ++i)
                                        myc += (((1 << way[i]) & mi) ? ub[way[i]] : lb[way[i]]);
                                if (myc + wa[tof[way[vzi]]] == wa[1]) {
                                        okie = 1;
                                        //cout << myc << "+" << wa[tof[way[vzi]]] << " and " << wa[1] << endl;
                                        break;
                                }
                        }
                        if (!okie) break;
                }
                printf("Case #%d: ", zi + 1);
                if (vzi == p) cout << "Looks Good To Me\n";
                else cout << way[vzi] + 1 << endl;
        }
}
