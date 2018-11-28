/* sidchelseafan */
#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define sz(a) (int)a.size()
#define pii pair<int,int>
#define pll pair<ll,ll>

//Hardware Instructions
#define bitcount __builtin_popcount
#define gcd __gcd

//Trasersal Macros
#define rep(i,n) for(int i=0, _##i=(n); i<_##i; ++i)
#define dwn(i,n) for(int i=(n); --i>=0; )
#define repr(i,l,r) for(int i=(l), _##i=(r); i<_##i; ++i)
#define dwnr(i,l,r) for(int i=(r), _##i=(l); --i>=_##i; )
#define repi(i,a) for(__typeof((a).begin()) i=(a).begin(), _##i=(a).end(); i!=_##i; ++i)
#define dwni(i,a) for(__typeof((a).rbegin()) i=(a).rbegin(), _##i=(a).rend(); i!=_##i; ++i)
#define all(a) a.begin(),a.end()
#define fill(a,s) memset(a,s,sizeof(a));
#define ff first
#define ss second
#define abs(x) (x<0?(-x):x)

using namespace std;
const ll MX=100000;
const ll MOD = 1000000007;
ll fast_exp(ll base,ll exp,ll mod){
  ll res=1;
  while(exp > 0){
    if (exp%2==1)res=(res*base)%mod;
    base = (base*base)%mod;
    exp/=2;
   }
  return res;
}
int main(){

	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	int t, n;
	cin >> t;
	int c = 0;
	while(t--){
		cin >> n;
		++c;
		if (n==0) cout <<"Case #"<< c <<": "<<"INSOMNIA\n";
		else{
			set<int> s;
			ll i = 0;
			ll num;
			while(1){
				num = (i + 1)*n;
				ll cpy = num;
				while(cpy){
					s.insert(cpy%10);
					cpy /= 10;
				}
				if (s.size() == 10) break;
				++i;
			}
			cout << "Case #"<<c<<": "<< num <<"\n";
		}
	}

	return 0;
}