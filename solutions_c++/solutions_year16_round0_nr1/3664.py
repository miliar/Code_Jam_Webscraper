#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vpi> vvpi;

ll gcd(int a, int b) {
	return (b == 0 ? a : gcd(b, a % b));
}
ll mod = 1000000007;
int lcm(int a, int b) {
	return ((a * b) / gcd(a, b));
}
ll pw(ll b, ll p) {
	if (!p)
		return 1;
	ll sq = pw(b, p / 2);
	sq = (sq * sq) % mod;
	if (p % 2)
		sq = (sq * b) % mod;
	return sq;
}ll _sieve_size;
bitset<10000010> bs;
vi primes;
void sieve(ll upperbound) {
_sieve_size = upperbound + 1;
bs.set();
bs[0] = bs[1] = 0;
for (ll i = 2; i <= _sieve_size; i++) if (bs[i]) {
for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
primes.push_back((int)i);
} }
ll num;
ll cnt;
vvi g(17);
string a[2],b[2];
map<int,int> mp;int n;
int arr[1000];
vi ans;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
int tt;cin>>tt;
ll big=1LL<<62;

while(tt--){cnt++;memset(arr,0,sizeof arr);ll tot=100000000;bool f=1;
	ll n;cin>>n;ll t=n;ll u=n;
	while(t<big&&tot--){
		n=t;
		while(n){
				arr[n%10]=1;
				n/=10;
			}
		ll sum =0;
		for (int i=0;i<11;i++){
			sum+=arr[i];
		}
		if (sum==10)
		{
			cout<<"Case #"<<cnt<<": "<<t<<endl;f=0;break;
		}
		else{
			t+=u;
		}
	}
	if(f)cout<<"Case #"<<cnt<<": "<<"INSOMNIA"<<endl;
}
}
