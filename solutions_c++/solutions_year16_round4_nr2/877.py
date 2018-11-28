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

int t, k, n;

double s[205];
Ldouble res[205][205], ans;

int bit_pattern;

void tui_solve(){
	
	ans = 0;
	sort(s+1,s+n+1);
	
	FI(i,0,(1<<n)-1){
		int cnt = 0;
		FI(j,0,n-1) if(i&(1<<j)) cnt++;
		if(cnt != k) continue;
		
		FI(j,0,n) FI(kk,0,n) res[j][kk] = 0;
		
		int p = 0;
		
		res[0][0] = 1.0;
		
		FI(j,0,n-1) if(i&(1<<j)){
			FI(kk,0,p){
				res[p+1][kk] += res[p][kk] * (1 - s[j+1]);
				res[p+1][kk+1] += res[p][kk] * s[j+1];
			}
			p++;
		}
		if(res[k][k/2] > ans){
			ans = res[k][k/2];
			bit_pattern = i;
		}
	}
	printf("%.10lf\n",(double)ans);
	return;
}

void solve(){
	memset(res,0,sizeof(res));
	res[0][0] = 1;
	FI(j,1,n){
		double x = s[j];
		FD(i,k,1) FI(j,0,k){
			res[i][j] = max(res[i][j], res[i-1][j] * (1 - x));
			if(j) res[i][j] = max(res[i][j], res[i-1][j-1] * x);
		}
	}
	printf("%.10lf\n",(double) res[k][k/2]);
	return;
}

int main(){
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bs.out","w",stdout);
	
	scanf("%d",&t);
	FI(i,1,t){
		printf("Case #%d: ",i);
		scanf("%d %d",&n,&k);
		FI(i,1,n) scanf("%lf",&s[i]);
		tui_solve();
		//solve();
	}
	return 0;
}

