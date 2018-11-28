#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int dx[]={1,0,-1,0},dy[]={0,1,0,-1};
int n,m;
char bd[150][150];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%d",&n,&m);
		for (int i=0; i<n; i++)
			scanf("%s",bd[i]);
		int imp = 0,ret = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (bd[i][j] != '.') {
					int fail = 0;
					for (int d=0; d<4; d++) {
						int x=i+dx[d],y=j+dy[d];
						int ok = 0;
						while (x >= 0 && x < n && y >= 0 && y < m) {
							if (bd[x][y] != '.') { ok = 1; break; }
							x += dx[d]; y += dy[d];

						}
						if (ok == 0) {
							if (bd[i][j] == '<' && d == 3) ret++;
							if (bd[i][j] == '^' && d == 2) ret++;
							if (bd[i][j] == 'v' && d == 0) ret++;
							if (bd[i][j] == '>' && d == 1) ret++;
							fail++;
						}
					}
					if (fail == 4) { imp = 1; }
				}
			}
		}
		if (imp) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,ret);
	}
    return 0;
}
