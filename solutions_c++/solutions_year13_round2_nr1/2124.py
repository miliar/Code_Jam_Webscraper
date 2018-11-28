#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm> 
#include <iostream>
#include <cmath>
using namespace std;
#define INF 100000000
int dp[105][105];
int t,x,n;
int a[1000006];

int solve(int pos, int sz){
	if (dp[pos][sz] > -1) return dp[pos][sz];
	if (pos >=n) return dp[pos][sz] = 0;
	int ret = 1+solve(pos+1,sz);
	//cout << pos <<" " <<sz << "   " << ret <<endl;
	if (sz > a[pos]){ //cout << sz <<" " << a[pos] << endl; 
	ret = min(ret,solve(pos+1,min(101,sz+a[pos])));
	}
	for (int i = sz+1; i <=min(101,sz*2-1); ++i){
		//cout << i << endl;
		ret = min(ret,1+solve(pos,i));
	}
	//cout <<pos <<" " << sz <<"  " << ret << "            " << a[pos] << endl;
	return dp[pos][sz] = ret;

}

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for (int tc = 1; tc <=t; ++tc){
		printf("Case #%d: ",tc);
		scanf("%d %d",&x,&n);
		for (int i =0; i <n; ++i )
			scanf("%d",&a[i]);
		sort(a,a+n);
		memset(dp,-1,sizeof(dp));
		printf("%d\n",solve(0,x));
	}

}