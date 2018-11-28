#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#define MAX_N 200

// (x,y) choose x person, prob that y say yes
double p[MAX_N+1][MAX_N+1];

int N, K;
double P[MAX_N];

void dump()
{
	for (int x=0;x<=N;++x) {
		for (int y=0;y<=N;++y) {
			printf("%.3f ", p[x][y]);
		}
		printf("\n");
	}
	printf("=======\n");
}


double dp[17];

double calc(int set)
{
	int cnt = 0;
	
	for (int i=0;i<=16;++i) dp[i] = 0;
	dp[0] = 1;
	
	for (int i=0;i<N;++i) {
		if (set & (1<<i)){
			++cnt;
			double pp = P[i];
			for (int j=16;j>=0;--j) {
				if (j == 0)
					dp[j] = dp[j] * (1-pp);
				else
					dp[j] = dp[j] * (1-pp) + dp[j-1] * pp;
			}
		}
	}
	if (cnt != K) return -1;
	return dp[K/2];
}

double solv()
{
	double ans = 0;
//	for (int i=0;i<=MAX_N;++i) for (int j=0;j<=MAX_N;++j) p[i][j] = 0;
	p[0][0] = 1.0;
	
	for (int i=0;i<(1<<N);++i) {
		double tmp = calc(i);
		if (tmp > ans) ans = tmp;
	}
	return ans;

	
/*	
	for (int i=0;i<N;++i) {
		double pp = P[i];
		
		for (int x=i+1;x>0;x--) {
			for (int y=0;y<=N;++y) {
				double newp = 0;
				if (y == 0)
					newp = p[x-1][y] * (1-pp);
				else 
					newp = p[x-1][y-1] * pp + p[x-1][y] * (1-pp);

				if (newp > p[x][y])
					p[x][y] = newp;
			}
		}
		dump();
	}

	return p[K][K/2];
*/
}

int main()
{
	int T;
	cin >> T;
	for (int nCase = 1; nCase <= T; ++nCase) {
		cin >> N >> K;
		for (int i=0;i<N;++i) cin >> P[i];
		printf("Case #%d: %.7f\n", nCase, solv());
	}
	return 0;
}
