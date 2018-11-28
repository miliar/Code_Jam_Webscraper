#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int v=1;
	while(v<=t)
	{
		int smax,i,j,n,ans=0,a[1005];
		char s[1005];
		cin>>smax;
		cin>>s;
		n=smax+1;
		for(i=0;i<n;i++) a[i]=s[i]-'0';
		int temp=0;
		temp = a[0];
		if(n==1)
		{
			ans=0;
		}
		else
		{
			for(i=1;i<n;i++)
			{
				if(temp>=i)
				{
					temp = temp+a[i];
				}
				else
				{
					ans = ans+i-temp;
                   // cout<<ans<<" "<<i<<"   ";
					temp = i+a[i];
				}
			}
		}
		cout<<"Case #"<<v<<": "<<ans<<endl;
		v++;
	}
	return 0;
}