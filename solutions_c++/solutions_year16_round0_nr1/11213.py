#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F(i,a,b) for(ll i=a;i<=b;i++)
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define ALL(a) (a.begin()),(a.end())
#define ZERO(a) memset(a,0,sizeof(a))
#define mp make_pair
#define pb push_back 
#define X first
#define Y second 
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n) 
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;  
void fast_io() { cin.tie(0); ios::sync_with_stdio(false); } 
const ll SIZE=(ll)1e3;

int main(){
	
	int t;
	scanf("%d",&t);
	ll n;
	
	for(int T=1;T<=t;++T)
	{
		scanf("%lld",&n);
		ll add=n;
		
		bool occ[10]={0};
		int c=0;
		
		while(c!=10)
		{
			ll temp=n;
			
			while(temp!=0)
			{
				if(occ[temp%10]==0)
				{
					occ[temp%10]=1;
					++c;
				}
				
				temp/=10;	
			}
			
			if(c==10) //solution found
			{
				printf("Case #%d: %lld\n",T,n);	
				break;
			}
			
			if(n+add<=n) //solution does not exist
			{	
				printf("Case #%d: INSOMNIA\n",T);
				break;
			}
			else n+=add; //solution  may exist, has to be found
		}
		
	}
	
	return 0;
}