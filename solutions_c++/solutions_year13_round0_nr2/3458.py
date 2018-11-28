#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <map>
#define rep(i,n) for (int i=0;i<n;i++)
#define Max(a,b) a>b?a:b
#define Min(a,b) a<b?a:b
#define INF 0x7fffffff
#define fop freopen("data.in", "r", stdin); freopen("data.out", "w", stdout);
#define LL long long
using namespace std;
const int maxn=105;
int a[maxn][maxn];
int N,M;
int row[maxn],col[maxn];
bool isok;

int  findMax(int id,bool h)
{
	int mx=-1;
	if (h==1){
		rep(i,M)
			if (mx<a[id][i]) mx=a[id][i];
	}
	else {
		rep(i,N)
			if(mx<a[i][id]) mx=a[i][id];
	}
	return mx;

}

void solve(){
	rep(i,N) rep(j,M)
		if (a[i][j]<row[i] && a[i][j]<col[j])
		{
			isok=false;
			return;
		}
}
int main(){
	int T;  
	fop;
	scanf("%d",&T);
	for (int cas=1;cas<=T;++cas)
	{
		isok=true;
		scanf("%d%d",&N,&M);
		rep (i,N) rep(j,M)
			scanf("%d",&a[i][j]);
		rep (i,N) row[i]=findMax(i,1);
		rep (j,M) col[j]=findMax(j,0);
		solve();
		printf("Case #%d: ",cas);
		if (isok) printf("YES\n");
		else printf("NO\n");

	}
	return 0;
}
