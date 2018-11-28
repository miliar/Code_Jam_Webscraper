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

int main() {
	ios_base::sync_with_stdio(0);
	freopen("inp12.in","r",stdin);
	int t,smax,sum,p,temp;
	char s[1001];
	int a[1001];
	s(t);
	for(int x=1;x<=t;x++){
		s(smax);
		scanf("%s",s);
		p=0;
		a[0]=s[0]-48;
		//cout<< "i= " << 0 << "\ta[i]= " << a[0]<<endl;
		for(int i=1;i<=smax;i++){
			if(i<=a[i-1]){
				a[i]=a[i-1]+s[i]-48;
			}
			else{
				p+=1;
				a[i]=a[i-1]+s[i]-48+1;
			}
			//cout<< "i= " << i << "\ta[i]= " << a[i]<<endl;
			//cout<<"p= "<<p<<endl;
		}
		printf("Case #%d: %d\n",x,p);
	}
	return 0;
}
