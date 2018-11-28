#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
	ll i,j,k,l,m,n,t;
	char s[1005];
	scanf("%lld",&t);
	j=1;
	while(t--)
	{
		scanf("%lld",&n);
		scanf("%s",s);
		ll max=0;
		ll cnt=0;
		for(i=0;i<=n;i++)
		{
           if(i>max)
           {
             cnt=cnt+i-max;
             max=max+i-max;
           }
           max=max+(s[i]-48);
		}
		cout<<"Case #"<<j<<": "<<cnt<<endl;
		j++;
	}
}
