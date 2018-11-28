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
	int n,ans=0,sum=0;
	string s;
	cin >> n >> s;

	for (int i = 0; i <= n; ++i)
	{
		if(ans+sum<i && s[i]>'0') ans+=i-sum-ans;
		sum+=s[i]-'0';
	}
	return ans;
}

int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 0; cas < T; ++cas)
	{
		printf("Case #%d: %d\n",cas+1,solve());
	}
	return 0;
}