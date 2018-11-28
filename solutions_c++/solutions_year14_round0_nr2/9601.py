#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <iomanip>

using namespace std;

#define VI vector<int>
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

const double EPS = 10e-13;

double rec(const double C, const double F, const double X, double cur, double pace,
	   double limit) {
    if(cur >= X) return 0.0;

    double t1 = (X - cur) / (double) pace;

    if(limit <= 0) return t1;
    double r = (C - cur) / pace;

    limit = min(t1, limit - r);
    double t0 = rec(C, F, X, r * pace + cur - C, pace + F, limit) + r;

    return min(t0,t1);
}

void algo(int tc) {
    double C,F,X; cin >> C >> F >> X;
    cout << fixed;
    cout << "Case #" << tc << ": " << setprecision(7) << rec(C, F, X, 0.0, 2.0, X/2.0) << "\n";
}


int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);

    int TC; cin >> TC;
    for(int t = 1; t <= TC; ++t) algo(t);

    return 0;
}
