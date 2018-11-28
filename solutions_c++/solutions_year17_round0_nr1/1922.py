#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair< ii , int > pii;
#define endl '\n'
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ll long long
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(decltype((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define FASTIO (ios_base::sync_with_stdio(0),cout.tie(0),cin.tie(0))
#define TIME_S clock_t tStart = clock()
#define TIME_E printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC)
const int INF = 1e9;
/*codejam_2017_A*/

string s;
int k, l;

bool chk() {
	REP(i, l) {
		if (s[i] == '-')
			return false;
	}
	return true;
}

void flip(int x) {
	FOR(i, x, x + k) {
		s[i] = (s[i] == '-') ? '+' : '-';
	}
}

int main() {
	FASTIO;
	int t;
	cin >> t;
	REP(c, t) {
		cin >> s >> k;
		l = sz(s);
		int ans = 0;
		REP(i, l - k + 1) {
			if (chk())
				break;
			if (s[i] == '-') {
				ans++;
				flip(i);
			}
		}
		cout << "Case #" << c + 1 << ": ";
		if (chk()) {
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
}
