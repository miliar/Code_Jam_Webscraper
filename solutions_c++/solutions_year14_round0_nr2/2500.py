#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

#define clr(a, x)  memset(a, x, sizeof(a))
#define REP(i, n)  for(int i = 0; i < (n); i++)
#define DEBUG

typedef long long LL;

void solve() {
	int T;
	double C, F, X;
	cin >> T;
	REP(Case, T) {
		cin >> C >> F >> X;
		double ans = X / 2;
		double s = 0.0, v = 2.0;
		while(s < ans) {
			double tmp = s + X / v;
			ans = min(tmp, ans);
			s += C / v;
			v += F;
		}
		printf("Case #%d: %.8f\n", Case+1, ans);
	}
}

int main() {
#ifdef DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	solve();
#ifdef DEBUG
	fclose(stdin);
	fclose(stdout);
#endif
	return  0;
}













