/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

vector<char> t;
char s[2000000 + 1];

void solve() {
	gets(s);
	int i;
	t.clear();
	for (i = 0; s[i]; i++) {
		if (t.size() && t.back() == s[i])
			t.pop_back();
		else
			t.push_back(s[i]);
	}
	printf("%d\n", (int)((t.size() * 5 + (i - t.size()) * 10) / 2));
}

int main() {
	int n;
	scanf("%d ", &n);
	for (int i = 1; i <= n; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}
