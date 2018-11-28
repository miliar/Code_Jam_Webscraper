#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int tc;
int n,m,a[205],p[205];
char g[205][205];
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
int lt[]={3,2,1,0},rt[]={1,0,3,2};

int valid(int x,int y,int d) {
	do {
		//printf("%d %d %d\n",x,y,d);
		x = x+dx[d];
		y = y+dy[d];
		if (g[x][y] == '/') d = lt[d];
		else d = rt[d];
	} while (x >= 0 && x < n && y >= 0 && y < m);
	//printf("%d %d %d\n",x,y,d);
	if (x < 0) return y+1;
	if (x == n) return n+m+m-y;
	if (y < 0) return (n+m)*2-x;
	if (y == m) return m+x+1;
}

int main() {
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%d",&n,&m);
		for (int i=0; i<(n+m)*2; i++)
			scanf("%d",&a[i]);
		for (int i=0; i<(n+m)*2; i+=2) {
			p[a[i]] = a[i+1];
			p[a[i+1]] = a[i];
			//printf("%d %d\n",a[i],a[i+1]);
		}

		int val = 1;
		for (int i=0; i<(1<<(n*m)); i++) {
			for (int j=0; j<(n*m); j++)
				if ((1<<j) & i) {
					g[j/m][j%m] = '/';
				}
				else {
					g[j/m][j%m] = '\\';
				}

			val = 1;
			/*
			for (int i=0; i<n; i++) {
				for (int j=0; j<n; j++)
					printf("%c",g[i][j]);
				printf("\n");
			}
			*/
			for (int j=0; j<m; j++) {
				int st = j+1;
				int fin = valid(-1,j,1);
				//printf("%d %d (%d)\n",st,fin,p[st]);
				if (p[st] != fin) val = 0;
			}
			for (int j=0; j<m; j++) {
				int st = n+m+m-j;
				int fin = valid(n,j,3);
				//printf("%d %d (%d)\n",st,fin,p[st]);
				if (p[st] != fin) val = 0;
			}
			for (int j=0; j<n; j++) {
				int st = m+j+1;
				int fin = valid(j,m,2);
				//printf("%d %d (%d)\n",st,fin,p[st]);
				if (p[st] != fin) val = 0;
			}
			for (int j=0; j<n; j++) {
				int st = (n+m)*2-j;
				int fin = valid(j,-1,0);
				//printf("%d %d (%d)\n",st,fin,p[st]);
				if (p[st] != fin) val = 0;
			}

			if (val == 1) break;
		}
		printf("Case #%d:\n",t);
		if (val == 0) {
			printf("IMPOSSIBLE\n",t);
		}
		else {
			for (int i=0; i<n; i++) {
				for (int j=0; j<m; j++)
					printf("%c",g[i][j]);
				printf("\n");
			}
		}
	}
    return 0;
}
