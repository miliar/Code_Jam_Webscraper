#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<cstdio>
#include<cstring>
#include<string>
#include<cctype>
#include<cstdlib>
#include<algorithm>
#include<bitset>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<sstream>
#include<fstream>
#include<iomanip>
#include<ctime>
#include<complex>
#include<functional>
#include<climits>
#include<cassert>
#include<iterator>
#include<unordered_map>
using namespace std;


int t;

#define M 20
long double dp[M][M];  //choose yes 
long double pas[M][M];

double a[M];

int T;
vector<double> A;
int n, k1;
double solve(){
	for (int i = 0; i <= A.size(); i++){
		for (int j = 0; j <= A.size(); j++){
			dp[i][j] = 0;
		}
	}
	dp[0][0] = 1.0;
	for (int i = 0; i < A.size(); i++){
		for (int j = 0; j <= A.size(); j++){
			if (dp[i][j] != 0.0){
				dp[i + 1][j + 1] += dp[i][j] * A[i];
				dp[i + 1][j] += dp[i][j] * (1.0 - A[i]);
			}
		}
	}
	return dp[A.size()][k1 / 2];
}
int main(){
	pas[0][0] = 1;
	for (int i = 0; i + 1 < M; i++){
		for (int j = 0; j <= i; j++){
			pas[i + 1][j] += pas[i][j];
			pas[i + 1][j + 1] += pas[i][j];
		}
	}
	cin >> t;
	while (t--){
		T++;
		scanf("%d%d", &n, &k1);
		printf("Case #%d: ", T);
		for (int i = 0; i < n; i++){
			scanf("%lf", &a[i]);
		}
		double ans = 0;
		for (int i = 0; i < (1 << n); i++){
			int cnt = 0;
			for (int j = 0; j < n; j++){
				cnt += (int)((i >> j) & 1);
			}
			if (cnt == k1){
				A.clear();
				for (int j = 0; j < n; j++){
					if ((i >> j) & 1){
						A.push_back(a[j]);
					}
				}
				ans = max(ans, solve());
			}
		}
		printf("%.16f\n", ans);
	}
	return 0;
}