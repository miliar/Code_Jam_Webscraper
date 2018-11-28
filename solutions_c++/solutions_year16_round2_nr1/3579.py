#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const double PI = acos(-1.0);
const double EPS = 1e-8;

int cot[256], tmp[27], path[1000], cur, len;
string num[11] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool dfs(int ch_cot) {
	if (ch_cot == len) {
		return 1;
	}
	for (int i = 0; i < 10; ++i) {
		int tmp[26] = {0};
		for (auto c: num[i]) {
			++tmp[c - 'A'];
		}
		bool flag = 1;
		for (int i = 0; i < 26; ++i) {
			if (cot[i + 'A'] - tmp[i] < 0) {
				flag = 0;
				break;
			}
		}
		if (flag) {
			for (int i = 0; i < 26; ++i) {
				cot[i + 'A'] -= tmp[i];
			}
			path[cur++] = i;
			if (dfs(ch_cot + num[i].size())) {
				return 1;
			}
			--cur;
			for (int i = 0; i < 26; ++i) {
				cot[i + 'A'] += tmp[i];
			}
		}
	}
	return 0;
}

int main() {
#ifdef LOCAL
	//freopen("in", "r", stdin);
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
#endif // LOCAL
	ios::sync_with_stdio(0);
	int t, cas = 0;
	string s;
	cin >> t;
	while (t-- && cin >> s) {
		memset(cot, 0, sizeof cot);
		cur = 0;
		len = s.size();
		for (auto c: s) {
			++cot[c];
		}
		dfs(0);
		sort(path, path + cur);
		cout << "Case #" << ++cas << ": ";
		for (int i = 0; i < cur; ++i) {
			cout << path[i];
		}
		cout << endl;
	}
	return 0;
}
