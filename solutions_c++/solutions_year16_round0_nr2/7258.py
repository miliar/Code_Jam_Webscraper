/*

-------------------------------------------------------------------------------------------------\
 \       |AUTHOR: RAGHU PAAVAN(rap)  :D ---------------------------------------------------------- \
 /       |        NIT CALICUT  ------------------------------------------------------------------- /
---------|----------------------------------------------------------------------------------------/

*/
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll    long long int
#define all(c) c.begin(),c.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define scan(x) scanf("%d", &x)
#define scanl(x) scanf("%lld", &x)
#define print(a) printf("%d\n",a)
#define printl(a) printf("%lld\n",a)
#define pb push_back
#define maxn 100005
ll rap[100];
int main()
{
    ll i,t,l;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
		ll count=1;
		string s;
		cin>>s;
		memset(rap,0,sizeof(rap));
		l=s.size();
		if(s[0]=='+')rap[0]=1;
		else rap[0]=0;
		i=1;
		while(i<l)
		{
			if(s[i]!=s[i-1])count++;
			i++;
			}
		if(count%2)
		{
			if(rap[0]==0)cout<<"Case #"<<k<<": "<<count<<endl;
			else cout<<"Case #"<<k<<": "<<count-1<<endl;
			}
		else
		{
			if(rap[0]==0)cout<<"Case #"<<k<<": "<<count-1<<endl;
			else cout<<"Case #"<<k<<": "<<count<<endl;
			}
	}
    return 0;
}
