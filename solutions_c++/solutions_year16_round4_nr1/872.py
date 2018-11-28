#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

int dp[13][3][3];
PII pv[13][3][3][2];

map<int,int> M;
int p;

int t, n, a, b, c, tar;

void gen(int aa, int bb, int cc){
	if(aa == 0){
		if(bb == 0) printf("P");
		if(bb == 1) printf("R");
		if(bb == 2) printf("S");
		return;
	}
	PII lt = pv[aa][bb][cc][0];
	PII rt = pv[aa][bb][cc][1];
	gen(aa-1, lt.fi, lt.se);
	gen(aa-1, rt.fi, rt.se);
	return;
}

void solve(){
	if(max(max(a,b),c) - min(min(a,b),c) > 1){
		printf("IMPOSSIBLE\n");
		return;
	}
	if(a != b && a != c) tar = 0;
	if(b != a && b != c) tar = 1;
	if(c != a && c != b) tar = 2;
	int t2 = 0;
	if(dp[n][tar][1] != -1 && (dp[n][tar][t2] == -1 || dp[n][tar][1] < dp[n][tar][t2])) t2 = 1;
	if(dp[n][tar][2] != -1 && (dp[n][tar][t2] == -1 || dp[n][tar][2] < dp[n][tar][t2])) t2 = 2;
	gen(n, tar, t2);
	printf("\n");
	return;
}
int main(){
	memset(dp,-1,sizeof(dp));
	dp[0][0][0] = 0;
	dp[0][1][1] = 1;
	dp[0][2][2] = 2;
	p = 3;
	FI(i,1,12){
		M.clear();
		FI(j,0,2) FI(k,0,2){
		//dp[i][j][k] = ?
			dp[i][j][k] = 999999999;
			FI(l,0,2) FI(m,0,2) FI(n,0,2) FI(o,0,2){
				if(l==m || l==j || m==j) continue;
				if(n==o) continue;
				if(dp[i-1][l][n] == -1 || dp[i-1][m][o] == -1) continue;
				if((n == k && o == (k+1)%3) || (n == (k+1)%3 && o == k)){
					if(dp[i-1][l][n] * p + dp[i-1][m][o] < dp[i][j][k]){
						dp[i][j][k] = dp[i-1][l][n] * p + dp[i-1][m][o];
						pv[i][j][k][0] = mp(l, n);
						pv[i][j][k][1] = mp(m, o);
					}
				}
			}
		}
		FI(j,0,2) FI(k,0,2) if(dp[i][j][k] != -1) M[dp[i][j][k]] = true;
		p = 0;
		for(map<int,int>::iterator it = M.begin();it!=M.end();it++){
			M[(*it).fi] = p++;
		}
		FI(j,0,2) FI(k,0,2) if(dp[i][j][k] != -1) dp[i][j][k] = M[dp[i][j][k]];
	}
	
	freopen("A-large.in","r",stdin);
	freopen("Al.out","w",stdout);
	
	scanf("%d",&t);
	FI(i,1,t){
		printf("Case #%d: ",i);
		scanf("%d %d %d %d",&n,&a,&b,&c);
		swap(a,b);
		solve();
	}
	return 0;
}
