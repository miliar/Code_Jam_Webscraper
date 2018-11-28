/*_______SHREY MANIK______*/
#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <iomanip>
#include <list>
#include <bitset>
#define ff first
#define ss second
#define mod 1000000007
#define SET(a) memset(a,-1,sizeof(a))
#define CLEAR(a) memset(a,0,sizeof(a))
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
using namespace std;
typedef long long LL;
typedef pair< int , int > pii;
typedef pair< int , LL> pil;
typedef pair< LL, int>pli;
typedef pair< LL, LL> pll;
typedef vector< LL >vl;
typedef vector< int > vi;
template<class T>T gcd(T a,T b){return (b==0)?a:gcd(b,a%b);}
template<class T>T lcm(T a,T b){return (a*b)/gcd(a,b);}
template<class T>T powmod(T a,T b) {T res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}

LL n,i,a;
int t,k,m;
set<LL>s;
void decimal(LL a)
{
	while(a>0)
	{
		s.insert(a%10);
		a/=10;
	}
}
int r=1;
int main()
{
  freopen("input.in","r",stdin);
   freopen("output1.txt","w",stdout);
  cin>>t;
  while(t--)
  {
  		cin>>n;
  		a=n;
		i=1;
		if(n==0){
	
  			cout<<"Case #"<<r<<": INSOMNIA\n";
  			
  }
    else{
	
	  	
  		while(1){
		k = s.size();
  		decimal(n);
  		m = s.size();
  		
  		 if(m == 10)
			{
				cout<<"Case #"<<r<<": "<<n<<"\n";
				break;
			} 
		 
		else{
			++i;
			n=i*a;
		}
		
		
	}
	}
	++r;
	s.clear();
  }
  return 0;
}




