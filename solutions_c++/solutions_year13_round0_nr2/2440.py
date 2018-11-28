#include<cstdio>

int main () {
	int ncase, n, m;
	scanf("%d", &ncase);
	int map[100][100];
	for(int c=1; c<=ncase; c++) {
		printf("Case #%d: ", c);
		scanf("%d %d", &n, &m);
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				scanf("%d", &map[i][j]);
		int stat[100][100]={0};
		int hor[100]={0}, ver[100]={0};
		bool horpos[100]={0}, verpos[100]={0};
		bool possible = true;
		if(n>1 && m>1) {
			int m1 = m-1, n1=n-1;
			/*puts("");
			for(int i=0; i<n; i++,puts(""))
				for(int j=0; j<m; j++)
					printf("%d ",map[i][j]);
				*/	
			for(int i=0; i<n; i++)
				for(int j=0; j<m; j++)
					if(hor[i] < map[i][j])
						hor[i] = map[i][j];
			for(int j=0; j<m; j++)
				for(int i=0; i<n; i++)
					if(ver[j] < map[i][j])
						ver[j] = map[i][j];
			for(int i=0; i<n; i++) {
				horpos[i] = true;
				for(int j=1; j<m; j++)
					if(map[i][j]!=map[i][0]) {
						horpos[i] = false;
						break;
					}
			}
			for(int j=0; j<m; j++) {
				verpos[j] = true;
				for(int i=1; i<n; i++)
					if(map[i][j]!=map[0][j]) {
						verpos[j] = false;
						break;
					}
			}/*
			printf("Hor : ");
			for(int i=0; i<n; i++)
				printf("%d ", horpos[i]); puts("");
			printf("Ver : ");
			for(int i=0; i<m; i++)
				printf("%d ", verpos[i]); puts("");
				*/
			for(int i=0; i<n; i++)
				for(int j=0; j<m; j++) {
					if(map[i][j] == hor[i] || horpos[i])
						stat[i][j] |= 1;
					if(map[i][j] == ver[j] || verpos[j])
						stat[i][j] |= 2;
				}
			/*puts("");
			for(int i=0; i<n; i++,puts(""))
				for(int j=0; j<m; j++)
					printf("%d%d ",stat[i][j]&1, (stat[i][j]&2)>0);
*/
			for(int i=0; i<n && possible; i++)
				for(int j=0; j<m; j++)
					if(!stat[i][j]) {
						possible=false;
						break;
					}
		}
	
		puts(possible ? "YES" : "NO");
	}
	return 0;
}
