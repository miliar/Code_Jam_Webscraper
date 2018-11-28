#include <queue>
#include <string>
#include <string.h>
#include <iostream>

using namespace std;

struct Pancake
{
	Pancake(string s, int n) {
		this->s = s;
		this->nFlips = n;
	}

	string s;
	int nFlips;
};

bool vis[2048];

int toInt(string s)
{
	int p = 0;
	for (int i = 0; i < s.length(); i++) {
		p <<= 1;
		if (s[i] == '-') p |= 1;
	}

	return p;
}

string flip(string s, int n)
{
	string r = s;

	for (int i = 0; i < n; i++) {
		if (s[n - 1 - i] == '+') r[i] = '-';
		else r[i] = '+';
	}

	return r;
}

int solve(string s)
{
	int minFlips;

	queue<Pancake> Q;
	Q.push(Pancake(s, 0));

	memset(vis, 0, sizeof(vis));
	vis[toInt(s)] = true;
	if (vis[0]) return 0;

	while (!vis[0]) {
		Pancake p = Q.front(); Q.pop();

		for (int n = 1; n <= s.length(); n++) {
			string r = flip(p.s, n);
			int v = toInt(r);
			if (vis[v]) continue;

			vis[v] = true;
			if (v == 0) {
				minFlips = p.nFlips + 1;
				break;
			}
			Q.push(Pancake(r, p.nFlips + 1));
		}
	}

	return minFlips;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		cout << "Case #" << t << ": " << solve(s) << endl;
	}

	return 0;
}

