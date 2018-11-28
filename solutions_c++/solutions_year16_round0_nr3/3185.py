#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vpi> vvpi;
#include<string>
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

int arr[1000];
vi ans;
string tobi(ll n)
{
	string s="";
while(n){
	int a=n%2;
	n/=2;
if(a)s+='1';
else s+='0';
}
return s;
}
ll fun (string n,ll m){
	ll ans=0;
	for ( int i=0;i<n.size();i++){
		if(n[i]=='1')ans+=(ll)pow(m,i);
	}

	return ans;
}
bool isprime(ll n){
	for ( ll i=2;i*i<=n;i++){
		if(n%i==0)return 0;
	}
	return 1;
}
int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
sieve(10000000);
	int tt;cin>>tt;
map <ll,vector <string> > mp;
	for (int j=0;j<(1<<14);j++){
		ll num=((j*2)|(1<<(15)))+1;
string num2=tobi(num);bool f=1;
for (int k=2;k<11;k++){
	ll z=fun(num2,k);
	if(isprime(z)){f=0;break;}
}
if(f)mp[16].push_back(num2);
if(mp[16].size()>=50)break;
	}

while(tt--){cnt++;
	int a,b;cin>>a>>b;
	cout<<"Case #"<<cnt<<":"<<endl;
	for ( int i=0;i<b;i++){
string temp=mp[a][i];
for(int i=temp.size()-1;i>=0;i--)cout<<temp[i];cout<<" ";
for (int k=2;k<11;k++){
	ll div =fun(temp,k);
	for (int j=2;;j++){
		if(div%j==0){
			cout<<j<<" ";break;
		}
	}
	}
cout<<endl;
}
}
}
