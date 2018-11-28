#include <bits/stdc++.h>
 
using namespace std;
 
#define      pii               std::pair<int,int>
#define      vi                std::vector<int>
#define      mp(a,b)           std::make_pair(a,b)
#define      X                 first
#define      Y                 second
#define      pb(x)             push_back(x)

 
typedef long long LL;
LL MOD = 1000000007;
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc = 1;tc <= t;tc++)
	{
		int n;
		scanf("%d",&n);
		string s;
		cin >> s;
		int cur = s[0]-'0';
		int ans = 0;
		for(int i=1;i<=n;i++)
		{
			if(cur < i) ans +=(i-cur) , cur = i;
			cur += (s[i]-'0');
		}
		printf("Case #%d: %d\n",tc,ans);
	}	
	return 0;
}
