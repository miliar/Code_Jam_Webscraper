#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

void solve(int);

int main () {

	ios::sync_with_stdio(false);
	
	int test_num;
	cin >> test_num;
	for (int case_id = 1;case_id <= test_num;case_id++) {
		solve(case_id);
	}

	return 0;
}

const int N = 210;

double A[N];
double dp[N][2*N];

void solve ( int case_id ) {

	int n, k;

	cin >> n >> k;
	for ( int i = 0;i < n;i++) {
		cin >> A[i];
	}

	sort(A, A+n);

	double ans = 0.0;
	int p = 0;
	for (int o = 0;o <= k;o++) {
		int x = 0;
		for ( int i = 0;i < n;i++) {
			if ( i < o or i >= n-k+o) {
				x |= 1 << i;
			}
		}
		vector<int> idx;
		for ( int j = 0;j < n;j++) {
			if( (x >> j) & 1 ){
				idx.push_back(j);
			}
		}
		if(idx.size() != k) continue;
		for(int i = 0;i < k;i++) {
			for ( int j = 0 ;j <= 2*n;j++) {
				if ( i == 0 ) {
					if ( j == n+1 ) {
						dp[i][j] = A[idx[i]];
					} else if (j == n-1) {
						dp[i][j] = 1.0 - A[idx[i]];
					} else {
						dp[i][j] = 0.0;
					}
				} else {
					dp[i][j] = 0;
					dp[i][j] += (j > 0 ? dp[i-1][j-1] * A[idx[i]] : 0.0);
					dp[i][j] += (j < 2*n ? dp[i-1][j+1] * (1-A[idx[i]]) : 0.0);
				}
			}
		}
		if (dp[k-1][n] > ans) {
			ans = dp[k-1][n];
			p = x;
		}
	}

	printf("Case #%d: %.8lf\n", case_id, ans);
}