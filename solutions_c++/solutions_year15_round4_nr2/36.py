#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-12;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

const int N = 1000;

int n;
double ri[N], ci[N];
double v, x;

bool cmp(const pair<double, double> &a, const pair<double, double> &b) {
    return a.second < b.second;
}

bool go(double t) {
    double least = 0.0, bottom = 0, rest = v;
    for (int i = 0; i < n; ++i) {
        double pick = min(rest, ri[i] * t);
        least += ci[i] * pick;
        bottom += pick;
        rest -= pick;
    }
    if (rest > eps) return false;
    least /= bottom;
    double most = 0.0;
    rest = v;
    bottom = 0.0;
    for (int i = n - 1; i >= 0; --i) {
        double pick = min(rest, ri[i] * t);
        most += ci[i] * pick;
        bottom += pick;
        rest -= pick;
    }
    most /= bottom;
    assert(!isinf(least));
    assert(!isnan(least));
    assert(!isinf(most));
    assert(!isnan(most));
    // cout << "x is " << x << " least is " << least << " most is " << most << " and t is " << t << endl;
    return x + eps > least && x < most + eps;
}

void solve(int test_id) {
    cin >> n >> v >> x;
    vector< pair<double, double> > vd(n);
    REP(i, n) cin >> vd[i].first >> vd[i].second;
    sort(ALL(vd), cmp);
    REP(i, n) {
        ri[i] = vd[i].first;
        ci[i] = vd[i].second;
    }
    cout << "Case #" << test_id << ": ";
    if (x < ci[0] || x > ci[n - 1]) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    double low = 0.0, high = 1e8;
    for (int iter = 0; iter < 100 && fabs(high - low) > eps; ++iter) {
        double mid = (low + high) * 0.5;
        if (go(mid)) {
            high = mid;
        } else {
            low = mid;
        }
    }

    printf("%.12f\n", low);
}

int main() {
    int tests;
    cin >> tests;
    for (int test_id = 1; test_id <= tests; ++test_id) {
        solve(test_id);
    }
    return 0;
}