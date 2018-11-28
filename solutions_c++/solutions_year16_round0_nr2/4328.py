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
int arr[1111];
int main(){

	freopen("B1.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int t;
	cin >> t;
	int c = 0;
	string s;
	while(t--){
		++c;
		cin >> s;
		rep(i, sz(s)){
			if (s[i]=='+') arr[i]=1;
			else arr[i]=0;
		}
		int ans = 0;
		while(true){
			int idx = sz(s);
			rep(i, sz(s)){
				if (!arr[i]) idx=i;
			}
			if (idx==sz(s)) break;
			++ans;
			int l,r;
			l=0,r=idx;
			while(l<=r){
				arr[l] = (arr[l]==1?0:1);
				if (r!=l) 
					arr[r] = (arr[r]==1?0:1);
				++l,--r;
			}
		}
		cout <<"Case #"<<c<<": "<< ans <<"\n";
	}

	return 0;
}