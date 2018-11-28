#include<iostream>
using namespace std;


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("q2.txt","w",stdout);
	int t;
	cin>>t;
	for(int test=1;test<=t;++test)
	{
		int a,b,k;
		cin>>a>>b>>k;
		long long ans=0;
		for(int i=0;i<a;++i)
		{
			for(int j=0;j<b;++j)
			{
				if((i&j)<k)
				{
					//cout<<i<<" "<<j<<endl;
					//if(i==j)
						++ans;
					//else
					//	ans+=2;
				}
			}
		}
		
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
