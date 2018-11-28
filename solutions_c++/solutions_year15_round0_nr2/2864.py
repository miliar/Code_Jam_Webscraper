#include <stdio.h>
#include <string.h>
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
	int n,ans=inf;
	int pan[1111];

	scanf("%d",&n);
	for (int i = 0; i < n; ++i) scanf("%d",&pan[i]);

	for (int i = 1; i < 1001; ++i)
	{
		if(ans<=i) return ans;
		int sum=0;
		for (int j = 0; j < n; ++j)
		{
			sum+=(pan[j]-1)/i;
		}
		ans=min(ans,sum+i);
	}
	return ans;
}

int main()
{
	//freopen("test.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 0; cas < T; ++cas)
	{
		printf("Case #%d: %d\n",cas+1,solve());
	}
	return 0;
}