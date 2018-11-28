#include <iostream>
#include <string>
using namespace std;

char arr[10000];
int n, x, y, z;

string dfs(int m, int u, int p) {
	if (m == 0) {
		if (u == 0)
			return "R";
		if (u == 1)
			return "P";
		return "S";
	}
	
	string ans1 = dfs(m - 1, u, p * 2);
	string ans2 = dfs(m - 1, (u + 2) % 3, p * 2 + 1);

	if (ans1 < ans2) return ans1 + ans2;
	return ans2 + ans1;
}

bool check(string s) {
	int xx = 0, yy = 0, zz = 0;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == 'R')
			xx++;
		if (s[i] == 'P')
			yy++;
		if (s[i] == 'S')
			zz++;
	}

	return (x == xx && y == yy && z == zz);
}

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cin >> n >> x >> y >> z;
		string ans1 = dfs(n, 0, 1);
		string ans2 = dfs(n, 1, 1);
		string ans3 = dfs(n, 2, 1);

		cout << "Case #" << t << ": ";
		if (check(ans1))
			cout << ans1;
		else
			if (check(ans2))
				cout << ans2;
			else
				if (check(ans3))
					cout << ans3;
				else
					cout << "IMPOSSIBLE";
		cout << endl;
	}
}