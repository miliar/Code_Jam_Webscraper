#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back
#define has(c,i) ((c).find(i) != (c).end())
#define DBG(...) ({ if(1) fprintf(stderr, __VA_ARGS__); })
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

string line;
int TC;
int N;

int main() {
	ios::sync_with_stdio(false);

	getline(cin, line);
	TC = stoi(line);
	FOR(tc, 1, TC+1) {
		getline(cin, line);
		N = stoi(line);

		map<string, int> LUT;

		vector<vi> input;
		FOR(n,0,N) {
			getline(cin, line);
			stringstream ss (line);

			input.pb(vi());
			string word;
			while (ss >> word) {
				if (!has(LUT, word))
					LUT[word] = sz(LUT)-1;
				input.back().pb(LUT[word]);
			}
		}

		int res = oo;
		FOR(bm, 0, (1<<N)) {
			if ((bm & 3) != 2) continue;
			vi prop (sz(LUT), 0);
			FOR(r,0,N) {
				int lang = ((1<<r) & bm) ? 1 : 2;
				for (int w : input[r])
					prop[w] |= lang;
			}
			int cur = 0;
			for (int l : prop)
				if (l == 3)
					cur++;

			res = min(res, cur);
		}

		printf("Case #%d: %d\n", tc, res);
	}
}
