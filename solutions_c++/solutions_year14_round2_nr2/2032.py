#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		int a,b,k;
		cin>>a>>b>>k;
		int ans = 0,rep = 0;
		for (int i=0;i<a;i++)
			for (int j=0;j<b;j++)
			{
				//cout<<i<<" "<<j<<" "<<(i&j)<<"\n";
				if ((i&j)<k)
				{
					ans++;
					//cout<<i<<" "<<j<<" "<<(i&j)<<"\n";
					
				}
			}		
		cout<<"Case #"<<tt<<": "<<ans<<"\n";
	}
	return 0;
}