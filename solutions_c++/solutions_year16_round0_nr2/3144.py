#include<bits/stdc++.h>
using namespace std;
#define ll long long int
char str[110];
ll recur(ll n,bool req)
{
	if(n==1)
	{
		if((req==1 && str[n-1]=='+') || (req==0 && str[n-1]=='-'))
			return 0;
		else
			return 1;
	}
	if(req==1)
	{
		if(str[n-1]=='+')
			return recur(n-1,1);
		else
			return 1+recur(n-1,0);
	}
	else
	{
		if(str[n-1]=='-')
			return recur(n-1,0);
		else
			return 1+recur(n-1,1);
	}
}
int main()
{
	ll counter=1,n,i,t,ans;
	cin>>t;
	while(t--)
	{
		cin>>str;
		n=strlen(str);
		//cout<<n<<endl;
		ans=recur(n,1);
		cout<<"Case #"<<counter<<": "<<ans<<endl;
		++counter;
	}
	return 0;
}