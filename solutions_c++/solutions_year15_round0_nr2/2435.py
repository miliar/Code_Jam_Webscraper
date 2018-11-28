#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;
 
typedef long long LL;
std::vector<int> A(100000);
int main()
{
	int t;
	cin>>t;
	for(int cas = 1;cas <= t;cas++)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>A[i];
		}
		int ans = 1e9 ;
		int m;
		for(int i = 1 ; i<1001 ; i++)
		{
			int cur = 0 , m =0;
			for(int j=0;j<n;j++)
			{
				if(A[j]>=i) m = i;
				cur += (A[j]-1)/i;
				m = max(m  , (A[j]%i));
			}
			cur += m;
			ans = min(cur,ans);
		}		
		printf("Case #%d: %d\n",cas,ans);
	}	
	return 0;
}
