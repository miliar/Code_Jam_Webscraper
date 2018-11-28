#include <bits/stdc++.h>
using namespace std;
typedef long double lf;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;
typedef pair<ll, ll> pll;
#define pb push_back
#define SZ(x) ((int)(x).size())
inline int ri() {
	int x=0, f=1, c=getchar();
	for(; c<48||c>57; f=c=='-'?-1:f, c=getchar());
	for(; c>47&&c<58; x=x*10+c-48, c=getchar());
	return x*f;
}
const int N=10;
int ans, n, b[N][N], a[N][N], tot, ps[N];
bool vis[N], flag, vis2[N];
char s[N][N];
bool dfs2(int x) {
	if(x==n) {
		return 1;
	}
	bool ok=0;
	int id=ps[x];
	for(int i=0; i<n; ++i) {
		if(!vis2[i] && b[id][i]) {
			vis2[i]=1;
			if(!dfs2(x+1)) {
				vis2[i]=0;
				return 0;
			}
			ok=1;
			vis2[i]=0;
		}
	}
	return ok;
}
bool check1() {
	return dfs2(0);
}
bool dfs1(int x) {
	if(x==n) {
		if(!check1()) {
			return 0;
		}
	}
	for(int i=0; i<n; ++i) {
		if(!vis[i]) {
			vis[i]=1;
			ps[x]=i;
			if(!dfs1(x+1)) {
				vis[i]=0;
				return 0;
			}
			vis[i]=0;
		}
	}
	return 1;
}
bool check() {
	return dfs1(0);
}
void dfs(int x, int y) {
	if(x==n) {
		if(check()) {
			/*
			for(int i=0; i<n; ++i) {
				for(int j=0; j<n; ++j) {
					printf("%d%c", b[i][j], " \n"[j==n-1]);
				}
			}
			printf("tot:%d\n", tot);
			*/
			ans=min(ans, tot);
		}
		return;
	}
	if(a[x][y]) {
		b[x][y]=1;
		dfs((y==n-1)?x+1:x, (y==n-1)?0:(y+1));
	}
	else {
		b[x][y]=1;
		++tot;
		dfs((y==n-1)?x+1:x, (y==n-1)?0:(y+1));
		--tot;
		b[x][y]=0;
		dfs((y==n-1)?x+1:x, (y==n-1)?0:(y+1));
	}
}
int main() {
	for(int _=1, T=ri(); _<=T; ++_) {
		printf("Case #%d: ", _);
		// puts("");
		n=ri();
		for(int i=0; i<n; ++i) {
			scanf("%s", s[i]);
			for(int j=0; j<n; ++j) {
				if(s[i][j]=='1') {
					a[i][j]=1;
				}
				else {
					a[i][j]=0;
				}
			}
		}
		ans=~0u>>1;
		dfs(0, 0);
		printf("%d\n", ans);
	}
	return 0;
}
