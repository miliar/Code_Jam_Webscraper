#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<iomanip>
#include<vector>
#include<list>
#include<iterator>
#include<stack>
#include<queue>
using namespace std;

#include<fstream>
FILE *fin=freopen("a.in","r",stdin);
FILE *fout=freopen("a.out","w",stdout);

int T,t,r,c,i,j,g,d[4][2]={0,1,0,-1,1,0,-1,0};
char s[110][110];

int test(int x,int y) {
	int k,ini,xx,yy;
	if (s[x][y]=='.')
	return 0;
	if (s[x][y]=='<')
	ini=1;
	else if (s[x][y]=='v')
	ini=2;
	else if (s[x][y]=='^')
	ini=3;
	else ini=0;
	xx=x+d[ini][0];
	yy=y+d[ini][1];
	while (xx>=0 && xx<r && yy>=0 && yy<c && s[xx][yy]=='.') {
		xx+=d[ini][0];
		yy+=d[ini][1];
	}
	if (xx<0 || xx>=r || yy<0 || yy>=c) {
		for (k=0;k<4;k++)
		if (k!=ini) {
			xx=x+d[k][0];
			yy=y+d[k][1];
			while (xx>=0 && xx<r && yy>=0 && yy<c && s[xx][yy]=='.') {
				xx+=d[k][0];
				yy+=d[k][1];
			}
			if (xx>=0 && xx<r && yy>=0 && yy<c)
			break;
		}
		if (k<4)
		return 1;
		return -999999;
	}
	else return 0;
}

int main() {
	cin>>T;
	for (t=1;t<=T;t++){
		scanf("%d%d",&r,&c);
		for (i=0;i<r;i++)
		scanf("%s",s[i]);
		g=0;
		for (i=0;(i<r && g>=0);i++)
		for (j=0;(j<c && g>=0);j++)
		{
			g+=test(i,j);
		}
		if (g<0)
		printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,g);
	}
    return 0;
}
