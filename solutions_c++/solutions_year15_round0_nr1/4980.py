#include <bits/stdc++.h>
using namespace std;
string data;
int a[1010];
int main()
{
	int t,i,j=1;
	int s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		cin>>data;
		for(i=0;i<=s;i++)
		{
			a[i]=data[i]-'0';
			// cout<<a[i]<<endl;
		}
		int x=a[0];
		int res=0;
		for(i=1;i<=s;i++)
		{
			if(x<i && a[i]!=0)
			{
				// res+=(a[i]-(x+res));
				res+=(i-x);
				x+=(i-x);
				// cout<<a[i]<<"\t"<<x<<"\t"<<i<<endl;
			}
			x+=a[i];
		}
		cout<<"Case #"<<j<<": "<<res<<endl;
		j++;
	}
	return 0;
}