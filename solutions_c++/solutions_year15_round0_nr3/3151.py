#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<utility>
#include<set>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<cctype>


#define pb push_back
#define mp make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define ren(i,a,b) for(int i=a;i>=b;i--)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define pii pair<int,int>
#define vll vector<long long int>  
#define vii vector<int>
#define gi(n) scanf("%d",&n)
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define ostr(n) printf("%s",n)
#define ol(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
using namespace std;
 
typedef unsigned long long int ull;
typedef long long int ll;
int main()
{ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,t1=0;
gl(t);
map<pair<int,char>,int>m;
pair<int,char> p;
p.ff=0;p.ss='1';
m[p]=0;
p.ff=0;p.ss='i';
m[p]=1;
p.ff=0;p.ss='j';
m[p]=2;
p.ff=0;p.ss='k';
m[p]=3;
p.ff=1;p.ss='1';
m[p]=4;
p.ff=1;p.ss='i';
m[p]=5;
p.ff=1;p.ss='j';
m[p]=6;
p.ff=1;p.ss='k';
m[p]=7;
//pair<int,char>mul[8][8];
/*rep(i,0,7)
rep(j,0,7)
{
	if(i==j)
	{
		if(i==0||i==4)
		{
			mul[i][j].ff=0;
			mul[i][j].ss='1';
		}
		else
		{
			mul[i][j].ff=1;
			mul[i][j].ss='1';
		}
	}
	else
	{
		if(i==0||j==0)
		{
			if(i==0)
			{
				mul[i][j].ff
			}
		}
	}
}*/
char mul[][12]={{"1ijk1ijk"},{"i1kji1kj"},{"jk1ijk1i"},{"kji1kji1"},{"1ijk1ijk"},{"i1kji1kj"},{"jk1ijk1i"},{"kji1kji1"}};
int sign[8][8]={{0,0,0,0,1,1,1,1},{0,1,0,1,1,0,1,0},{0,1,1,0,1,0,0,1},{0,0,1,1,1,1,0,0},{1,1,1,1,0,0,0,0},{1,0,1,0,0,1,0,1},{1,0,0,1,0,1,1,0},{1,1,0,0,0,0,1,1}};
while(t--)
{
  ll l,x;
  cin>>l>>x;
  string s1,s;
  cin>>s1;
  rep(i,1,x)
  s+=s1;
  pair<int,char> dp[10005],dp1[10005];
  dp[0].ff=0;dp[0].ss='1';
  dp1[l*x+1].ff=0;dp1[l*x+1].ss='1';
  rep(i,0,l*x-1)
  {
  	dp[i+1].ff=sign[m[dp[i]]][m[mp(0,s[i])]];
  	dp[i+1].ss=mul[m[dp[i]]][m[mp(0,s[i])]];
  	//o2(dp[i+1].ff,dp[i+1].ss);on;
  }
  ren(i,l*x-1,0)
  {
  	dp1[i+1].ff=sign[m[mp(0,s[i])]][m[dp1[i+2]]];
  	dp1[i+1].ss=mul[m[dp1[i+2]]][m[mp(0,s[i])]];
  	//o2(dp1[i+1].ff,dp1[i+1].ss);on;
  }
  pair<int,char>isposs,kposs,iposs;
  kposs.ff=0;kposs.ss='k';
  iposs.ff=0;iposs.ss='i';
  isposs.ff=1;isposs.ss='1';int f=0,f1=0;
  if(dp[l*x]!=isposs)
  f=1;
  if(!f)
  {
  	rep(i,2,l*x-1)
  	{
  		if(dp[i]==kposs&&dp1[i+1]==kposs)
  		{
  			rep(j,1,i-1)
  			{
  				if(dp[j]==iposs)
  				{
  					f1=1;
  					break;
				  }
			}
  			
		}
		if(f1==1)
		break;
	}
  }
  t1++;
  ol("Case #");ol(t1);ol(": ");	
  if(f==1)
  ol("NO\n");
  else
  {
  	if(f1==0)
  	ol("NO\n");
  	else
  	ol("YES\n");
  }
}
return 0;
}
