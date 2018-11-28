/*Author:
raunakrocks
Raunak Talwar
Final Year CSE'15 
MNNIT-Allahabad
raunaktalwar00@gmail.com
*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
/**** b'oz i'm lazzyy :P ****/
#define MAXI 100005
#define inp(n) scanf("%lld",&n) //for codeforces :P
#define FOX(i,n) for(ll i=0;i<n;i++)
#define FOX1(i,n) for(ll i=1;i<=n;i++)
#define FOX2(i,n) for(ll i=n;i>=1;i--)
#define foxi(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pb push_back
#define sf scanf
#define pf printf
#define MOD 1000000007
/*#define gc getchar_unlocked
void inp(ll &n)
{
	n=0;
	char ch=gc();
	ll sign=1;
	while(ch<'0'||ch>'9')
	{
		if(ch=='-')
			sign=-1;
		ch=gc();		
	}	
	while(ch>='0'&&ch<='9')
		{
			n=(n<<3)+(n<<1)+(ch-'0');
			ch=gc();
		}
		n*=sign;
}*/
ll mini(ll a,ll b){ return a>b?b:a; }
ll maxi(ll a,ll b){ return a>b?a:b; }
/***debugging stuff :P ***/
#define DEBUG 0
#ifdef DEBUG
    #define db(x)            cerr<<x<<endl;
    #define db1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define db2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define db3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
#else
    #define db(x)
    #define db1(x)
    #define db2(x,y)
    #define db3(x,y,z)
#endif


ll t,S,c,r,T=1;
char a[1999];

int main()
{
	clock_t startTime=clock();
	/******START: code here*********/
	inp(t);
	while(t--)
	{
		inp(S);
		sf("%s",a);
		c=a[0]-'0';	
		r=0;	
		for(ll i=1;i<=S;i++)
		{
			if(a[i]!='0')
			{
				if(c>=i)
				{
					c=c+(a[i]-'0');
					continue;
				}
				else
				{
					r=r+(i-c);
					c=c+(a[i]-'0')+(i-c);
				}
			}
		}
		pf("Case #%lld: %lld\n",T,r);
		T++;
	}
	/******END:code here**********/
	clock_t endTime=clock();
	cerr<<"\nTime:"<< double(endTime - startTime) / CLOCKS_PER_SEC <<" seconds\n" ;
	return 0;
}




