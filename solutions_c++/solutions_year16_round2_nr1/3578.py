#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		
		vector<int> cnt(10);
		string word[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"} ;	
		int n = (int) s.size();
		vector<int> v(30);
		vector<bool> visited(n);
		
		for (char x: s) {
			if (x == 'Z') ++cnt[0];
			if (x == 'W') ++cnt[2];
			if (x == 'U') ++cnt[4];
			if (x == 'X') ++cnt[6];
			if (x == 'G') ++cnt[8];
		}
		
		
		for (int i = 0; i < 10; i += 2) {
			for (char x: word[i]) v[x - 'A'] += cnt[i];
		}
		
		for (int i = 0; i < n; ++i) {
			if (v[s[i] - 'A']) {
				visited[i] = 1;
				--v[s[i] - 'A'];
			}
		}
		
		for (int i = 0; i < n; ++i) {
			if (visited[i]) continue;
			if (s[i] == 'O') ++cnt[1];
			else if (s[i] == 'R') ++cnt[3];
			else if (s[i] == 'F') ++cnt[5];
			else if (s[i] == 'S') ++cnt[7];
		}
		
		
		for (int i = 1; i < 10; i += 2) {
			for (char x: word[i]) v[x - 'A'] += cnt[i];
		}
		
		for (int i = 0; i < n; ++i) {
			if (!visited[i] && v[s[i] - 'A']) {
				visited[i] = 1;
				--v[s[i] - 'A'];
			}
		}
		
		for (int i = 0; i < n; ++i) {
			if (!visited[i]) ++cnt[9];
		}
		
		cnt[9] /= 4;
		
		printf("Case #%d: ", i);
		
		string ans = "";
		for (int i = 0; i < 10; ++i) ans += string(cnt[i], '0' + i);
		cout << ans << '\n';
	}
	return 0;
}