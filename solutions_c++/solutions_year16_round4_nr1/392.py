#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <string>

using namespace std;

typedef long long i64;

char get_a(string s) {
	if (s[0] == s[1])
		return 'X';
	sort(s.begin(), s.end());
	if (s == "PR")
		return 'P';
	if (s == "PS")
		return 'S';
	return 'R';
}

string perf_step(string s) {
	string res;
	for (int i = 0; i < s.length(); i += 2) {
		char c = get_a(s.substr(i, 2));
		if (c == 'X')
			return "X";
		res.push_back(c);
	}
	return res;
}

void dummy(int t, int n, int p, int r, int s) {
	string st;
	string ans = "IMPOSSIBLE";
	for (int i = 0; i < p; i++)
		st.push_back('P');
	for (int i = 0; i < r; i++)
		st.push_back('R');
	for (int i = 0; i < s; i++)
		st.push_back('S');
	do {
		string cur = perf_step(st);
		while (cur.length() > 1)
			cur = perf_step(cur);
		if (cur != "X") {
			ans = st;
			break;
		}

	} while (next_permutation(st.begin(), st.end()));
	cout << "Case #" << t << ": " << ans << endl;
}

const string res = "PRS";

void solve(vector <int> arr) {
	int sum = arr[0] + arr[1] + arr[2];
	if (sum == 1) {
		for (int i = 0; i < 3; i++)
			if (arr[i])
				cout << res[i];
		return;
	}
	int cur = sum / 2;
	vector <int> now(3);
	for (int i = 0; i < 3; i++) {
		now[i] = cur / (3 - i);
		cur -= now[i];
	}
	vector <int> res;
	do {
		int mi = arr[0] - now[0], ma = arr[0] - now[0];
		for (int i = 0; i < 3; i++) {
			mi = min(mi, arr[i] - now[i]);
			ma = max(ma, arr[i] - now[i]);
		}
		if (ma <= mi + 1)
			res = now;
	} while (next_permutation(now.begin(), now.end()));
	solve(res);
	for (int i = 0; i < 3; i++)
		arr[i] -= res[i];
	solve(arr);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector <int> arr = { p, r, s };

		int mi = arr[0], ma = arr[0];
		for (int i = 0; i < 3; i++) {
			mi = min(arr[i], mi);
			ma = max(arr[i], ma);
		}
		cout << "Case #" << t << ": ";
		if (ma > mi + 1) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		solve(arr);
		cout << endl;
		//dummy(t, n, p, r, s);
	}
}
