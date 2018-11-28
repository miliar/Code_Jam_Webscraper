#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll,ll> mm;
string str;
ll solve()
{
	ll n=str.size();
	ll i;
	ll ind=0;
	ll count=0;
	ll is=0;
	for(i=0;i<n;i++)
	{
		if(str[i]!='-')
		{
			ind=i;
			break;
		}
		else
		{
			is=1;
		}
	}
	if(is==1)
	count+=1;
	ll flag=0;
	for(i=ind;i<n;i++)
	{
		if(flag==0 && str[i]=='+')
		{
			flag=1;
			count+=1;
		}
		else if(flag==1 && str[i]=='-')
		{
			flag=0;
			count+=1;
		}
	}
	if(str[n-1]=='+')
	count-=1;
	return count;
}
int main()
{
	ll t,n,i;
	FILE * pFile;
	pFile = fopen ("output.txt","w");
	//fscanf ("input.txt", "%lld", &t);
	cin>>t;
	ll c=0;
	while(t--)
	{
		c++;
		cin>>str;
		ll ans=solve();
		//cout<<ans<<endl;
		fprintf (pFile, "Case #%lld: %lld\n",c,ans);
		//cout<<ans<<endl;
	}
}
