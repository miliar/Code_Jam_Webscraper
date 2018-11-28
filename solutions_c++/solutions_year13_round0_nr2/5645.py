#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
//#include <map>
#include <algorithm>
using namespace std;
int n,m;
int map[110][110];
int dy[4]={0,0,1,-1},dx[4]={-1,1,0,0};
bool in(int y,int x) {
	return (y>=0&&y<n&&x>=0&&x<m);
}
bool check(int i,int j) {
	int k,x,y;
	bool flag1=true,flag2=true;
	for(k=0;k<2;k++) {
		y=i+dy[k],x=j+dx[k];
		while (in(y,x)) {
			if (map[y][x]>map[i][j]) {flag1=false;break;}
			y+=dy[k],x+=dx[k];
		}
		if (in(y,x)) break;
	}
	for(k=2;k<4;k++) {
		y=i+dy[k],x=j+dx[k];
		while (in(y,x)) {
			if (map[y][x]>map[i][j]) {flag2=false;break;}
			y+=dy[k],x+=dx[k];
		}
		if (in(y,x)) break;
	}
	return (flag1||flag2);
}
int main() {
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int I,T;
	for (cin >> T,I=1;I<=T;I++) {
		int i,j;
		cin >> n >> m;
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				scanf("%d",&map[i][j]);
		for (i=0;i<n;i++) {
			for (j=0;j<m;j++) {
				if (check(i,j)==false) break;
			}
			if (j<m) break;
		}
		printf("Case #%d: ",I);
		if (i<n) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
