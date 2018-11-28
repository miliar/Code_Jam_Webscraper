// Headers 
#include<bits/stdc++.h>
using namespace std;
// Global declarations
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
typedef pair<ll, ll> pll;
const int mod = 1e9 + 7;
const int INF = 1 << 29;
// Macros
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else 
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

inline bool p(ll n){
	if (n == 1)
		return false;
	for (ll i = 2; i*i <= n; ++i){
		if ((n%i) == 0)
			return false;
	}
	return true;
}

bool ok(ll mask, vector<ll> &vv){
	for (ll base = 2; base <= 10; ++base){
		ll num = 0;
		ll msk = mask;
		ll fct = 1;
		while (msk){
			num = num + 1ll * fct*(msk & 1);
			fct *= base;
			msk >>= 1ll;
		}
		if (p(num))
			return false;
		vv.push_back(num);
	}
	return true;
}

void print(ll mask, vector<ll> &vv){
	stack<ll>s;
	while (mask){
		s.push(mask & 1);
		mask >>= 1;
	}
	while (!s.empty()){
		ll val = s.top();
		s.pop();
		out(val);
	}
	sp;
	tr(vv, it){
		ll num = *it;
		for (ll i = 2; i*i <= num; ++i){
			if ((num%i) == 0){
				out(i); sp;
				break;
			}
		}
	}
	el;
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	ll t;
	inl(t);
	ll cs = 1;
	while (t--){	
		ll len, j;
		inl(len); inl(j);
		printf("Case #%lld:\n", cs++);
		len -= 2;
		ll MX = 1ll << len;
		for (ll mask = 0; mask < MX; ++mask){
			ll mask1 = MX;
			mask1 |= mask;
			mask1 <<= 1;
			++mask1;
			vector<ll> vv;
			if (ok(mask1, vv)){
				//cout << ++tot << ".   ";			
				print(mask1, vv);
				--j;
				if (!j)break;
			}
		}
	}
	return 0;
}