#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#define maxn 1010
#define maxm 1010
using namespace std; 

double f[210][210];
double a[210], b[210];
double best_arr[210];
double best;
int n, m;

double calc(){
	for(int i = 0; i <= m; ++i)
		for(int j = 0; j <= m; ++j) f[i][j] = 0.0;
	f[0][0] = 1.0;
	for(int i = 0; i < m; ++i)
		for(int j = 0; j <= i; ++j) if(f[i][j] > 0){
			f[i+1][j+1] += f[i][j] * b[i+1];
			f[i+1][j] += f[i][j] * (1-b[i+1]);
		}
	return f[m][m/2];
}

void dfs(int k, int now){
	if(k > n){
		if (now == m){
			double tmp = calc();
			if(tmp > best) {
				best = tmp;
				for(int i = 1; i <= m; ++i) best_arr[i] = b[i];
			}
		}
		return;
	}
	dfs(k+1, now);
	b[now+1] = a[k];
	dfs(k+1, now+1);
}

void solve()
{
	cin >> n >> m;
	for(int i = 1; i <= n; ++i) cin >> a[i];
	best = 0.0;
	//dfs(1, 0);
	

	sort(a+1, a+n+1);
	for(int i = 0; i <=m; ++i){
		for(int j = 1; j <= i; ++j) b[j] = a[j];
		for(int j = 1; j <= m-i; ++j) b[i+j] = a[n-j+1];
		double tmp = calc();
		if(tmp > best) best = tmp;
	}
	



	printf("%.10f\n", best);
	//for(int i = 1; i <= n; ++i)printf("%.2f ", a[i]);
	//printf("\n");
	//sort(best_arr+1, best_arr+m+1);
	//for(int i = 1; i <= m; ++i)printf("%.2f ", best_arr[i]);
	//printf("\n");
}

int main() 
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

