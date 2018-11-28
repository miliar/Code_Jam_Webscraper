#include <bits/stdc++.h>
using namespace std;
#define infinity (1000000007)
#define ll long long
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define s(n) scanf("%d",&n)
#define s2(n,m) scanf("%d%d",&n,&m)
#define s3(n,m,l) scanf("%d%d%d",&n,&m,&l)
#define p(n) printf("%d\n",n)
#define rep(i,n) for(int i=0;i<n;++i)
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
//const int mod=1000000007;
int a[1001];

int main() {
	//ios_base::sync_with_stdio(0);
	//freopen("inp1.in","r",stdin);
	int t,n;
	ll sum,maxdiff,ans2;
	s(t);
	for(int x=1;x<=t;x++){
		s(n);
		for(int i=0;i<n;i++){
			s(a[i]);
		}
		sum=0;
		maxdiff=-1;
		for(int i=1;i<n;i++){
			if(a[i]<a[i-1]){
				sum+=a[i-1]-a[i];
			}
			if((a[i-1]-a[i])>maxdiff){
				maxdiff = a[i-1]-a[i];
			}
		}
		//cout << "maxdiff= " << maxdiff << endl; 
		ans2=0;
		for(int i=0;i<n-1;i++){
			if(a[i]<=maxdiff){
				ans2 += a[i];
			}
			else{
				ans2 += maxdiff;
			}
		}
		printf("Case #%d: %lld %lld\n",x,sum,ans2);
	}
	return 0;
}
