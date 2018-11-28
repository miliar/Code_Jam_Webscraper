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

int _,n,m,__;
char s[110][110];
void solve() {
	int ans=0;
	rep(i,0,n) rep(j,0,m) if (s[i][j]!='.') {
		bool ar=0;
		rep(c,0,m) if (c!=j&&s[i][c]!='.') ar=1;
		rep(c,0,n) if (c!=i&&s[c][j]!='.') ar=1;
		if (!ar) { puts("IMPOSSIBLE"); return;}
		if (s[i][j]=='<') {
			bool fd=0;
			rep(c,0,j) if (s[i][c]!='.') fd=1;
			if (!fd) ans++;
		}
		if (s[i][j]=='>') {
			bool fd=0;
			rep(c,j+1,m) if (s[i][c]!='.') fd=1;
			if (!fd) ans++;
		}
		if (s[i][j]=='^') {
			bool fd=0;
			rep(c,0,i) if (s[c][j]!='.') fd=1;
			if (!fd) ans++;
		}
		if (s[i][j]=='v') {
			bool fd=0;
			rep(c,i+1,n) if (s[c][j]!='.') fd=1;
			if (!fd) ans++;
		}
	}
	printf("%d\n",ans);
} 
int main() {
	for (scanf("%d",&_);_;_--) {
		scanf("%d%d",&n,&m);
		rep(i,0,n) scanf("%s",s[i]);
		printf("Case #%d: ",++__);
		solve();
	}
}
