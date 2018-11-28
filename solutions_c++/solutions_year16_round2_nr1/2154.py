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
	ll a,n,b,m,c,d,e,f;
	ll t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	string s;
	for(b=1;b<=t;b++)
	{
		cin>>s;
		ll siz=s.size();
		ll ct[200];
		memset(ct,0,sizeof(ct));
		for(a=0;a<siz;a++)
		{
			ct[s[a]]++;
		}
		ll ans[20];
		ans[0]=ct['Z'];
		ct['Z']=0;
		ct['E']-=ans[0];
		ct['R']-=ans[0];
		ct['O']-=ans[0];
		
		ans[2]=ct['W'];
		ct['W']=0;
		ct['T']-=ans[2];
		ct['O']-=ans[2];
		
		ans[4]=ct['U'];
		ct['F']-=ans[4];
		ct['O']-=ans[4];
		ct['U']-=ans[4];
		ct['R']-=ans[4];
		
		ans[6]=ct['X'];
		ct['S']-=ans[6];
		ct['I']-=ans[6];
		ct['X']=0;
		
		ans[8]=ct['G'];
		ct['E']-=ans[8];
		ct['I']-=ans[8];
		ct['G']-=ans[8];
		ct['H']-=ans[8];
		ct['T']-=ans[8];
		
		ans[1]=ct['O'];	
		ct['O']=0;
		ct['N']-=ans[1];
		ct['E']-=ans[1];
		
		ans[3]=ct['T'];
		ct['T']-=ans[3];
		ct['H']=0;
		ct['R']-=ans[3];
		ct['E']-=2*ans[3];
		
		ans[5]=ct['F'];
		ct['F']-=ans[5];
		ct['I']-=ans[5];
		ct['V']-=ans[5];
		ct['E']-=ans[5];
		
		ans[7]=ct['S'];
		ct['S']-=ans[7];
		ct['E']-=ans[7];
		ct['V']-=ans[7];
		ct['E']-=ans[7];
		ct['N']-=ans[7];
		
		ans[9]=ct['N']/2;
		cout<<"Case #"<<b<<": ";
		for(a=0;a<10;a++)
		{
			while(ans[a]--)
			{
				cout<<a;
			}
		}
		cout<<endl;
	}
	return 0;
}
