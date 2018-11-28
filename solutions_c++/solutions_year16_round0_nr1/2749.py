#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

long long T, N;

string solve() {
	if (N == 0) return "INSOMNIA";
	bool looked[10];
	memset(looked, false, sizeof looked);
	long long c = N;
	while (c < (1<<30)) {
		string s = to_string(c);
		for (char c : s) {
			looked[c - '0'] = true;
		}
		bool bad = false;
		for (long long i = 0; i < 10; i++) {
			if (looked[i] == false) {
				bad = true;
				break;
			}
		}
		if (!bad)
			return s;
		c += N;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("sheep.in", "r", stdin);
	freopen("sheep.out", "w", stdout);

	cin >> T;
	for (long long i = 0; i < T; i++) {
		cin >> N;
		cout << "Case #" << i + 1 << ": " << solve() << '\n';
	}

	cout.flush();
	return 0;
}
