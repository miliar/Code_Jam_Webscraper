#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

#define MAXN 14

int N, R, P, S;
string dp[MAXN][26];
char ccc[3] = {'P', 'R', 'S'};
int cnt[3];

char win(char a, char b) {
	if (a != 'R' && b != 'R') {
		return 'S';
	}
	if (a != 'S' && b != 'S') {
		return 'P';
	}
	return 'R';
}

char loser(char a) {
	if (a == 'R') {
		return 'S';
	}
	if (a == 'S') {
		return 'P';
	}
	return 'R';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	freopen("showdown.in", "r", stdin);
	freopen("showdown.out", "w", stdout);

	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		cout << "Case #" << tc << ": ";
		cin >> N >> R >> P >> S;
		dp[0]['R' - 'A'] = "R";
		dp[0]['P' - 'A'] = "P";
		dp[0]['S' - 'A'] = "S";
		for (int i = 1; i <= N; i++) {
			for (char c : ccc) {
				string r = dp[i - 1][loser(c) - 'A'];
				string s = dp[i - 1][c - 'A'];
				string foo = r + s;
				string bar = s + r;
				if (foo < bar) {
					dp[i][c - 'A'] = foo;
				}
				else {
					dp[i][c - 'A'] = bar;
				}
			}
		}

		// for (int i = 1; i <= N; i++) {
		// 	for (char c : ccc) {
		// 		error(i, c, dp[i][c - 'A']);
		// 	}
		// }

		bool goood = false;
		for (char c : ccc) {
			memset(cnt, 0, sizeof cnt);
			string s = dp[N][c - 'A'];
			for (char k : s) {
				if (k == 'R') {
					cnt[0]++;
				}
				if (k == 'P') {
					cnt[1]++;
				}
				if (k == 'S') {
					cnt[2]++;
				}
			}
			// error(s);
			if (cnt[0] == R && cnt[1] == P && cnt[2] == S) {
				cout << s << endl;
				goood = true;
				break;
			}
		}
		if (!goood) {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
