#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define pb push_back
#define lim ((ll)(1e5)+5)
#define F first
#define S second
#define D double
#define mod ((ll)(1e9)+7)
#define pq priority_queue
#define vl vector<ll>
#define pll pair<ll,ll>
#define vll vector<pll>
#define inf ((ll)(1e17)+7)
ll zero=0;
ll one=1;

int main()
{
ll t,temp;
ll coun=1;
scanf("%lld\n",&t);
while(t--)
{
	string s;
	getline(cin,s);
	ll ans=0;
	ll i=0;
  printf("Case #%lld: ",coun);
  coun++;
	ll noofitems=0;
	vector<char> a;
	a.clear();
	a.pb(s[0]);
	char p=s[0];
	for(i=1;i<s.size();i++)
	{
		if(s[i]!=p)
		{
		p=s[i];
		a.pb(s[i]);
		}
	}

	if((a[0]=='-')&&(((a.size())%2)==1))
	ans=1+(a.size()-1);
	else
    if((a[0]=='-')&&(((a.size())%2)==0))
    ans=1+(a.size()-2);
    else
    if((a[0]=='+')&&((a.size()%2)==1))
    ans=a.size()-1;
    else
    ans=a.size();
	printf("%lld\n",ans);


}
return 0;}

