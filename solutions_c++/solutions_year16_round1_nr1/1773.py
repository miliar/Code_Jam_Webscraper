#include <bits/stdc++.h>

using namespace std;

vector <string> guys;
const int MAXN = 1010;
char c[MAXN];
vector <string> dp;

string read() {
	scanf("%s", c);
	return string(c);
}

int main() {
	freopen("abig.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, cnt = 0;
	scanf("%d", &t);
	while (t--) {
		cnt++;
		string s = read();
		dp.clear();
		dp.resize(s.size());
		for (int i = 0; i < (int) s.size(); i++) {
			if (i > 0) {
				dp[i] = max(dp[i - 1] + s[i], s[i] + dp[i - 1]);
			} else {
				dp[i] = s[i];
			}
		}
		string ans = dp[s.size() - 1];
		printf("Case #%d: %s\n", cnt, ans.c_str());
	}
}
	
