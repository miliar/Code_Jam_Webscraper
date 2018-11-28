#include<cstdio>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<set>
using namespace std;

char tab[60][60],ftab[60][60];
int m,n,xc,yc;

void imprimeTab() {
	for(int i=1;i<=m;i++) {
		for(int j=1; j<=n; j++){
			if(i==xc && j==yc)
				printf("c");		
	    else printf("%c",tab[i][j]);	
		}
		printf("\n");
	}
}

int nextX(int x, int y) {
	if(y==n)
			return x+1;
	return x;
}

int nextY(int x, int y) {
	if(y==n)
			return 1;
	return y+1;
}

int xx[] = {-1,-1,-1,0,0,1,1,1};
int yy[] = {-1,0,1,-1,1,-1,0,1};
int grau(int x, int y) {
	int g=0;
	for(int k=0;k<8;k++)
		if(tab[x+xx[k]][y+yy[k]]=='*')
			g++;
	return g;
}

int flood(int x, int y){
	if(tab[x][y] != '.' || ftab[x][y]) return 0;
	//printf("GRAU %d %d %d\n",x,y,grau(x,y));
	ftab[x][y]=1;
	//printf("CONTANDO x:%d y:%d\n",x,y);
	if(grau(x,y))
		return 1;
	int s=1;
	for(int k=0;k<8;k++)
		s+=flood(x+xx[k], y+yy[k]);
	return s;
}

int click() {
	int ma=0;
	xc=yc=-1;
	for(int i=1; i <=m; i++)
		for(int j=1; j<=n;j++) {
			if(tab[i][j] == '.') {
				memset(ftab,0,sizeof(ftab));
				int x = flood(i,j);
				// printf("FOUND %d %d %d\n",i,j, x);
				if(x>ma) {
					ma = x;
					xc=i;
					yc=j;
				}
			}
		}
	return ma;
}

int CG;
bool back(int x, int y, int b) {
/*	
  printf("%d %d %d\n",x,y,b);
	imprimeTab();
	printf("\n");
	*/
	if(b==0){
		// printf("BASE\n");
		return click() == CG;
	}
	if(x==m+1){
		//printf("LIM\n");
		return false;
	}
	if(back(nextX(x,y), nextY(x,y), b))
		return true;
	if(tab[x][y]=='.'){
		tab[x][y]='*';
		if( back(nextX(x,y), nextY(x,y), b-1))
			return true;
		tab[x][y]='.';
	}
	return false;
}


void fillGreedy( int b) {
	for(int i=1;i<=m;i++)
			for(int j=1;j<=n;j++)
					tab[i][j]='.';
	for(int i=m;b && i>2;i--)
			for(int j=n;b && j>2;j--){
				tab[i][j]='*';
				b--;
			}
	if(b) {
		if(b%2) {
			tab[3][3] = '.';
			b++;
		}
		for(int j=n;j>3 && b;j--){
			tab[1][j] = '*';
			tab[2][j] = '*';
			b-=2;
		}
		for(int i=m; i>3 && b;i--){
			tab[i][1] = '*';
			tab[i][2] = '*';
			b-=2;
		}
	}
	xc=yc=1;
}

char bk[60][60];
int main(){
	int t;
	scanf("%d", &t);
	for(int c=1; c<=t; c++) {
	  printf("Case #%d:\n", c);
		int b;
		scanf("%d %d %d", &m, &n, &b);
		for(int i=0;i<=m+1; i++)
			for(int j=0;j<=n+1;j++)
				tab[i][j]='.';
		if(m ==1){
			for(int j=n;b;j--){
				tab[1][j]='*';
				b--;
			}
			xc=yc=1;
		}else if(n==1){
			for(int i=m;b;i--) {
				tab[i][1]='*';
				b--;
			}
			xc=yc=1;
		} else if(m==2){
			if((b%2 && b< m*n-2)  || b == m*n-2){
				printf("Impossible\n");
				continue;
			}
			for(int j=n;b>=2;j--){
				tab[1][j]=tab[2][j]='*';
				b-=2;
			}
			if(b%2) tab[2][1]='*';
			xc=yc=1;
		} else if(n==2){
			if((b%2 && b< m*n-2)  || b == m*n-2){
				printf("Impossible\n");
				continue;
			}
			for(int i=m;b>=2;i--){
				tab[i][1]=tab[i][2]='*';
				b-=2;
			}
			if(b%2) tab[1][2]='*';
			xc=yc=1;
		} else{
			fillGreedy(max(0,min(b,m*n-9)));
			for(int i=1;i<=m;i++)
				for(int j=1;j<=n;j++)
					bk[i][j]=tab[i][j];
			if(b > m*n-9) {
				int mm =m, nn=n;
				int bb = max(0, b - (m*n-9));
				m=n=3;
				CG = 9 - bb;
				for(int i=0;i<=m+1; i++)
					for(int j=0;j<=n+1;j++)
						tab[i][j]='#';
				for(int i=1;i<=m; i++)
					for(int j=1;j<=n;j++){
						tab[i][j]=bk[i][j];
						if(tab[i][j]=='*')bb--;
					}
				if(back(1,1,bb) && xc!=-1){
					m= mm; n = nn;
					b = m*n-9;
					for(int i=1;i<=m;i++)
							for(int j=1;j<=n;j++)
								if(i>3 || j>3) 
									tab[i][j] = bk[i][j];
				}
				else{
					printf("Impossible\n");
					continue;
				}
			}
		}
		imprimeTab();
	}

	return 0;
}
