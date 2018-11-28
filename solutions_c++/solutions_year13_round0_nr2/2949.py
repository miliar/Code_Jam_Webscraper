#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,m,gp[105][105],r[105],c[105];
bool check() {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(gp[i][j] < c[i]&& gp[i][j] < r[j])
				return false;
		}
	}
	return true;
}
int main () {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++) {
		scanf("%d%d",&n,&m);
		int flag = 0;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				scanf("%d",&gp[i][j]);
				if(gp[i][j] > 100)
					flag = 1;
			}
		}
		printf("Case #%d: ",cas);
		if(flag) puts("NO");
		else {
			for(int i = 0; i < n; i++) {
				c[i] = gp[i][0];
				for(int j = 0; j < m; j++) {
					c[i] = max(c[i],gp[i][j]);
				}
			}
			for(int i = 0; i < m; i++) {
				r[i] = gp[0][i];
				for(int j = 0; j < n; j++) {
					r[i] = max(r[i],gp[j][i]);
				}
			}
			if(check())
				puts("YES");
			else puts("NO");
		}
	}
	return 0;
}