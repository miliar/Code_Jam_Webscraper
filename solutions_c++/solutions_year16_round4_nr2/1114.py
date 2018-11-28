/*************************************************************\
~*********************ENJOY THE SILENCE***********************~
\*************************************************************/

#include <bits/stdc++.h>
using namespace std;

/*******************Debugging defines*************************/

#define ok_dump() cerr<<"OK\n"
#define var_dump(x) cerr<<#x": "<<x<<'\n'
#define arr_dump(x, n) {cerr<<#x"[]: ";\
	for(int _=1;_<=n;++_) cerr<<x[_]<<" ";cerr<<'\n';}

/*************************************************************/


double P[105][105];
double ProbYes[105];

double Solve(int mask, int n, int k) {

	//cerr << mask << ": ";
	P[0][0] = 1.0;
	int maxx = 0;
	for(int i = 1; i <= n; ++i) {
		if(mask & (1 << (i - 1))) {
			maxx += 1;
			P[i][0] = P[i - 1][0] * (1.0 - ProbYes[i]);
			P[i][maxx] = P[i - 1][maxx - 1] * ProbYes[i];

			for(int j = 1; j < maxx; ++j) {
				P[i][j] = P[i - 1][j] * (1.0 - ProbYes[i]) + P[i - 1][j - 1] * ProbYes[i];
			}
		}

		else {
			for(int j = 0; j <= maxx; ++j)
				P[i][j] = P[i - 1][j];
		}
	}

	assert(maxx == k);

	//cerr << P[n][k / 2] << '\n';
	return P[n][k / 2];
}

int main() {	
	freopen("input.txt", "r", stdin);
	freopen("outputok.txt", "w", stdout);

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int t;
	cin >> t;

	for(int tt = 1; tt <= t; ++tt) {

		int nn, kk;
		cin >> nn >> kk;
		for(int i = 1; i <= nn; ++i)
			cin >> ProbYes[i];

		double best = 0;
		for(int i = 0; i < (1 << nn); ++i) {
			int cnt = 0;
			for(int j = 0; j < nn; ++j)
				if(i & (1 << j)) cnt += 1;
			if(cnt != kk) continue;
			
			best = max(best, Solve(i, nn, kk));
		}

		cout << fixed << setprecision(12) << "Case #" << tt << ": " << best << '\n';
	}
	return 0;
}

/*************************************************************\
~*********************ENJOY THE SILENCE***********************~
\*************************************************************/

