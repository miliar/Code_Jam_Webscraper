// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; ++i)
/*
#define cin fin
*/
#define cout fout

//ifstream fin(".in");
ofstream fout("res.out");

const int N = 8, M = 13, mod = 0;

int par[N], sz[N], esize[N], rsz[N];
int find(int v) { return v == par[v]? v: par[v] = find(par[v]); }
void unite(int u, int v) {
    u = find(u);
    v = find(v);
    if (u == v) {
        esize[v]++;
        return;
    }
    par[u] = v;
    sz[v] += sz[u];
    rsz[v] += rsz[u];
    esize[v] += esize[u];
    esize[v]++;
}
int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    rep(ntc, tc) {
        cout << "Case #" << ntc + 1 << ": ";
        // Clear Start
        // Clear End
        // Start
        int n;
        cin >> n;
        int emask = 0;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            for (int j = 0; j < n; ++j)
                if (s[j] == '1')
                    emask |= 1 << (i * n + j);
        }
        int res = 10000;
        for (int mask = 0; mask < (1 << (n * n)); ++mask) {
            if ((mask & emask) == emask) {
                int ok = 0;
                for (int i = 0; i < 2 * n; ++i)
                    rsz[i] = i & 1, esize[i] = 0, par[i] = i, sz[i] = (i & 1? -1: 1);
                for (int u = 0; u < n; ++u)
                    for (int v = 0; v < n; ++v) {
                        int e = u * n + v;
                        if (mask >> e & 1) {
                            unite(u << 1, v << 1 | 1);
                        }
                    }
                for (int v = 0; v < 2 * n; ++v) {
                    int g = find(v);
                    if (esize[g] == rsz[g] * rsz[g] && sz[g] == 0)
                        ok++;
                }
                if (ok == n * 2)
                    res = min(res, (int) __builtin_popcount(mask));
            }
        }
        // End
        cout << res - (int) __builtin_popcount(emask) << '\n';
      
    }
}













