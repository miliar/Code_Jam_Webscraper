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
ll rap[26];
ll ans[10];
int main()
{
    ll t,l,p;
    unsigned int i;
    string s;
    cin>>t;
    for(p=1;p<=t;p++)
    {
		memset(rap,0,sizeof(rap));
		memset(ans,0,sizeof(ans));
		cin>>s;
		l=s.size();
		for(i=0;i<l;i++)rap[s[i]-'A']++;
		//for(i=0;i<26;i++)cout<<rap[i]<<" ";cout<<endl;
		if(rap[25]!=0)
		{
			ans[0]=ans[0]+rap[25];
			ll temp=rap[25];
			string kk="ZERO";
			for(i=0;i<kk.length();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[23]!=0)
		{
			ans[6]=ans[6]+rap[23];
			ll temp=rap[23];
			string kk="SIX";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
		
		if(rap[20]!=0)
		{
			ans[4]=ans[4]+rap[20];
			ll temp=rap[20];
			string kk="FOUR";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[22]!=0)
		{
			ans[2]=ans[2]+rap[22];
			ll temp=rap[22];
			string kk="TWO";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[14]!=0)
		{
			ans[1]=ans[1]+rap[14];
			ll temp=rap[14];
			string kk="ONE";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[17]!=0)
		{
			ans[3]=ans[3]+rap[17];
			ll temp=rap[17];
			string kk="THREE";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[5]!=0)
		{
			ans[5]=ans[5]+rap[5];
			ll temp=rap[5];
			string kk="FIVE";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[18]!=0)
		{
			ans[7]=ans[7]+rap[18];
			ll temp=rap[18];
			string kk="SEVEN";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[6]!=0)
		{
			ans[8]=ans[8]+rap[6];
			ll temp=rap[6];
			string kk="EIGHT";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		if(rap[8]!=0)
		{
			ans[9]=ans[9]+rap[8];
			ll temp=rap[8];
			string kk="NINE";
			for(i=0;i<kk.size();i++)rap[kk[i]-'A']=rap[kk[i]-'A']-temp;
			}
			
		cout<<"Case #"<<p<<": ";
		for(i=0;i<10;i++)
		{
			if(ans[i]!=0)
			{
				while(ans[i])
				{
					cout<<i;
					ans[i]--;
					}
				}
			}
			cout<<endl;
		}
    return 0;
}
