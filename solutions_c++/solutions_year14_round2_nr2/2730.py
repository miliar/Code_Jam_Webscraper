#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test,t,n,i,j,a,b,c,ans;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		ans=0;
		cin>>a>>b>>c;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<c)
				{
					ans++;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
    return 0;
}
