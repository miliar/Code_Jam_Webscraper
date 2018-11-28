#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
ll t,i;
cin>>t;
for(i=1;i<=t;i++)
{
	string s,k="";
	cin>>s;
	char c='A';
	ll j;
	for(j=0;j<s.size();j++)
	{
		if(s[j]>=c)
		{
		k=s[j]+k; c=s[j];}
		else
		k+=s[j];
	}
cout<<"Case #"<<i<<": "<<k<<endl;
}

   return 0;

}


