#include<iostream>
using namespace std;
#include<set>
#include<algorithm>
#include<string.h>
#define ll long long int
ll mark[10010];
int main()
{
	ll a,n,count,t,i,j,counter=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		memset(mark,0,sizeof(mark));
		for(i=0;i<(2*n-1);++i)
		{
			for(j=0;j<n;++i)
			{
				cin>>a;
				++mark[a];
			}
		}
		set<ll> ans;
		for(i=1;i<=2500;++i)
		{
			if(mark[i]%2==1)
				ans.insert(i);
		}
		set<ll>::iterator it=ans.begin();
		cout<<"Case #"<<counter++<<": ";
		for(;it!=ans.end();++it)
			cout<<(*it)<<" ";
	}
	return 0;
}
