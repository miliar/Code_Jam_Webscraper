#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#define maxl 1000000000
using namespace std;

int n,m;
int a[110][110];
bool dc[110],dr[110];

bool checkrow(int r,int x){
	int i;
	for(i=1;i<=m;++i)if(a[r][i]!=x)return false;	
	return true;
}

bool checkcol(int c,int x){
	int i;
	for(i=1;i<=n;++i)if(a[i][c]!=x)return false;	
	return true;
}

bool check(int x){
	int i,j;
	for(i=1;i<=n;++i)dr[i]=checkrow(i,x);
	for(i=1;i<=m;++i)dc[i]=checkcol(i,x);
	for(i=1;i<=n;++i)if(dr[i]){
		for(j=1;j<=m;++j)a[i][j]=x+1;
	}
	for(i=1;i<=m;++i)if(dc[i]){
		for(j=1;j<=n;++j)a[j][i]=x+1;
	}
	for(i=1;i<=n;++i)
		for(j=1;j<=m;++j)if(a[i][j]==x)return false;
	return true;
}
	

void solve(){
	scanf("%d%d",&n,&m);
	int maxx,i,j;
	maxx=0;
	for(i=1;i<=n;++i)
		for(j=1;j<=m;++j){
			scanf("%d",&a[i][j]);
			maxx=max(maxx,a[i][j]);
		}
	for(i=1;i<maxx;++i)if(!check(i)){
		printf("NO\n");
		return;
	}
	printf("YES\n");
}

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}