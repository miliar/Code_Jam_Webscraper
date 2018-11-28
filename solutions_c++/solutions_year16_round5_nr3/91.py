// polygamy at home, a six-part miniseries
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
#include <iomanip>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
typedef long long ll;
const int N = 1111;
const double INF = 1e18;
int n, s;
ll xs[N], ys[N], zs[N], xv[N], yv[N], zv[N];

pair<double, double> getEdge(int i, int j, double mx) {
    ll vx = xv[i] - xv[j];
    ll vy = yv[i] - yv[j];
    ll vz = zv[i] - zv[j];

    ll cd = (xs[i] - xs[j]) * (xs[i] - xs[j])
            + (ys[i] - ys[j]) * (ys[i] - ys[j])
            + (zs[i] - zs[j]) * (zs[i] - zs[j]);

    if(vx == 0 && vy == 0 && vz == 0) {
        if(cd <= mx * mx) return {0, INF};
        else return { -1, -1};
    }

    double a = vx * vx + vy * vy + vz * vz;
    double b = 2 * (vx * (xs[i] - xs[j]) + vy * (ys[i] - ys[j]) + vz * (zs[i] - zs[j]));
    double c = cd - mx * mx;
    double d = b * b - 4 * a * c;
    if(d < 0) return { -1, -1};
    if(a == 0) return {0, INF};
    double t1 = (-b + sqrt(d)) / (2 * a);
    double t2 = (-b - sqrt(d)) / (2 * a);
    if(t1 > t2) swap(t1, t2);
    return {max(0.0,t1), t2};
}

double efr[N][N], eto[N][N], bt[N][N];
bool done[N][N];
typedef pair<int, int> Edge;

bool go(double mx) {
    memset(done, 0, sizeof(done));
    rep(i, 0, n) rep(j, 0, n) bt[i][j] = INF;

    rep(i, 0, n) efr[i][i] = eto[i][i] = -1;
    rep(i, 0, n) rep(j, i + 1, n) {
        pair<double, double> cur = getEdge(i, j, mx);
        efr[i][j] = cur.first, efr[j][i] = cur.first;
        eto[i][j] = cur.second, eto[j][i] = cur.second;
    }

    set<pair<double, Edge>> q;
    rep(i, 1, n) {
        if(efr[0][i] < 0) continue;
        if(efr[0][i] > s) continue;
        q.insert({efr[0][i], {0, i}});

    }

    auto update = [&](int ci, int cj, int ni, double ct) {
        if(done[ci][ni] || efr[ci][ni] < 0) return;
        if(eto[ci][ni] >= ct && efr[ci][ni] <= eto[ci][cj] + s) {
            double nt = max(ct, efr[ci][ni]);
            if(nt < bt[ci][ni]) {
                Edge ne = {min(ci, ni), max(ci, ni)};
                if(bt[ci][ni] < INF) {
                    q.erase({bt[ci][ni], ne});
                }
                bt[ci][ni] = bt[ni][ci] = nt;
                q.insert({nt, ne});
            }
        }
    };

    while(!q.empty()) {
        double ct;
        int ci, cj;
        ct = q.begin()->first;
        tie(ci, cj) = q.begin()->second;
        q.erase(q.begin());
        if(ci==1 || cj==1) return true;
        //cout<<ci<<" "<<cj<<" "<<ct<<endl;
        done[ci][cj] = done[cj][ci] = true;

        rep(ni, 0, n) {
            update(ci, cj, ni, ct);
            update(cj, ci, ni, ct);
        }
    }

    return false;
}

void solve() {
    cin >> n >> s;

    rep(i, 0, n) {
        cin >> xs[i] >> ys[i] >> zs[i] >> xv[i] >> yv[i] >> zv[i];
    }
    double from = 0, to = 2000;
    rep(it,0,60){
        double avg = (from+to)/2;
        if(go(avg)){
            to = avg;
        } else {
            from = avg;
        }
    }
    cout << from;
}

int main() {
    if(0) freopen("in.txt", "r", stdin);
    else {
        freopen("/home/vaclav/Downloads/C-small-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
    }
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(12);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
