#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
#define GCD(a,b) __gcd(a, b)
#define mp make_pair
#define DEBUG(x) cout << x << "\n"
#define ALL(x) x.begin(), x.end()
#define INF (1 << 30)
#define pb push_back

int T, SMax;
string S;
int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cin >> SMax >> S;
		int ppl_cnt = 0, needed = 0;
		for (int i = 0; i <= SMax; ++i) {
			int newPpl = (S[i] - '0');
			if (i == 0)
				ppl_cnt += newPpl;
			else {
				int req = i;
				int newPpl = (S[i] - '0');
				if (newPpl == 0) continue;
				if (ppl_cnt >= req) {
					ppl_cnt += newPpl;
				}
				else {
					needed += req - ppl_cnt;
					ppl_cnt += needed;
					ppl_cnt += newPpl;
				}
			}
		}
		cout << "Case #" << tc << ": " << needed << '\n';
	}
}