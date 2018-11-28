#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

int T;
string s;
int L;

int solve(int idx, int c) {
	if (idx < 0) return 0;
	if (s[idx] == c) {
		return solve(idx - 1, c);
	}
	else {
		return 1 + solve(idx - 1, c == '+' ? '-' : '+');
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("pancake.in", "r", stdin);
	freopen("pancake.out", "w", stdout);

	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> s;
		L = s.size();
		cout << "Case #" << i << ": " << solve(L - 1, '+') << '\n';
	}

	cout.flush();
	return 0;
}
