#include <cassert>
#include <cstdlib>
#include <cstdio>

#include <functional>
#include <iostream>
#include <algorithm>
#include <valarray>
#include <iterator>
#include <complex>
#include <numeric>
#include <utility>
#include <bitset>
#include <limits>
#include <memory>
#include <random>
#include <string>
#include <tuple>
#include <new>

#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <deque>
#include <array>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>

#define DEBUG(...) fprintf(stderr, __VA_ARGS__)
#define ALL(c) begin(c), end(c)
#define SIZE(c) (int)(c).size()

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());



constexpr int ITER = 1000;
constexpr long double eps = std::numeric_limits<double>::epsilon();

void solve(int test) {
	int n;
	scanf("%d", &n);
	long double V, X;
	vector<long double> R(n);
	vector<long double> C(n);
	scanf("%Lf%Lf", &V, &X);
	int ht = 1;
	int fr = 1;
	for (int i = 0; i < n; i++) {
		scanf("%Lf%Lf", &R[i], &C[i]);
		ht &= C[i] > X + eps;
		fr &= C[i] < X - eps;
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			if (C[i] < C[j]) {
				swap(C[i], C[j]);
				swap(R[i], R[j]);
			}
	for (int i = 0; i + 1 < n; i++) assert(C[i] <= C[i + 1]);
	if (fr || ht) {
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}
	double left = 0.;
	double right = 1e10;
	for (int iter = 0; iter < ITER; iter++) {
		auto ave = (left + right) / 2.;
		int ok = 1;
		long double tV = 0.;
		long double tC = 0.;
		for (int i = 0; i < n; i++) {
			long double aV = min(ave * R[i], V - tV);
			long double nV = tV  + aV;
			long double nC = (tC * tV + aV * C[i]) / nV;
			tV = nV;
			tC = nC;
		}
		ok &= tV >= V - eps;
		ok &= tC <= X + eps;
	 	tV = 0.;
		tC = 0.;
		for (int i = n - 1; i >= 0; i--) {
			long double aV = min(ave * R[i], V - tV);
			long double nV = tV  + aV;
			long double nC = (tC * tV + aV * C[i]) / nV;
			tV = nV;
			tC = nC;
		}
		ok &= tV >= V - eps;
		ok &= tC >= X - eps;
		if (ok) {
			right = ave;
		} else {
			left = ave;
		}
	}
	auto res = (left + right) / 2;
	printf("Case #%d: %.20e\n", test, (double)res);
}

int main () {
 	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) solve(test);
}
