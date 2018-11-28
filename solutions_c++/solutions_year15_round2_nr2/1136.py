#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;

int ans[19][19][19];
int r,c,n;

int best;
int mp[16][16];
const int di[4][2]={{-1,0},{1,0},{0,1},{0,-1}};

void check(){
	int cnt=0;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(mp[i][j])
			for(int k=0;k<4;k++){
				int x=i+di[k][0];
				int y=j+di[k][1];
				if(x<0||y<0||x>=r||y>=c) continue;
				if(mp[x][y]) cnt++;
			}
		}
	}
	best=min(best,cnt/2);
}

void dfs(int id,int cnt){
	if(id==r*c){
		if(cnt==n)check();
		return;
	}
	if(r*c-id<n-cnt||cnt>n)return;
	int x=id/c;
	int y=id%c;
	mp[x][y]=1;
	dfs(id+1,cnt+1);
	mp[x][y]=0;
	dfs(id+1,cnt);
}

int main()
{
	memset(ans,0,sizeof(ans));
	for(r=1;r<=16;r++){
		for(c=1;r*c<=16;c++){
			for(n=(r*c+1)/2+1;n<=r*c;n++){
				best=INT_MAX;
				dfs(0,0);
				ans[r][c][n]=best;
			}
		}
	}
	freopen("B-small-attempt0.in","r",stdin);
	freopen("BSMALL.txt","w",stdout);
	int T,Case=1;
	for(scanf("%d",&T);Case<=T;Case++){
		
		scanf("%d%d%d",&r,&c,&n);
		printf("Case #%d: ",Case);
		/*if(n<=(r*c+1)/2){
			puts("0");continue;
		}else{
		}*/
		printf("%d\n",ans[r][c][n]);
	}
    return 0;
}

