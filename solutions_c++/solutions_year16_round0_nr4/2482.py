#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
	ll t,c,k,s,r,counter=1,i,j;
	cin>>t;
	while(t--)
	{
		cin>>k>>c>>s;
		cout<<"Case #"<<counter++<<": ";
		if(k==1)
		{
			cout<<"1\n";
			continue;
		}
		if(c==1)
		{
			if(s<k)
				cout<<"IMPOSSIBLE\n";
			else
			{
				for(i=1;i<=k;++i)
					cout<<i<<" ";
				cout<<endl;
			}
			continue;
		}
		for(i=2,j=1;j<k;++j,++i)
			cout<<i<<" ";
		cout<<endl;
	}
	return 0;
}