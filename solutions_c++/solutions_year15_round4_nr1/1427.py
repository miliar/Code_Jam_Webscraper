#include <bits/stdc++.h>
using namespace std;
#define fo(i,n) for(int i=0;i<(n);i++)
#define rfo(i,n) for(int i=n;i--;)
#define ff(i,s,e) for(int i=(s);i<=(e);i++)
#define mx(a,b) a=max(a,b)
#define mn(a,b) a=min(a,b)

int T, ans;
//var
int R, C;
char g[105][105];
bool to[105][105][4];
int cnt[105][105];
bool rip;
//end var

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d\n", &T);
	ff(_, 1, T) {
		ans = 0;
		rip = 0;
		//code
		scanf("%d %d\n", &R, &C);
		fo(r, R) scanf("%s\n", g[r]);
		//end code
		fo(r, R) fo(c, C) cnt[r][c] = 0;
		fo(r, R) {
			int last = -1;
			fo(c, C) {
				to[r][c][3] = (last != -1);
				if(last == -1) cnt[r][c]++;
				if(g[r][c] != '.') last = c; 
			}
			last = -1;
			rfo(c, C) {
				to[r][c][1] = (last != -1);
				if(last == -1) cnt[r][c]++;
				if(g[r][c] != '.') last = c; 
			}
		}
		fo(c, C) {
			int last = -1;
			fo(r, R) {
				to[r][c][0] = (last != -1);
				if(last == -1) cnt[r][c]++;
				if(g[r][c] != '.') last = c; 
			}
			last = -1;
			rfo(r, R) {
				to[r][c][2] = (last != -1);
				if(last == -1) cnt[r][c]++;
				if(g[r][c] != '.') last = c; 
			}
		}
		fo(r, R) fo(c, C) if(g[r][c] != '.') {
			if(cnt[r][c] == 4) rip = 1; 
			int dir = 0;
			if(g[r][c] == '^') dir = 0;
			if(g[r][c] == '>') dir = 1;
			if(g[r][c] == 'v') dir = 2;
			if(g[r][c] == '<') dir = 3;
			if(!to[r][c][dir]) ans++;
		}
		if(rip) 
			printf("Case #%d: IMPOSSIBLE\n", _);
		else
			printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}
