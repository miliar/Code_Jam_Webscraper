//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 125

char maze[N][N];
int n, m;
int mm[4][2] = {0, 1, 0, -1, 1, 0, -1, 0};
string dirs("><v^");

bool test(int x, int y, int k) {
	x += mm[k][0], y += mm[k][1];
	while (x >= 0 && x < n && y >= 0 && y < m) {
		if (maze[x][y] != '.') return true;
		x += mm[k][0], y += mm[k][1];
	}
	return false;
}

int solve() {
	int ans = 0;
	Rep(i, n) Rep(j, m) {
		if (maze[i][j] == '.') continue;
		if (test(i, j, dirs.find(maze[i][j]))) continue;
		bool flag = false;
		Rep(k, 4) 
			if (test(i, j, k)) {
				flag = true;
				ans++;
				break;
			}
		if (!flag) return -1;
	}
	return ans;
}
int		main(){
	int cas, tt = 0;
	scanf("%d", &cas);
	while (cas --) {
		scanf("%d%d", &n, &m);
		Rep(i, n) scanf("%s", maze[i]);
		int ans = solve();
		printf("Case #%d: ", ++tt);
		if (ans == -1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
	return 0;
}
