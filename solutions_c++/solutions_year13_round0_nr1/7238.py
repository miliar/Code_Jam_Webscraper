#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
char A[5][5];
int t;
bool x,o,c;
void read()
{
	int i,j;
	c=1;
	x=o=0;
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
		{
			scanf(" %c",&A[i][j]);
			if(A[i][j]=='.') c=0;
		}
}
void control(char a,char b,char c,char d,char v)
{
	if(a!=v && a!='T') return; 
	if(b!=v && b!='T') return;
	if(c!=v && c!='T') return;
	if(d!=v && d!='T') return;
	if(v=='X') x=1;
	else o=1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("cikti.txt","w",stdout);
	int i,j;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		read();
		for(j=1;j<=4;j++)
		{
			control(A[j][1],A[j][2],A[j][3],A[j][4],'X');
			control(A[1][j],A[2][j],A[3][j],A[4][j],'X');
			control(A[j][1],A[j][2],A[j][3],A[j][4],'O');
			control(A[1][j],A[2][j],A[3][j],A[4][j],'O');
		}
		control(A[1][1],A[2][2],A[3][3],A[4][4],'X');
		control(A[1][4],A[2][3],A[3][2],A[4][1],'X');
		control(A[1][1],A[2][2],A[3][3],A[4][4],'O');
		control(A[1][4],A[2][3],A[3][2],A[4][1],'O');
		printf("Case #%d: ",i);
		if(c==1 && !x && !o) printf("Draw\n");
		else if(!c && !x && !o) printf("Game has not completed\n");
		else if(x) printf("X won\n");
		else printf("O won\n");
	}
	getchar(); getchar();
	return 0;
}
