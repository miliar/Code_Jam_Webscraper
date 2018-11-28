#include <bits/stdc++.h>
#define all(v) v.begin(),v.end()
#define fore(i,a,n) for(int i=a;i<n;i++)
#define rev(i,n) for(int i = n-1; i>= 0; i--)
#define pb push_back
#define mp make_pair
#define dprint(v) cerr << #v " = " << v << endl
#define endl '\n'
#define fill(m,v) memset(m,v,sizeof m)
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
const int N = 100005;
const ll mod = (ll) 1e9 + 7;
ll exp(ll n, ll e) {
	ll r = 1LL;
	for(ll i = 0;i < e ;i++)
		r *= n;
	return r;
}

int main() {
	int test;
	cin >> test;
	
	fore(t,0,test) {
		ll k,c,l;
		cin >> k >> c >> l;
		ll s = exp(k,c-1);
		ll cur = 1LL;
		cout << "Case #" << t+1 << ":";
		fore(i,0,k) {
			cout << " " << cur;
			cur += s;
		}
		cout << endl;
	}
}
