#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif
int r,c;
char inp[110][110];
char dir[5] = "^v<>";
int stp[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
int inB (int x, int y) {
	return x>0 && x<=r && y>0 && y<=c;
}
int checkD(int x, int y, char d) {
	rep(k,0,3) {
		if (d == dir[k]) {
			int sx = x + stp[k][0], sy = y + stp[k][1];
			while (inB(sx,sy)) {
				if (inp[sx][sy] != '.') return 1;
				sx += stp[k][0];
				sy += stp[k][1];
			}
		}
	}
	return 0;
}
void lemon() {  
	scanf("%d%d",&r,&c);
	rep(i,1,r) scanf("%s",inp[i]+1);
	int ans = 0;
	int INF = 100000;
	rep(i,1,r) {
		rep(j,1,c) {
			if (inp[i][j] != '.') {
				if (checkD(i,j,inp[i][j])) continue;
				int f = 0;
				rep(k,0,3) if (checkD(i,j,dir[k])) f = 1;
				if (f) ans ++;
				else ans += INF;
			}
		}
	}
	if (ans < INF) printf("%d\n", ans);
	else puts("IMPOSSIBLE");
}
int main() {
  ios::sync_with_stdio(true);
  #ifndef ONLINE_JUDGE
   // freopen("","r",stdin);
  #endif
  int cas;
  scanf("%d",&cas);
  rep(i,1,cas) {
  	printf("Case #%d: ",i);
  	lemon();
  }
  return 0;
}