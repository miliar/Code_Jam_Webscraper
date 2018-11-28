#include <bits/stdc++.h>

#define debug(x)
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;

int N, R, P, S;
string current = "";

inline char wins(char c) {
	if(c == 'R') {
		return 'S';
	}
	if(c == 'S') {
		return 'P';
	}
	return 'R';
}

void roll(char cur, int level) {
	if(level == N) {
		current.push_back(cur);
		return;
	}
	roll(cur, level + 1);
	roll(wins(cur), level + 1);
}

inline string bagulho(string s) {
	debug(s);
	int tam = 0;
	int jump = 2;
	while(tam < N) {
		for(int i = 0; i < (int) s.size(); i += jump) {
			if(s.substr(i, 1 << tam) > s.substr(i + (1 << tam), (1 << tam))) {
				for(int j = i; j < i + (1 << tam); j++) {
					debug(j);
					debug(s[j]);
					debug(j + (1 << tam));
					debug(s[j + (1 << tam)]);
					swap(s[j], s[j + (1 << tam)]);
				}
			}
		}
		jump <<= 1;
		tam++;
	}
	debug(s);
	return s;
}

int main() {
	ios_base::sync_with_stdio(false);
	
	int t;
	cin >> t;
	int kase = 1;
	while(t--) {
		cin >> N >> R >> P >> S;
		vector<string> v;
		vector<char> chars {'R', 'S', 'P'};
		for(auto &each : chars) {
			current = "";
			roll(each, 0);
			v.push_back(current);
		}
		bool deu_bom = false;;
		string ans = "";
		for(auto &each : v) {
			map<char, int> m;
			for(auto &each_each : each) {
				m[each_each]++;
			}
			if(m['R'] == R && m['S'] == S && m['P'] == P) {
				deu_bom = true;
				string cur = bagulho(each);
				if(ans == "") {
					ans = cur;
				}
				else {
					ans = min(ans, cur);
				}
			}
		}
		cout << "Case #" << kase++ << ": ";
		if(deu_bom) {
			cout << ans << '\n';
		}
		else {
			cout << "IMPOSSIBLE" << '\n';
		}
	}
	return 0;
}
