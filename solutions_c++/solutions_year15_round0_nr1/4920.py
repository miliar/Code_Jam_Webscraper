#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define F(i,a,b) for(ll i=a;i<=b;i++)
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define ALL(a) (a.begin()),(a.end())
#define ZERO(a) memset(a,0,sizeof(a))
#define mp make_pair
#define pb push_back 
#define X first
#define Y second
#define pi 3.14159265
#define MOD 1000000007  

int main()
{	
	cin.sync_with_stdio(0);
	
	ll t;
	
	cin>>t;
	
	F(i,1,t)
	{
		ll num;
		
		cin>>num;
		
		string s;
		
		cin>>s;
		
		ll ppl=0;
		
		ll ans=0;
		
		F(j,0,num)
		if(s[j]!='0') //no ppl with shyness j, to aage bado
		{
			if(j>ppl)  //less ppl		
			{
				ans+=j-ppl; 
				ppl=j; //atleast j ppl must be standing		
			}
			
			ppl+=s[j]-'0'; //these ppl will also be standing
		}	
		
		cout<<"Case #"<<i<<": "<<ans<<"\n";
		
	}
	
    return 0;
}
