#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	ll t;
	cin>>t;
	ll c=0;
	char str[1010];
	while(t--)
	{
		c++;
		ll n;
		cin>>n>>str;
		ll ptr=0;
		ll count=str[0]-'0';
		for(ll i=1;i<=n;i++)
		{
			if(count<i)
			{
				ptr+=i-count;
				count+=i-count;
				count+=str[i]-'0';
			}
			else
			{
				count+=str[i]-'0';
			}
		}
		
		cout<<"Case #"<<c<<": "<<ptr<<endl;
	}
return 0;
}