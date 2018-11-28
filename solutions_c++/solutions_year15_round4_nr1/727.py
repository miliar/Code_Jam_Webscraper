#pragma warning(disable:4996)
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<vector>
using namespace std;
char str[105][105];
int n,m;
int check(int vx,int vy){
	int x=vx,y=vy;
	if(str[x][y]=='.') return 0;
	int vf=0;
	if(str[x][y]=='^'){
		x--;
		while(x>=1){
			if(str[x][y]!='.') vf=1;
			x--;
		}
	}
	if(str[x][y]=='>'){
		y++;
		while(y<=m){
			if(str[x][y]!='.') vf=1;
			y++;
		}
	}
	if(str[x][y]=='<'){
		y--;
		while(y>=1){
			if(str[x][y]!='.') vf=1;
			y--;
		}
	}
	if(str[x][y]=='v'){
		x++;
		while(x<=n){
			if(str[x][y]!='.') vf=1;
			x++;
		}
	}
	if(vf){
		return 0;
	}
	else{
		int kt=0;
		for(int i=1;i<=n;i++){
			if(str[i][vy]!='.') kt++;
		}
		for(int j=1;j<=m;j++){
			if(str[vx][j]!='.') kt++;
		}
		if(kt>2) return 1;
		else return -1;
	}	
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,T,k,st,et,ans,vcase=0,flag;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++){
			scanf("%s",str[i]+1);
		}
		ans=0;flag=0;
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++){
				k=check(i,j);
				if(k==-1) flag=1;
				ans+=k;
			}
		}
		if(flag) printf("Case #%d: IMPOSSIBLE\n",++vcase);
		else printf("Case #%d: %d\n",++vcase,ans);
	}
	return 0;
}
