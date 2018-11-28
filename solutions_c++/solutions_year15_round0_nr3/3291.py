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

ll sign[4][4];
		
char mul[4][5]={ "1ijk","i1kj","jk1i","kji1"  };
		
map<char,ll> m;

int main()
{	
	cin.sync_with_stdio(0);
	
	ll t;
	
	F(i,0,3)
	F(j,0,3)
	sign[i][j]=1;
		
	sign[1][1]=-1;
	sign[1][3]=-1;	
	sign[2][1]=-1;
	sign[2][2]=-1;
	sign[3][2]=-1;
	sign[3][3]=-1;

	m['1']=0;
	m['i']=1;
	m['j']=2;
	m['k']=3;
	
	cin>>t;

	F(T,1,t)
	{
		ll l,x;
		
		ll yes=0;
		
		cin>>l>>x;
		
		string s1;
		
		cin>>s1;
		
		string s=s1;
		
		ll len=l*x;
		
		F(i,2,x)
		s=s+s1;
		
		ll fk=0;
		ll fi[10010]={0};
		
		ll a;
		ll sn;	
		
		for(ll i=len-1;i>=0;i--)
		{
			ll op1=m[s[i]]; //converted to number
			
			if(i==len-1)
			{
				a=op1;
				sn=1;
			}
			else
			{	
				sn=sign[op1][a] * sn; //sign
			
				a=m[ mul[op1][a] ];		//number
			
			}
			
			if(a==3 && sn==1 && fk==0)
			fk=i; //farthest k
			
			if(a==1 && sn==1)	
			fi[i]=1; //i found at i index
				
		}
		
		F(i,0,len-1)
		{
			ll op1=m[s[i]]; //to num	
			
			if(i==0)
			{
				a=op1;	
				sn=1;
			}
			else
			{
				sn=sign[a][op1] * sn;
				
				a=m[ mul[a][op1] ];
			}
			
			if(sn==1 && a==1)
			if(fi[i+1]==1 && fk>=i+2)
			{
				yes=1;	
				break;
			}
			
		}
		
		if(yes)
		cout<<"Case #"<<T<<": YES\n";
		else cout<<"Case #"<<T<<": NO\n";

	}
	
    return 0;
}
	
		//F(i,0,len-1)
		//cout<<fi[i];
		
		//cout<<"\n";
