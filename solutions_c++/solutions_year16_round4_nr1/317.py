#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string ans,f[3][20];
bool flag;
int n,t,T,p,r,s;

bool judge(int u) {
	int p_ = 0, r_ = 0,s_ = 0;
	for (int i = 0; i < (int)f[u][n].length(); i++) {
		if (f[u][n][i] == 'R') r_++;
		else if (f[u][n][i] == 'P') p_++;
		else s_++;
	}
	if (r_ != r || p_ != p || s_ != s) return false;
	if (flag) {
		if (f[u][n] < ans) ans = f[u][n];
	}
	else ans = f[u][n];
	return true;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	f[0][0] = "R"; f[1][0] = "P"; f[2][0] = "S";
	for (int j = 1; j <= 12; j++) {
		// R S
		if (f[0][j - 1] < f[2][j - 1])
			f[0][j] = f[0][j - 1] + f[2][j - 1];
		else f[0][j] = f[2][j - 1] + f[0][j - 1];
		// P R
		if (f[1][j - 1] < f[0][j - 1])
			f[1][j] = f[1][j - 1] + f[0][j - 1];
		else f[1][j] = f[0][j - 1] + f[1][j - 1];
		// S p
		if (f[2][j - 1] < f[1][j - 1])
			f[2][j] = f[2][j - 1] + f[1][j - 1];
		else f[2][j] = f[1][j - 1] + f[2][j - 1];		
	}
	for (scanf("%d",&T), t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d %d %d %d",&n,&r,&p,&s);
		flag = false; ans = "";
		for (int i = 0; i < 3; i++) flag |= judge(i);
		if (flag) cout << ans << endl;
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

