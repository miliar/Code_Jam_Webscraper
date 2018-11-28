#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,i,j;
	string k,c;
	cin>>t;
	for(int l = 0;l<t;l++)
	{
		cout<<"Case #"<<l+1<<": ";
		cin>>i>>k;
		c=k;
		int ans=0;
		c[0]='0';
		for(i=1;i<k.length();i++)
		{
			c[i] = (c[i-1]-'0') + (k[i-1]-'0') + '0';
			if(k[i]!='0' && c[i]<i+'0') 
			{
				ans+=(i-c[i]+'0');
				c[i]+=(i-c[i]+'0');
			}
		}
		cout<<ans<<"\n";
	}
	return 0;	
}