#include <bits/stdc++.h>
using namespace std;
#define pb(y) push_back(y)
typedef long long ll ;

void solve()
{
	int n ; 
	std::vector<int> v;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		int curr;
		scanf("%d",&curr);
		v.pb(curr);
	}
	int ans =0 ;
	for(int i =0;i<n;i++)
	{
		int min_element  = v[0];
		int mini =0;
		int l = v.size();
		for(int j=0;j<l;j++)
		{
			if(v[j]<min_element)
			{
				min_element = v[j];
				mini = j;
			}
		}
		//printf("%d %d\n",mini, min_element );
		ans = ans + min(mini , l-mini-1);
		v.erase(v.begin()+mini);
	}
	printf("%d\n",ans);
	return;
}
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}