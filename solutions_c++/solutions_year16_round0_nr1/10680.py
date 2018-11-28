#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define fi first
#define se second
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PII;
const ll mod=1000000007;
ll powmod(ll a,ll b) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head


set<int> digits;

void get_digits(ll n){
	while(n>0){
		int d=n%10;
		n/=10;
		digits.insert(d);
	}
}

int check(ll n){
	for (ll i = 1; i <=100 ; ++i)
	{
		get_digits(n*i);
		if(digits.size()==10){
			return n*i;
		}
	}
	return -1;
}

int main(){
	int c;
	cin>>c;
	for (int i = 1; i <= c; ++i)
	{
		long long int n;
		cin>>n;
		digits.clear();
		ll ans=check(n);
		cout<<"Case #"<<i<<": "; 
		if(ans==-1)
			cout<<"INSOMNIA\n";
		else
			cout<<ans<<endl;
	}
	return 0;	
}
