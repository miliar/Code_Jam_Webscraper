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
int A[1000001];
int main()
{
	int t;
	scanf("%d",&t);
	for(int tc = 1;tc <= t;tc++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&A[i]);
		}
		int ans = MOD , m;
		for(int i = 1 ; i<1001 ; i++)
		{
			int cur = 0 , m =0;
			for(int j=0;j<n;j++)
			{
				if(A[j
					]>=i) m = i;
				cur += (A[j]-1)/i;
				m = max(m  , (A[j]%i));
			}
			cur += m;
			ans = min(cur,ans);
		}		
		printf("Case #%d: %d\n",tc,ans);
	}	
	return 0;
}
