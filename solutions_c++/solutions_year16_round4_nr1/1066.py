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

int N, R, P, S;

bool good(const string& lineup) {
	//DEBUG(lineup);
	if (LEN(lineup) == 1) return true;
	string next_lineup;
	for (int i=0; i<LEN(lineup); i+=2) {
		if (lineup[i] == lineup[i+1]) return false;
		if ((lineup[i] == 'S' && lineup[i+1] == 'P') ||
			(lineup[i] == 'P' && lineup[i+1] == 'R') ||
			(lineup[i] == 'R' && lineup[i+1] == 'S'))
			next_lineup.push_back(lineup[i]);
		else next_lineup.push_back(lineup[i+1]);
	}
	return good(next_lineup);
}

void solve_small() {
	
	//DEBUG(good("PSRS"));
	
	cin >> N >> R >> P >> S;
	
	if (max(abs(P-R), max(abs(P-S), abs(R-S))) > 1) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	
	string lineup;
	FOR(i,0,P) lineup.push_back('P');
	FOR(i,0,R) lineup.push_back('R');
	FOR(i,0,S) lineup.push_back('S');
	
	//cout << max(abs(P-R), max(abs(P-S), abs(R-S))) << " : ";
	
	do {
		if (good(lineup)) {
			cout << lineup << endl;
			return;
		}
		
	} while (next_permutation(ALL(lineup)));
}

typedef tuple<int,int,int> tiii;

pair<tiii, tiii> split(const tiii& players) {
	int p, r, s;
	p = get<0>(players)/2;
	r = get<1>(players)/2;
	s = get<2>(players)/2;
	
	int pm, rm, sm;
	pm = get<0>(players)%2;
	rm = get<1>(players)%2;
	sm = get<2>(players)%2;
	
	int p1 = p;
	int p2 = p;
	int r1 = r;
	int r2 = r;
	int s1 = s;
	int s2 = s;
	
	if (pm && rm) { p1++; r2++; }
	if (pm && sm) { p1++; s2++; }
	if (rm && sm) { r1++; s2++; }
	
	return make_pair(make_tuple(p1,r1,s1), make_tuple(p2,r2,s2));
}

int summ(const tiii& players) {
	int p, r, s;
	tie(p,r,s) = players;
	return p + r + s;
}

string get_lineup(const tiii& players) {
	if (summ(players) == 2) {
		string ret;
		if (get<0>(players)) ret.push_back('P');
		if (get<1>(players)) ret.push_back('R');
		if (get<2>(players)) ret.push_back('S');
		return ret;
	}
	auto splitt = split(players);
	return get_lineup(splitt.first) + get_lineup(splitt.second);
}

void solve() {
	cin >> N >> R >> P >> S;
	
	if (max(abs(P-R), max(abs(P-S), abs(R-S))) > 1) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	
	tiii players = make_tuple(P, R, S);
	cout << get_lineup(players) << endl;
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
