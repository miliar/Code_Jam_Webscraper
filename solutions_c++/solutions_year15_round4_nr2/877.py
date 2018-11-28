#include <iostream>
#include <iomanip>
#include <vector>           
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <functional>
#include <string>
#include <string.h>  // Include for memset!
#include <complex>
#include <random>
#define _USE_MATH_DEFINES
#include <math.h>

#define INF 2000000000              // 9
#define LLINF 9000000000000000000LL // 18
#define LDINF 1e200

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
typedef vector<bool> vb;
typedef long long ll;
typedef long double ld;

# define EPSILON 1e-10

void ans(long double ans, bool pos, int t) {
	cout << "Case #" << t << ": ";
	if (pos) printf("%.8Lf", ans);
	else cout << "IMPOSSIBLE";
	cout << endl;
}

// Given a monotonically increasing function f, approximately solves f(x) = c,
// assuming that f(l) <= c <= f(h)
long double binary_search(long double l, long double h, long double(*f)(long double), long double c) {
	while (true) {
		long double m = (l + h) / 2, v = f(m);
		if ((abs(v - c) < EPSILON && (h - l < EPSILON)) || (h - l <= 1e-30)) return m;
		if (v < c) l = m;
		else       h = m;
	}
}

vector<long double> R, C;
long double V, X;

long double my_f(long double v) {
	return (v * C[0] + (V - v) * C[1]) / V;
}

#define RES_PHI (2 - ((1.0 + sqrt(5)) / 2.0))

long double gss(long double(*f)(long double), long double leftbound, long double rightbound) {
	long double lb = leftbound, rb = rightbound, mlb = lb + RES_PHI * (rb - lb), mrb = rb + RES_PHI * (lb - rb);
	long double lbv = f(lb), rbv = f(rb), mlbv = f(mlb), mrbv = f(mrb);

	while (rb - lb >= EPSILON) { // || abs(rbv - lbv) >= EPSILON) {
		if (mlbv < mrbv) { // > to maximize
			rb = mrb;  rbv = mrbv;
			mrb = mlb;  mrbv = mlbv;
			mlb = lb + RES_PHI * (rb - lb);
			mlbv = f(mlb);
		}
		else {
			lb = mlb;  lbv = mlbv;
			mlb = mrb;  mlbv = mrbv;
			mrb = rb + RES_PHI * (lb - rb);
			mrbv = f(mrb);
		}
	}
	return mlbv; // any bound should do
}

long double my_f2(long double v) {
	return max(v / R[0], (V - v) / R[1]);
}

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {

		int N;
		cin >> N >> V >> X;

		R.assign(N, 0);
		C.assign(N, 0);
		for (int i = 0; i < N; ++i) cin >> R[i] >> C[i];

		switch (N) {
		case 1:
			if (C[0] == X)
				ans(V / R[0], true, t);
			else ans(0, false, t);
			break;
		case 2:
			if (C[1] > C[0])
			{
				swap(C[1], C[0]);
				swap(R[1], R[0]);
			}
			if (X == C[0] && X == C[1]) {
				long double a = gss(my_f2, 0, V);
				ans(a, true, t);
			}else 
			if ((C[0] <= X + EPSILON && X - EPSILON <= C[1]) || (C[1] <= X + EPSILON && X - EPSILON <= C[0])) {
				long double a = binary_search(0, V, my_f, X);
				if (abs(my_f(a) - X) < EPSILON)
					ans(max(a / R[0], (V - a) / R[1]), true, t);
				else ans(0, false, t);
			}
			else ans(0, false, t);
			break;
		}
	}

	return 0;
}