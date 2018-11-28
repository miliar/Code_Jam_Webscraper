#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

void solve() {
	int n;
	cin >> n;
	{ string dummy; getline(cin, dummy); }
	unordered_map<string, int> mp;
	vector<vector<int>> words;
	for (int i = 0; i < n; ++i) {
		string line;
		getline(cin, line);
		assert(cin);
		vector<int> newwords;
		istringstream is(line);
		string word;
		while (is >> word) {
			auto it = mp.emplace(move(word), int(mp.size()));
			assert(it.first != end(mp));
			newwords.emplace_back(it.first->second);
		}
		words.emplace_back(move(newwords));
	}
	//for (auto m: mp) E(m.first, m.second);
	assert(n <= 20);
	vector<char> typ;
	int ans = numeric_limits<int>::max();
	for (int mask = 0; mask < (1<<n); ++mask) {
		typ.assign(mp.size(), '\0');
		if ((mask & 3) != 2) continue;
		for (int i = 0; i < n; ++i) {
			bool french = (mask & (1<<i)) != 0;
			int bit = french ? 2 : 1;
			for (int w: words[i])
				typ[w] |= bit;
		}
		ans = min(ans, int(count(all(typ), char(3))));
	}
	cout << ans;
}

int main() {
	int tcase;
	cin >> tcase;
	for (int t = 0; t < tcase; ++t) {
		cout << "Case #" << (t + 1) << ": ";
		solve();
		cout << "\n";
	}
	return 0;
}
