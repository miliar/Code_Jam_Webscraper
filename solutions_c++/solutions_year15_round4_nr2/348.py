#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

double R[110], C[110];
double V, X;

bool eq(double x, double y) {
	return fabs(x - y) < 1e-12;
}

double solve() {
	int n;
	cin >> n >> V >> X;

	FI cin >> R[i] >> C[i];

	if (n == 1) {
		if (eq(X, C[0]))
			return V / R[0];
		return -7;
	}

	if (eq(C[0], C[1])) {
		if (eq(X, C[0]))
			return V / (R[0] + R[1]);
		return -7;
	}

	double v0 = V*(X - C[1]) / (C[0] - C[1]);
	if (v0 < 0 || v0 > V + 1e-12)
		return -7;

	return max(v0 / R[0], (V - v0) / R[1]);
		
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		double res = solve();
		if (res > -1)
			printf("Case #%d: %.10lf\n", tc, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'B';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 0;
		bool LARGE = false;

		if (LARGE) {
			sprintf(in_file, "%c-large.in", TASK);
			sprintf(out_file, "%c-large.out", TASK);
		} else {
			sprintf(in_file, "%c-small-attempt%d.in", TASK,  ATTEMPT);
			sprintf(out_file, "%c-small-attempt%d.out", TASK,  ATTEMPT);
		}

		cerr << in_file <<  endl; freopen(in_file, "rt", stdin);
		cerr << out_file << endl; freopen(out_file, "w", stdout);
	}
}
