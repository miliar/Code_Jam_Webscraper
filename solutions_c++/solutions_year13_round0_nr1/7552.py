#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<algorithm>
#define tar(i,n) for(int i=1;i<=n;++i)
#define rep(i,n) for(int i=0;i<n;++i)
using namespace std;
inline void upmin(int &x,int b){if(b<x)x=b;}
inline void upmax(int &x,int b){if(b>x)x=b;}

char c[4][4];
char e[4][4];

int main(){
	freopen("tttt.in","r",stdin);
	freopen("tttt.out","w",stdout);
	int n;
	scanf("%d\n",&n);
	tar(x,n){
		rep(i,4){
			rep(j,4)scanf("%c",&c[i][j]);
			scanf("\n");
		}
		scanf("\n");

		int flagO,flagX,emp;
		flagO=flagX=emp=false;
		rep(i,4)rep(j,4)if(c[i][j]=='.')emp=true;
		rep(i,4)rep(j,4)e[i][j]=c[i][j];
		rep(i,4)rep(j,4)if(e[i][j]=='T')c[i][j]='O';
		rep(i,4)if(c[i][0]=='O' && c[i][1]=='O' && c[i][2]=='O' && c[i][3]=='O')flagO=true;
		rep(i,4)if(c[0][i]=='O' && c[1][i]=='O' && c[2][i]=='O' && c[3][i]=='O')flagO=true;
		if(c[0][0]=='O' && c[1][1]=='O' && c[2][2]=='O' && c[3][3]=='O')flagO=true;
		if(c[3][0]=='O' && c[2][1]=='O' && c[1][2]=='O' && c[0][3]=='O')flagO=true;

		rep(i,4)rep(j,4)if(e[i][j]=='T')c[i][j]='X';
		rep(i,4)if(c[i][0]=='X' && c[i][1]=='X' && c[i][2]=='X' && c[i][3]=='X')flagX=true;
		rep(i,4)if(c[0][i]=='X' && c[1][i]=='X' && c[2][i]=='X' && c[3][i]=='X')flagX=true;
		if(c[0][0]=='X' && c[1][1]=='X' && c[2][2]=='X' && c[3][3]=='X')flagX=true;
		if(c[3][0]=='X' && c[2][1]=='X' && c[1][2]=='X' && c[0][3]=='X')flagX=true;
		printf("Case #%d: ",x);
		if(flagO && flagX)printf("Draw");else
		if(flagO)printf("O won");else
		if(flagX)printf("X won");else
		if(emp)printf("Game has not completed");else
			printf("Draw");
		
		printf("\n");
	}
	return 0;
}
