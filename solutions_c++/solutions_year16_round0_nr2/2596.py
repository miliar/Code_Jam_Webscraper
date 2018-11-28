//mohit____the_____great______and_________powerful_______!!!
#include <bits/stdc++.h>
using namespace std;
#define ll long long 
#define fi first 
#define se second
#define pb push_back  
#define mp make_pair
string s;
ll flip_all(ll ind)
{
	ll i ;
	for(i=0;i<=ind;i+=1)
		{if(s[i]=='-')s[i]='+';else s[i]='-'; }

}
int main()
{
	freopen("panin.txt","r",stdin);
	freopen("panout.txt","w",stdout);
	
	ll n ,t, i ,j , k, ans ;

	cin>>t;
	j=1;
	while(t--)
	{	ans=0;
		cin>>s;
		n=s.length();
		for(i=n-1;i>=0;i--)
		{
			if(s[i]=='-')
				{flip_all(i);ans++;}
		}
		cout<<"Case #"<<j<<": "<<ans<<endl;
		j+=1;

	}

	return 0;
}