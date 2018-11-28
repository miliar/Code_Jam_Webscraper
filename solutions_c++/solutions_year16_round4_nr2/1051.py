#include <bits/stdc++.h>
using namespace std;

#define DEBUG_ON 1 // 0 = off, 1 = on

namespace {
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define LEN(x) (int)((x).size())
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define OP minmax

#define FOR(i, begin, end)						\
  for (__typeof(end) i = (begin) - ((begin) > (end));			\
       i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#ifndef ONLINE_JUDGE
#include "debug.h"
#endif // ONLINE_JUDGE

typedef long long int ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<ll> vll;
template <typename T> using min_pq = priority_queue<T, vector<T>, greater<T>>;

ll expmod(ll a, ll b, ll mod) { ll res = 1; a %= mod; for (; b; b >>= 1) { if (b & 1) res = res * a % mod; a = a * a % mod; } return res; }
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
}

const int MAX_N = 200000;
const ll MODD = 1000000009LL;
const ld EPS = 1e-9;

int N, K;
vector<ld> P;

vector<ld> get_subset(const vector<bool>& subset) {
	vector<ld> res;
	FOR(i,0,N) if (subset[i]) res.push_back(P[i]);
	return res;
}

ld get_probability(const vector<bool>& ss) {
	vector<ld> subset = get_subset(ss);
	
	vector<bool> votes_yes(K);
	fill(votes_yes.begin(), votes_yes.begin() + K/2, true);
	sort(ALL(votes_yes));
	
	ld prob = 0;
	do {
		ld cur = 1;
		FOR(i,0,K) {
			if (votes_yes[i]) cur *= subset[i];
			else cur *= (1 - subset[i]);
		}
		prob += cur;
		//DEBUG(votes_yes, cur);
	} while(next_permutation(ALL(votes_yes)));
	
	return prob;
}

void solve() {
	cin >> N >> K;
	P.resize(N);
	FOR(i,0,N) cin >> P[i];
	
	ld best = 0;
	vector<bool> subset(N);
	fill(subset.begin(), subset.begin()+K, true);
	sort(ALL(subset));
	
	do {
		//DEBUG(subset);
		ld pr = get_probability(subset);
		//DEBUG(pr);
		best = max(best, pr);
	} while (next_permutation(ALL(subset)));
	
	cout << fixed << setprecision(8) << best << endl;
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  int T = 0;
  cin >> T;
  
  for (int t = 1; t <= T; t++) {
    cout << "Case #" << t << ": ";
    solve();
  }
}
