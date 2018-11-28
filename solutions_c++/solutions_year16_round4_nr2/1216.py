#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <cstring>
#include <fstream>

using namespace std;

#define EPS 1e-9

typedef long double ld;

vector<double> p;

int n, k;
vector<double> v;
bool used[20][20];
double dyn[20][20];

double rec(int cur, int left) {
    double &ret = dyn[cur][left];
    if (used[cur][left]) return ret;
    ret = 0.0;
    used[cur][left] = true;
    if (cur == k) {
        return ret = (left == 0);
    }
    if (v[cur] > EPS && left > 0) {
        ret += v[cur] * rec(cur+1, left-1);
    }
    if (v[cur] < (1-EPS)) {
        ret += (1-v[cur]) * rec(cur+1, left);
    }
    return ret;
}

double calc(int mask) {
    v.clear();
    for(int i=0; i<n; ++i) {
        if ((mask>>i) & 1) {
            v.push_back(p[i]);
        }
    }
    memset(used, 0, sizeof(used));
    return rec(0, k/2);
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, NT, i, j;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>n>>k;
        p.clear();
        p.resize(n);
        for(i=0; i<n; ++i) {
            cin>>p[i];
        }
        double res;
        res = 0.0;
        for(i=0; i<(1<<n); ++i) {
            if (__builtin_popcount(i) != k) continue;
            double cur;
            cur = calc(i);
            res = max(res, cur);
        }
        printf("Case #%d: %.9f\n", T, res);
    }

    return 0;
}

