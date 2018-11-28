#include <bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	ll t;ll z,k,c,s;
	scanf("%lld",&t);
	z=1;
	while(t--)
	{
		scanf("%lld%lld%lld",&k,&c,&s);
		cout<<"Case #"<<z<<": ";
		for(int i=1;i<=k;i++)
		{
			cout<<i<<" ";
		}
		cout<<endl;
		z++;
	}
	return 0;
}