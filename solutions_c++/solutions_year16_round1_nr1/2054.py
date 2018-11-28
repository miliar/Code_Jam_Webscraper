#include<bits/stdc++.h>
using namespace std;
#define ll long 
#define lim 100005
#define mk make_pair
#define pll pair<ll,ll>
#define pb push_back
#define X first
#define Y second
#define MOD 1000000007
#define ios ios_base::sync_with_stdio(0)




int main(void)
{
	ios;
	ll a,n,b,m,c,d,e,t,f;
	string s,r,temp1,temp2;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(a=1;a<=t;a++)
	{
		cin>>s;
		
		for(b=0;b<s.size();b++)
		{
			temp1=r;
			temp1+=s[b];
			temp2=r;
			temp2.insert(temp2.begin(),s[b]);
			r=max(temp1,temp2);
		}
		cout<<"Case #"<<a<<":"<<" "<<r<<endl; 
		r.clear();
	}
	return 0;
}
