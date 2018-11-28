#include <bits/stdc++.h>

using namespace std;

#define MAXN 22
#define INF 100000000

int T, N;
string line;
unordered_set<int> O[2];
vector<int> S[MAXN];
unordered_map<string, int> idx;
int crtIdx;

vector<string> readSentence() {
	getline(cin, line);
	stringstream ss(line);
	string w;
	vector<string> ret;
	while (ss >> w) {
		ret.push_back(w);
	}
	return ret;
}

unordered_set<int> W[2];
int solve() {
	int ans = INF;
	for (int mask = 0; mask < (1 << N); mask++) {
		W[0].clear();
		W[1].clear();
		int crt = 0;
		for (int i = 0; i < N; i++) {
			int t = -1;
			if (mask & (1 << i)) { // E
				t = 0;
			} else { // F
				t = 1;
			}
			for (int s : S[i]) {
				if (W[t].count(s) == 0 && O[t].count(s) == 0) {
					W[t].insert(s);
					if (W[1 - t].count(s) > 0 || O[1 - t].count(s) > 0) {
						crt++;
					}
				}
			}
		}
		ans = min(ans, crt);
	}
	for (int s : O[0]) {
		if (O[1].count(s) > 0) {
			ans++;
		}
	}
	return ans;
}

int get(string str) {
	if (idx.count(str) == 0) {
		idx[str] = crtIdx++;
	}
	return idx[str];
}

int main() {
	freopen("date.in", "r", stdin);
	freopen("date.out","w", stdout);
	cin.sync_with_stdio(false);
	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		N -= 2;
		O[0].clear();
		O[1].clear();
		idx.clear();
		crtIdx = 0;
		getline(cin, line);
		vector<string> aux = readSentence();
		for (auto it : aux) {
			O[0].insert(get(it));
		}
		aux = readSentence();
		for (auto it : aux) {
			O[1].insert(get(it));
		}
		for (int i = 0; i < N; i++) {
			aux = readSentence();
			S[i].clear();
			for (auto it : aux) {
				S[i].push_back(get(it));
			}
		}
		int ans = solve();
		cout << "Case #" << t << ": " << ans << '\n';
		cerr << "Test === " << t << '\n';
	}
	
	return 0;
}
