#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int t,k,a,b,c,i,j,ans;
	cin>>t;
	for (k=1;k<=t;k++)
	{
		cin>>a>>b>>c;
		ans=0;
		for (i=0;i<a;i++)
			for (j=0;j<b;j++) if ((i&j)<c) ans++;
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
