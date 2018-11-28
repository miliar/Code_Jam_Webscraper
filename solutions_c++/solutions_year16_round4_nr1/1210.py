#include <bits/stdc++.h>

#define ALL(v) v.begin(), v.end()
#define REP(i, a, b) for (int i = a; i < b; i++)
#define REPD(i, a, b) for (int i = a; i > b; i--)
#define REPLL(i, a, b) for (ll i = a; i < b; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
#define FORD(i, a, b) for (int i = a; i >= b; i--)
#define FORLL(i, a, b) for (ll i = a; i <= b; i++)

using namespace std;

typedef long long ll;
typedef long double ld;

typedef vector<int>::iterator vit;
typedef set<int>::iterator sit;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pii> vpii;
typedef pair<ld, ld> pld;

#define remax(a, b) a = max(a, b)
#define remin(a, b) a = min(a, b)

#define popcount __builtin_popcount
#define pb push_back
#define mp make_pair
#define st first
#define y first
#define nd second
#define x second

#define eps 1e-9
#define pi acos(-1.0)

const int inf = 1e9 + 1;

const int N = 100123;

int z, n;
int r, p, s;

map<char, string> m = { {'P', "PR"}, {'R', "RS"}, {'S', "PS"} };

void solve(int tc) {
	cin >> n;
	cin >> r >> p >> s;

	int res = -1;

	string ss;
	FOR(win, 0, 3) {
		if(win == 1) win++;
		ss = "";
		ss += (char)(win + 'P');
		while(ss.size() < (1<<n)) {
			string t = "";
			
			for(char c : ss) {
				t += m[c];
				//cerr << c << ": " << m[c] << " ";
			}
			//cerr << ss << " " << t << endl;
			ss = t;
		}

		int cnt[4] = {0, 0, 0, 0};
		for(char c : ss) {
			cnt[c-'P']++;
		}
		if(cnt[0] == p && cnt[2] == r && cnt[3] == s) {
			res = win;
			break;
		}

	}
	
		for(int len = 1; len <= ss.size()/2; len *= 2) {
			for(int i = 0; i < ss.size(); i += len*2) {
				string a = ss.substr(i, len);
				string b = ss.substr(i+len, len);;
				if(a > b) {
					REP(j, i, i+len) ss[j] = b[j-i];
					REP(j, i+len, i+2*len) ss[j] = a[j-i-len];
				}
			}
		}

	cout << "Case #" << tc << ": " << (res < 0 ? "IMPOSSIBLE" : ss) << endl;
}

int main() {
  ios_base::sync_with_stdio(0);

  cin >> z;

  FOR(tc, 1, z) solve(tc);
}