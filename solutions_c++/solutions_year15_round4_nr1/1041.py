#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(int R, int C, string *s) {
	int ans = 0;
	for (int y = 0; y < R; y++) {
		for (int x = 0; x < C; x++) {
			if (s[y][x] != '.') {
				int ok = 0;
				bool nochange = false;
				for (int i = 1; y-i >= 0; i++) {
					if (s[y-i][x] != '.') {
						ok++;
						if (s[y][x] == '^') nochange = true;
						break;
					}
				}
				for (int i = 1; y+i < R; i++) {
					if (s[y+i][x] != '.') {
						ok++;
						if (s[y][x] == 'v') nochange = true;
						break;
					}
				}
				for (int i = 1; x-i >= 0; i++) {
					if (s[y][x-i] != '.') {
						ok++;
						if (s[y][x] == '<') nochange = true;
						break;
					}
				}
				for (int i = 1; x+i < C; i++) {
					if (s[y][x+i] != '.') {
						ok++;
						if (s[y][x] == '>') nochange = true;
						break;
					}
				}
				if (ok == 0)
					return -1;
				if (!nochange)
					ans++;
			}
		}
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int R, C;
		cin >> R >> C;
		string s[110];
		for (int y = 0; y < R; y++) {
			cin >> s[y];
		}
		int ans = solve(R, C, s);
		cout << "Case #" << i+1 << ": ";
		if (ans < 0)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << endl;
	}
}
