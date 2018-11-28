#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int maze[111][111];
int dx[] = {0,0,1,-1};
int dy[] = {1,-1,0,0};
int n , m ;
bool inmaze(int x,int y) {
	return x >= 0 && x < n && y >= 0 && y < m;
}
bool func() {
	for (int i = 0 ; i < n ; i ++) {
		for (int j = 0 ; j < m ; j ++) {
			int cnt = 0;
			for (int dd = 0; dd < 2 ; dd ++) {
				for (int d = dd*2 ; d < dd*2 + 2 ; d ++) {
					int x = i;
					int y = j;
					while (inmaze(x,y) && maze[x][y] <= maze[i][j]) {
						x += dx[d] , y += dy[d];
					}
					if (inmaze(x,y)) {
				//		cout << i << j << x << y << endl;
						cnt ++;
						break;
					}
				}
			}
			if (cnt == 2) return false;
		}
	}
	return true;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		scanf("%d%d",&n,&m);
		for (int i = 0 ; i < n ; i ++) {
			for (int j = 0 ; j < m ;j ++) {
				scanf("%d",&maze[i][j]);
			}
		}
		cout << "Case #" << cas << ": " << (func() ? "YES" : "NO") << endl;
	}
	return 0;
}