#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
const int inf=0xfffffff;

int solve(){
	int c,d,v;
	bool dp[111];
	cin >> c >> d >> v;

	memset(dp,0,sizeof dp);
	dp[0]=true;

	for (int i = 0; i < d; ++i)
	{
		int n;
		scanf("%d",&n);
		for (int i = v-n; i >= 0; --i)
		{
			if(dp[i]) dp[i+n]=true;
		}
	}

	int ans=0;
	for (int k = 0; k <= v; ++k)
	{
		if(!dp[k]){
			ans++;
			for (int i = v-k; i >= 0; --i)
			{
				if(dp[i]) dp[i+k]=true;
			}
		}
	}
	return ans;
}

int main(){
	//freopen("test.in","r",stdin);
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: %d\n",cas,solve());
	}
	return 0;
}