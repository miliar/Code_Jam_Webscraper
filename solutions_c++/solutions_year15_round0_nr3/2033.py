/*Author: Rishul Aggarwal*/

#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define in(type,x) scanf("%" #type,&x)
#define debug(args...) {dbg,args; cerr<<endl;}
#define test int t;\
in(d,t);\
while(t--)

using namespace std;

struct debugger
{template<typename T> debugger& operator,(const T& v)
{cerr<< v <<" ";
return *this;
}
}dbg;

ll gcd(ll a,ll b) {if(b==0) return a; return gcd(b,a%b);}

ll power(ll b,ll exp,ll m) {ll ans=1; b%=m; while(exp){if(exp&1) ans=(ans*b)%m; exp>>=1; b=(b*b)%m; } return ans; }


char s1[10002][10002];
int s2[10002][10002];
char id[4][4]={'1','i','j','k','i','1','k','j','j','k','1','i','k','j','i','1'};
int sign[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
char mp[256];

int main()
{
  freopen("input.in","r",stdin);
  freopen("output.txt","w",stdout);
  int cas=1;
  mp['1']=0,mp['i']=1,mp['j']=2,mp['k']=3;
  test
  {
  	int m,x;
  	cin>>m>>x;
  	string s;
  	cin>>s;
  	string a;
  	rep(i,1,x) a+=s;
  	int l=a.length();
  	
  	for(int i=0;i<l;i++)
  	{
  		s1[i][i]=a[i];
  		s2[i][i]=1;
  		for(int j=i+1;j<l;j++)
  		{
  			int in1,in2;
  			in1=mp[s1[i][j-1]],in2=mp[a[j]];
  			s1[i][j]=id[in1][in2];
  			s2[i][j]=s2[i][j-1]*sign[in1][in2];
  		}
  	}
  	
    	
  	//now try placing partition for getting 'j' 
  	
  	bool flag=0;
  	for(int i=1;i<l-1;i++)
  	{
  		for(int j=i;j<l-1;j++)
  		{
  			//a[i..j] is partition for 'j'
  			
  			if(s1[0][i-1]=='i' && s1[i][j]=='j' && s1[j+1][l-1]=='k' && s2[0][i-1]==1 && s2[i][j]==1 && s2[j+1][l-1]==1)
  			{
  				flag=1;
  				break;
  			}
  		}
  		if(flag) break;
  	}
  	//cout<<"here2\n";
  	
  	if(flag) cout<<"Case #"<<cas<<": "<<"YES\n";
  	else cout<<"Case #"<<cas<<": "<<"NO\n";
	cas++; 	
  
  }

  return 0;
}

