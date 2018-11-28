#include <bits/stdc++.h>
using namespace std;
 double pi=3.14159265359;
#define infinity (1000000007)
#define ll long long
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define pip pair<int,pii>
typedef vector<int> vi;
typedef vector<pii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define pb push_back
#define s(n) scanf("%lld",&n)
#define s2(n,m) scanf("%lld%lld",&n,&m)
#define s3(n,m,l) scanf("%lld%lld%lld",&n,&m,&l)
#define rep(i,n) for(long long i=0;i<n;i++)
ll pwr(ll a,ll b,ll mod) {ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
long long mod=1000000007;
int main()
{
	long long a=0,b,c,d,i,j,l,sum,result,n,m,k=0,s,t;
    scanf("%lld",&t);
    while(t--)
    {
    	cin>>a;
    	if(a==0)
    	printf("Case #%lld: INSOMNIA\n",++k);
    	else{
    		int hash1[10]={0};
    		int flag=1;i=0;
    		while(flag){
    			i++;
    			result=a*i;
    			
    			while(result!=0){
    				hash1[result%10]=1;
    				
    				result/=10;
    			
    			}
    			
    			for( j=0;j<10;j++){
    				if(hash1[j]!=1)
    				break;
    			}
    			if(j==10)
    			flag=0;
    			
    		}
    		printf("Case #%lld: %lld\n",++k,i*a);
    	}
    	
    }
	return 0;
}





