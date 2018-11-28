									/*	In the name of God	*/
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

int n,b[101],dp[101][1001*1001];

int rec(int x,int a){
	if (x==n || a>b[n-1])return 0;
	if (dp[x][a]!=-1)
		return dp[x][a];
	if (b[x]<a)
		return dp[x][a]=rec(x+1,a+b[x]);
	else{
		if (a==1)
			return dp[x][a]=1+rec(x+1,a);
		ll y=a;
		int i=0;
		while (y<=b[x]){
			y+=y-1;
			i++;
		}
		return dp[x][a]=min(1+rec(x+1,a),i+rec(x,y));
	}
}

int main(){
	
	freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);	
	int a,ti,tc,i,j,m;
	scanf("%d",&tc);
	rep(ti,tc){
		memset(dp,-1,sizeof dp);
		scanf("%d %d",&a,&n);
		rep(i,n)
			scanf("%d",&b[i]);
		sort(b,b+n);		
		printf("Case #%d: %d\n",ti+1,rec(0,a));
	}
	
	return 0;
}