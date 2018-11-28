#include <bits/stdc++.h>
using namespace std;
#define sqr(x) ((x) * (x))
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"
#define sync ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define clean(a) memset((a),0,sizeof (a))
#define fin(name) freopen(name, "r", stdin)
#define fout(name) freopen(name, "w", stdout)
typedef pair<int,int> pii;
typedef long long ll;
const int N = 200005;
const int MAX = 1000000007;
const double EPS = 0.000001;
//cout << fixed << setprecision(10);

int n,j,cnt;
ll d;
vector<int> ans;

ll binary(ll n) {
	string s = "";
	while(n) {
		s = (char)((n & (ll)1) + 48) + s;
		n = (n >> (ll)1);
	}
	ll d = (ll)0;
	for(int i = 0;i<(int)s.length();i++)
		d = d * 10 + (s[i] - 48);
	return d;
}

ll make(ll d, int base) {
	ll a = (ll)0;
	ll p = (ll)1;
	while(d) {
		a += (d % (ll)10) * p;
		p *= (ll)base;
		d /= (ll)10;
	}
	return a;
}

int nprost(ll n) {
	int d = 2;
	int q = (int)sqrt(n);
	while(d<=q)
		if (!(n % d))
			return d;
			else d++;
			
	return 0;
}

int main() {
	fin("C.in");
	fout("C.out");
	sync;
	int t;
	cin >> t >> n >> j;
	cnt = 0;
	cout << "Case #1: " << endl;
	for(ll i = ((ll)1 << (ll)(n-(ll)1)) + 1;i < ((ll)1 << (ll)n) && j;i++) {
		d = binary(i);
		if (d % 10) {
			ans.clear();
			bool f = true;
			
			for(int base = 2;base<=10 && f;base++) {
				ans.pb(nprost(make(d,base)));
				if (!ans[(int)ans.size()-1])
					f = false;
			}
			if (!f)
				continue;
			cout << d << " ";
			for(int k = 0;k<(int)ans.size();k++)
				cout << ans[k] << " ";
			cout << endl;
			j--;
		}
	} 
	return 0;
}
