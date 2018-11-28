#include <cstdio>

int T;
int r, c, m;
int e;
char g[55][55];
int ok;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		scanf("%d%d%d", &r, &c, &m);
		e=r*c-m;
		for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='.';
		g[r-1][c-1]='c';
		ok=1;
		if(r==1) {
			for(int i=0; i<m; i++) g[0][i]='*';
		}
		else if(c==1) {
			for(int i=0; i<m; i++) g[i][0]='*';
		}
		else if(r==2) {
			if(e>2 && m%2==0) {
				for(int i=0; i<m/2; i++) g[0][i]=g[1][i]='*';
			}
			else if(e==1) {	
				for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='*';
				g[r-1][c-1]='c';
			}
			else {
				ok=0;
			}
		}
		else if(c==2) {
			if(e>2 && m%2==0) {
				for(int i=0; i<m/2; i++) g[i][0]=g[i][1]='*';
			}
			else if(e==1) {
				for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='*';
				g[r-1][c-1]='c';
			}
			else {
				ok=0;
			}
		}
		else {
			if(e==1) {
				for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='*';
				g[0][0]='c';
			}
			else if(e==4) {
				for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='*';
				g[0][0]='c';
				g[0][1]=g[1][0]=g[1][1]='.';
			}
			else if(e==6) {
				for(int i=0; i<r; i++) for(int j=0; j<c; j++) g[i][j]='*';
				g[0][0]='c';
				g[0][1]=g[0][2]=g[1][0]=g[1][1]=g[1][2]='.';
			}
			else if(e==2 || e==3 || e==5 || e==7) {
				ok=0;
			}
			else {
				int s=0;
				while(m>=r && s+1<c-1) {
					for(int i=0; i<r; i++) g[i][s]='*';
					s++;
					m-=r;
				}
				if(s+1==c-1) {
					int row=0;
					while(m>0) {
						if(m>1) {
							g[row][s]=g[row][s+1]='*';
							m-=2;
						}
						else {
							g[row][s]=g[row][s+1]=g[row+1][s]=g[row+1][s+1]='*';
							g[r-3][s-1]=g[r-2][s-1]=g[r-1][s-1]='.';
							m--;
						}
						row++;
					}
				}
				else {
					if(m<=r-2) {
						for(int i=0; i<m; i++) g[i][s]='*';
					}
					else {
						if(s+2!=c-1) {
							for(int i=0; i<m-1; i++) g[i][s]='*';
							g[0][s+1]='*';
						}
						else {
							for(int i=0; i<m-2; i++) g[i][s]='*';
							g[0][s+1]=g[0][s+2]='*';
						}
					}
				}
			}
		}
		if(ok) {
			printf("Case #%d:\n", q);
			for(int i=0; i<r; i++) {
				for(int j=0; j<c; j++) printf("%c", g[i][j]);
				printf("\n");
			}
		}
		else {
			printf("Case #%d:\nImpossible\n", q);
		}
	}

	return 0;
}
