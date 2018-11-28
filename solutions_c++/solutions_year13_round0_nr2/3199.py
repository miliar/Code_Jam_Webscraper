//#pragma comment(linker, "/STACK:134217728,134217728") /*128Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
#include <algorithm>
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>
using namespace std;

/*--in common define-----*/
#define N  110
#define E  100010
#define ll long long
const ll PRIME =999983;
const ll MOD   =1000000007;
const ll MULTI =1000000007;
/*--end in common define-*/

/*--in common use--------*/
#define cube(x) ((x)*(x)*(x))
#define sq(x)     ((x)*(x))
#define all(x)     x.begin(),x.end()
#define lp(a,s,t)   int (a)=(s);(a)<(t);(a)++
#define lpe(a,s,t) int (a)=(s);(a)<=(t);(a)++
inline bool isodd(int x){return x&1;}
inline bool isodd(ll x) {return x&1;}
/*--end in common use----*/

int n,m,a[N][N];
bool visit[N][N];
int d[N*N];
vector<pair<int,int> > v[110]; 
bool check(int x)
{
	int k;
	for(int t=0;t<v[x].size();t++){
		int i=v[x][t].first, j=v[x][t].second;
		if(visit[i][j]) continue;
		for(k=0;k<m;k++)
			if(a[i][k]>x) break;
		if(k==m){
			for(k=0;k<m;k++)
				if(a[i][k]==x) visit[i][k]=true;
			continue;
		}
		for(k=0;k<n;k++)
			if(a[k][j]>x) break;
		if(k==n){
			for(k=0;k<n;k++)
				if(a[k][j]==x) visit[k][j]=true;
			continue;
		}
		return false;
	}
	return true;
}

bool solve(int num)
{
	memset(visit,false,sizeof(visit));
	for(int i=0;i<num;i++)
		if(!check(d[i])) return false;
	return true;
}

int main() {

	int re,Case=1;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&re);
	while(re--){
		scanf("%d %d",&n,&m);
		for(int i=0;i<=100;i++) v[i].clear();
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%d",&a[i][j]);
				v[a[i][j]].push_back(make_pair(i,j));
				d[i*m+j]=a[i][j];
			}
		}
		sort(d,d+n*m);
		printf("Case #%d: ",Case++);
		if(solve((unique(d,d+n*m)-d))) puts("YES");
		else puts("NO");
	}
	return 0;
}