#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

int T;
int K, C, S;

string solve() {
	string s = "";
	for (int i = 1; i <= S; i++) {
		s += to_string(i);
		if (i != S) s += ' ';
	}
	return s;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("fractiles.in", "r", stdin);
	freopen("fractiles.out", "w", stdout);

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> K >> C >> S;
		cout << "Case #" << tc << ": " << solve() << '\n';
	}

	cout.flush();
	return 0;
}
