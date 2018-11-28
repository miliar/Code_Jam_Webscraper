#include <bits/stdc++.h>
using namespace std;
#define pb(y) push_back(y)
typedef long long ll ;

void solve()
{

	int n , c,i,l;
	int A[100000];
	scanf("%d%d",&n,&c);
	for(int i =0;i<n;i++)
	{
		scanf("%d",&A[i]);
	}
	sort(A,A+n);
	std::vector<int> v;
	for(i =n-1;i>=0;i--)
	{
		if(A[i]>c/2)v.pb(A[i]);
		else break;
	}
	int ans = 0 ;
	for(i = i ;i>=0;i--)
	{
		l = v.size();
		if(l==0)
		{
			v.pb(A[i]);
		}
		else if(v[l-1]+A[i]<=c)
		{
			ans++;
			v.erase(v.begin()+l-1);
		}
		else v.push_back(A[i]);
	}
	printf("%d\n",ans+(int)v.size());
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