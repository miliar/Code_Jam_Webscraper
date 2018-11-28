#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{freopen("A-large.in","rt",stdin);
    freopen("1.out","wt",stdout);

	int t,n,k,i,count,aud;
	char smax[1005];
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		cin>>smax;
		aud=smax[0]-'0';
		count=0;
		for(i=1;i<=n;i++)
		{
			if(smax[i]!='0')
			{
			if(i>aud)
			{
				count+=(i-aud);
				aud=i;
			}
			aud+=smax[i]-'0';
			}
		}
		cout<<"Case #"<<k<<": "<<count<<"\n";
	}
	return 0;
}
