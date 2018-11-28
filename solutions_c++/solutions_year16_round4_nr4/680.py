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

int t,n,s[26][26],cost;
char str[29];
bool vis[26][26];

vector<PII> v;

void prep(){
	while(1){
		bool modi = false;
		FI(i,1,n) FI(j,1,n) if(s[i][j]) FI(k,i+1,n) FI(l,1,n){
			if(j != l && s[k][l]){
				if(s[k][j] && (!s[i][l])){
					s[i][l] = true;
					cost++;
					modi = true;
				}
				if(s[i][l] && (!s[k][j])){
					s[k][j] = true;
					cost++;
					modi = true;
				}
			}
		}
		if(!modi) break;
	}
	
	v.clear();
	memset(vis,0,sizeof(vis));
	
	int sumi = 0, sumj = 0;
	
	FI(i,1,n) FI(j,1,n) if(!vis[i][j] && s[i][j]){
		int ci = 0, cj = 0;
		FI(k,1,n) if(s[i][k]) ci++;
		FI(k,1,n) if(s[k][j]) cj++;
		FI(k,1,n) FI(l,1,n) if(s[k][l] && s[i][l]) vis[k][l] = true;
		sumi += ci;
		sumj += cj;
	//	if(ci != cj)
		v.push_back(mp(ci,cj));
	}
	
//	cost += n - max(sumi, sumj);
	
	return;
}

int dp[1111111],sum[1111111];

int sz, wtf;
bool viss[26];

void dfs(int step, int oi, int oj, int osum, int ot){
	if(step == sz && ot + max(oi, oj) <= n){
		wtf = min(wtf, osum + max(oi, oj) * max(oi, oj) + n - ot - max(oi, oj));
		return;
	}
	FI(i,0,sz-1) if(!viss[i]){
		viss[i] = true;
		if(oi == oj){
			dfs(step+1, v[i].fi, v[i].se, osum + oi * oi, ot + oi);
		}else{
			dfs(step+1, oi + v[i].fi, oj + v[i].se, osum, ot);
			dfs(step+1, v[i].fi, v[i].se, osum + max(oi, oj) * max(oi, oj), ot + max(oi, oj));
		}
		viss[i] = false;
	}
	return;
}

void solve(){
	sz = v.size();
	FI(i,0,sz-1) cost -= v[i].fi * v[i].se;
	
	wtf = 99999;
	memset(viss,0,sizeof(viss));
	dfs(0,0,0,0,0);
	
	printf("%d\n", cost + wtf);
	return;
}

int main(){
	
	freopen("D-small-attempt2.in","r",stdin);
	freopen("Ds.out","w",stdout);
	
	scanf("%d",&t);
	FI(i,1,t){
		scanf("%d",&n);
		FI(j,1,n){
			scanf("\n%s",str+1);
			FI(k,1,n) s[j][k] = str[k] - '0';
		}
		printf("Case #%d: ",i);
		cost = 0;
		prep();
		solve();
	}
	return 0;
}
/*o
*/
