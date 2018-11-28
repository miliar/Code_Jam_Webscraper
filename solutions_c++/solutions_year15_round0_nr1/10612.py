#include<iostream>
#define ll long long int
#include<string.h>

using namespace std;

int main()
{
	ll t, c;
	char s[1005];
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>c;
		cin>>s;
		ll x=(ll)s[0]-'0', y=0;
		for(int j=1; j<=c; j++)
		{
			if(j<=x||s[j]=='0')
			x=x+(ll)s[j]-'0';
			else
			{
				y=y+j-x;
				x=j;
				x=x+(ll)s[j]-'0';
			}
		}
	cout<<"Case #"<<i<<": "<<y<<endl;
	}
}