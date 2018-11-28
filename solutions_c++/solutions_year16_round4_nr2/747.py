#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<map>
#include<queue>
#include<iterator>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define CLR(a) memset(a,0,sizeof(a))
#define ll long long
#include<ctime>
#include<cmath>
#include<vector>
#include<iostream>

int tc, n, m, x, y, z, k, w, tt;
double A[205], B[205], dp[205][205], ans;

double MAX(double a, double b) { if (a > b) return a; else return b; }

void update()
{
	FOR(i, 0, 20) FOR(j, 0, 20) dp[i][j] = -1.0;
	dp[0][0] = 1.0;
	
	FOR(i, 0, m)
	{
		FOD(j, i + 1, 1) FOE(k, 0, j) 
		{
			if (k == 0) dp[j][k] = MAX(dp[j][k], dp[j - 1][k] * (1.0 - B[i]));
			else if (k == j) dp[j][k] = MAX(dp[j][k], dp[j - 1][k - 1] * B[i]);
			else dp[j][k] = MAX(dp[j][k], dp[j - 1][k] * (1.0 - B[i]) + dp[j - 1][k - 1] * B[i]);
		}
	}
	
	
	ans = MAX(ans, dp[m][m / 2]);
}

void solve(int x)
{
	if (x == n && w == m) update();
	else if (x != n)
	{
		B[w++] = A[x];
		solve(x + 1);
		w--;
		solve(x + 1);
	}
}

int main ()
{
	scanf("%d", &tc);
	while(tc--)
	{
		scanf("%d %d", &n, &m);
		FOR(i, 0, n) scanf("%lf", &A[i]);
		
		ans = 0.0;
		solve(0);
	
		printf("Case #%d: %.10lf\n", ++tt, ans);
	}
	
	return 0;
}
	
	
