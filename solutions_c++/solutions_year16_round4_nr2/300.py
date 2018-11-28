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

double p[210];
int n;

double f[210][210];

int bc(int n) {
	int res = 0;
	for (; n; n &= n - 1) ++res;
	return res;
}

double compute(VI v) {
	memset(f, 0, sizeof f);
	f[0][0] = 1;
	int cnt = 0;
	int K = v.size();
	FIR(v.size()) {

		double cp = p[v[i]];
		FORE(j, 0, n) {
			f[i+ 1][j + 1] += cp*f[i][j];
			f[i+ 1][j] += (1 - cp)*f[i][j];
		}

	}

	return f[K][K / 2];

}

double solve() {
	int K;
	GI2(n, K);

	double res = 0;
	FI scanf("%lf", p + i);
	sort(p, p + n);
	

	VI v;

	REPN(start) {
		FORE(len, 1, K) {
			if (start + len > n) break;

			v.resize(0);
			FIR(len) v.push_back(start + i);

			if (start + K <= n) {
				int p = 0;
				while (v.size() < K) {
					v.push_back(n - 1 - p);
					++p;
				}

				res = max(res, compute(v));
				if (res == 1) {
					int b = 0;
				}
				v.resize(len);
			}

			if (K - len <= start) {
				FIR(K - len)
					v.push_back(i);
				res = max(res, compute(v));
				if (res == 1) {
					int b = 0;
				}
			}
		}
	}


	return res;

}


void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		double res = solve();
		
		printf("Case #%d: %.10lf\n", tc, res);
		cerr << tc << endl;
		
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
		bool LARGE = true;

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
