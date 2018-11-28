#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define abs_val(a) (((a)>=0)?(a):-(a))

ll mulmod(ll a, ll b, ll c) {
  ll x = 0, y = a % c;
  while (b) {
    if (b & 1) x = (x + y) % c;
    y = (y << 1) % c;
    b >>= 1;
  }
  return x % c;
}
ll Pow(ll a, ll b){
    ll x = 1, y = a;
    while(b > 0){
        if(b % 2 == 1){
            x = (x * y);
        }
        y = (y * y);
        b /= 2;
    }
    return x;
}

ll gcd(ll a, ll b) { return !b ? a : gcd(b, a % b); }
ll pollard_rho(ll n) {
	int i = 0, k = 2;
	ll x = 3, y = 3;
	while (1) {
		i++;
		x = (mulmod(x, x, n) + n - 1) % n;
		ll d = gcd(abs_val(y - x), n);
		if (d != 1 && d != n) return d;
		if (i == k) y = x, k *= 2;
	}
}
 
ll fastPow(ll x, ll n, ll MOD) {
  ll ret = 1;
  while (n) {
    if (n & 1) ret = mulmod(ret, x, MOD);
    x = mulmod(x, x, MOD);
    n >>= 1;
  }
  return ret;
}
 
bool isPrime(ll n) {
	ll d = n - 1;
	int s = 0;
	while (d % 2 == 0) {
		s++;
		d >>= 1;
	}
	int a[9] = {2, 3, 5, 7, 11, 13, 17, 19, 23};
	for(int i = 0; i < 9; i++) {
		bool comp = fastPow(a[i], d, n) != 1;
		if(comp) 
			for(int j = 0; j < s; j++) {
				ll fp = fastPow(a[i], (1LL << (ll)j)*d, n);
				if (fp == n - 1) {
					comp = false;
					break;
				}
			}
		if(comp) return false;
	}
	return true;
}
ll f(string x, ll b){
	ll sol = 0; ll n = x.length();
	for(ll i = 0; i < n; ++i){
		if(x[i] == '1') sol = (ll) sol + Pow(b, n - i - 1);
	}
	return sol;
}

bool cj(string x){
	for(int i = 2; i < 11; ++i){
		ll p = f(x, i);
		if(isPrime(p)) return false;
	}
	return true;
}

ll div(ll x){
	for(ll i = 2; i*i < x; ++i){
		if(x % i == 0) return i;
	}
}

int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	ll t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		ll n, j; cin>>n>>j;
		ll k = 0;
		vector<int> sol[52];
		vector<string> js;
		ll nSub = 1 << n;
		for(ll i = 0; i < nSub && k < j; i++){
     		string s = bitset<17>(i).to_string().substr(17-n);
			//cout<<s<<endl;
			if(s[0] == '1' && s[s.length() - 1] == '1'){
				//cout<<s<<" "<<cj(s)<<endl;
				if(cj(s)){
					//cout<<s<<endl;
					js.push_back(s);
					for(int i = 2; i < 11; ++i){
						//cout<<"H1 "<<i<<endl;
						ll p = f(s, i);
						//cout<<"H2 "<<p<<" "<<isPrime(p)<<endl;
 						ll d;
						if(p >= 1000000) d = pollard_rho(p);
						else d = div(p);
						//cout<<"H3 "<<i<<endl;
						sol[k].push_back(d);
					}
					++k;
				}
			}
		}
		cout<<"Case #"<<(i+1)<<":\n"; 
		for(int r = 0; r < js.size(); ++r){
			cout<<js[r]<<" ";
			for(int h = 0; h < sol[r].size(); ++h){
				cout<<sol[r][h];
				if(h == sol[r].size() -1) cout<<"\n";
				else cout<<" ";
			}	
		}
	}
	return 0;
}
