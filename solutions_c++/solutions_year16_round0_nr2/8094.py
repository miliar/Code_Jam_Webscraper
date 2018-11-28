#include <bits/stdc++.h>

using namespace std;

void solve(int ind) {
	string s;
	cin >> s;
	int n = s.size();
	int cnt = 1;
	for (int i = 1; i < n; i++)
		cnt += int(s[i - 1] != s[i]);
	int ans = 0;

	if (cnt == 1)
		ans = int(s[0] == '-');
	else if (s[0] == '+') 
		ans = cnt - cnt % 2;
	else
		ans = cnt - 1 + cnt % 2;

	printf("Case #%d: %d\n", ind, ans); 
}

int main() {

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) 
    	solve(i + 1);

	return 0;
}
