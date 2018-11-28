#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int nei[110][110][5];
int dir[110][110];
char in[110];
int t, r, c;

inline int gn(int i, int j) {
	return i*c+j;
}

int main() {
	scanf("%d", &t);
	for(int tc=1; tc<=t; tc++) {
		scanf("%d%d", &r, &c);
		memset(nei, 0, sizeof(nei));
		memset(dir, 0, sizeof(dir));
		memset(in, 0, sizeof(in));
		for(int i=1; i<=r; i++) {
			scanf("%s", in+1);
			for(int j=1; j<=c; j++) {
				switch(in[j]) {
					case '^': dir[i][j]=1; break;
					case '>': dir[i][j]=2; break;
					case 'v': dir[i][j]=3; break;
					case '<': dir[i][j]=4; break;
				}
			}
		}
		// up
		for(int j=1; j<=c; j++) {
			int pre = 0;
			for(int i=1; i<=r; i++) {
				if(dir[i][j]) {
					nei[i][j][1] = pre;
					pre = gn(i,j);
				}
			}
		}
		// right
		for(int i=1; i<=r; i++) {
			int pre = 0;
			for(int j=c; j>=1; j--) {
				if(dir[i][j]) {
					nei[i][j][2] = pre;
					pre = gn(i,j);
				}
			}
		}
		// down
		for(int j=1; j<=c; j++) {
			int pre = 0;
			for(int i=r; i>=1; i--) {
				if(dir[i][j]) {
					nei[i][j][3] = pre;
					pre = gn(i,j);
				}
			}
		}
		// left
		for(int i=1; i<=r; i++) {
			int pre = 0;
			for(int j=1; j<=c; j++) {
				if(dir[i][j]) {
					nei[i][j][4] = pre;
					pre = gn(i,j);
				}
			}
		}
		int ans = 0;
		bool pos = true;
		for(int i=1; i<=r; i++) {
			for(int j=1; j<=c; j++) {
				int d = dir[i][j];
				if(d && !nei[i][j][d]) {
					if(nei[i][j][1]+nei[i][j][2]+nei[i][j][3]+nei[i][j][4] == 0)
						pos = false;
					ans ++;
				}
			}
		}
		if(pos) printf("Case #%d: %d\n", tc, ans);
		else printf("Case #%d: IMPOSSIBLE\n", tc);
	}
	return 0;
}