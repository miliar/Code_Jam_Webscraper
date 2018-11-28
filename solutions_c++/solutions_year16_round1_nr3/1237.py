#include <bits/stdc++.h>
using namespace std;

#define DEBUG_ON 1  // 0 = off, 1 = on

namespace {
#define ALL(x) (x).begin(),(x).end()
#define RALL(x) (x).rbegin(),(x).rend()
#define LEN(x) (int)((x).size())
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define OP minmax

#define FOR(i, begin, end)  \
  for (__typeof(end) i = (begin) - ((begin) > (end));  \
       i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#ifndef ONLINE_JUDGE
#include "debug.h"
#endif  // ONLINE_JUDGE
  
typedef long long int ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<ll> vll;
template<typename T> using min_pq = priority_queue<T, vector<T>, greater<T>>;

ll expmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}
}

const int MAX_N = 200000;
const ll MODD = 1000000009LL;
const ld EPS = 1e-9;

vi subset(vi& F, int sub) {
	vi ss;
	for (int i=0; i<(int)F.size(); i++) {
		if (sub & (1 << i)) ss.push_back(F[i]);
	}
	return ss;
}

bool valid(vi& F, vi& circle) {
	int n = (int)circle.size();
	for (int i=0; i < n; i++) {
		if (!(circle[(i-1+n)%n] == F[circle[i]] || circle[(i+1+n)%n] == F[circle[i]])) {
			return false;
		}
	}
	return true;
}

void solve() {
	int N; cin >> N;
	vi F(N);
	FOR(i,0,N) { cin >> F[i]; F[i]--; }
	int ans = 0;
	vi kids(N);
	iota(ALL(kids), 0);
	
	for (int sub=1; sub < (1 << N); sub++) {
		vi ss = subset(kids, sub);
		sort(ALL(ss));
		do {
			if (valid(F, ss)) ans = max(ans, (int)ss.size());
		} while (next_permutation(ALL(ss)));
	}
	
	cout << ' ' << ans << endl;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int T; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ":";
		solve();
	}
}
