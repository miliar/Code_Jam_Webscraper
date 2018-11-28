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

int n, m, k, af, bf;

const int INF = 1200000000, mod = 1000002013, maxn = 510000;
map<int, long long> hom;

int main() {
        int af, bf, t, w, l, cf;
        cin >> t;
        for (int zi = 0; zi < t; ++zi) {
                cin >> n >> m;
                vector<pair<pair<int, int>, int> > e;
                long long dcnt = 0;
                for (int i = 0; i < m; ++i) {
                        scanf("%d%d%d", &af, &bf, &cf);
                        long long raised = n - (bf - af);
                        dcnt = (dcnt + ((((n * (n + 1ll) / 2) - raised * (raised + 1ll) / 2) % mod) * cf) % mod) % mod;
                        e.pb(mp(mp(af, bf), cf));
                        e.pb(mp(mp(bf, INF), cf));
                }
                sort(e.begin(), e.end());
                set<pair<int, long long> > tps;
                hom.clear();
                long long cnt = 0;
                for (int i = 0; i < e.size(); ++i) {
                        if (e[i].x.y == INF) {
                                while (e[i].y > 0) {
                                        int fromv = tps.begin()->first;
                                        long long was = tps.begin()->second;
                                        long long sell = min(e[i].y + 0ll, tps.begin()->second);
                                        tps.erase(tps.begin());
                                        hom[fromv] -= sell;
                                        e[i].y -= sell;
                                        //cout << "pay from " << fromv << " to " << e[i].x.x << " " << sell << " times.\n";
                                        if (was - sell > 0) tps.insert(mp(fromv, was - sell));
                                        long long raised = n - (e[i].x.x - (-fromv));
                                        cnt = (cnt + (sell * (((n * (n + 1ll) / 2) - raised * (raised + 1ll) / 2) % mod)) % mod) % mod;
                                }
                        } else {
                                tps.erase(mp(-e[i].x.x, hom[-e[i].x.x]));
                                hom[-e[i].x.x] += e[i].y;
                                tps.insert(mp(-e[i].x.x, hom[-e[i].x.x]));
                        }
                } 
                //cout << "pay " << cnt << " instead " << dcnt << endl;
                cnt = (dcnt - cnt + mod) % mod;
                printf("Case #%d: ", zi + 1);
                cout << cnt << endl;
        }
}
