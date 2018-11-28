#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

int n,m;
char s[1000][1000];

bool check(int i,int j,int dx,int dy){
	for (;;){
		i+=dx;
		j+=dy;
		if (i<0||i>=n||j<0||j>=m) return false;
		if (s[i][j]!='.') return true;
	}
}

void getans(){
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++)
		scanf("%s",s[i]);
	bool ok=true;
	int cnt=0;
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			if (s[i][j]!='.'){
				int dx,dy;
				if (s[i][j]=='^') dx=-1,dy=0;
				if (s[i][j]=='>') dx=0,dy=1;
				if (s[i][j]=='v') dx=1,dy=0;
				if (s[i][j]=='<') dx=0,dy=-1;
				// printf("%d %d %d %d\n",i,j,dx,dy);
				if (check(i,j,dx,dy)) continue;
				if (!check(i,j,-1,0)&&!check(i,j,1,0)&&!check(i,j,0,1)&&!check(i,j,0,-1))
					ok=false;
				cnt++;
			}
	if (!ok) printf("IMPOSSIBLE\n");
	else printf("%d\n",cnt);
}

int main(){
	int N;
	scanf("%d",&N);
	for (int r=1;r<=N;r++){
		printf("Case #%d: ",r);
		getans();
	}
	return 0;
}