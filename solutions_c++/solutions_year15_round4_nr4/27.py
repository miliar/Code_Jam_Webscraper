#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define fi first
#define se second
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

int _,n,m,a[110][110],r,c;
int ans,__,ret;
bool check(int x,int y) {
	int cnt=0;
	if (x>0) cnt+=(a[x][y]==a[x-1][y]);
	if (x+1<n) cnt+=(a[x][y]==a[x+1][y]);
	cnt+=(a[x][y]==a[x][(y+1)%m]);
	cnt+=(a[x][y]==a[x][(y+m-1)%m]);
	return cnt==a[x][y];
}
void dfs(int x,int y) {
	if (x==n) {
		bool fg=1;
		rep(i,0,m) if (!check(n-1,i)) { fg=0; break;}
		if (fg) {
			ans++;
		}
	} else {
		rep(i,1,5) {
			a[x][y]=i;
			if (x==0||check(x-1,y)) {
				if (y==m-1) dfs(x+1,0); else dfs(x,y+1);
			}
		}
	}
}
int f(int r,int c) {
	n=r,m=c;
	ans=0;
	dfs(0,0);
	return ans;
}
int main() {
	for (scanf("%d",&_);_;_--) {
		scanf("%d%d",&r,&c);
		ret=0;
		rep(i,1,c+1) ret+=f(r,__gcd(i,c));
		printf("Case #%d: %d\n",++__,ret/c);
	}
}
