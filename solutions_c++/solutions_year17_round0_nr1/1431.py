#include <bits/stdc++.h>
using namespace std;

string s;
int n, k;

int findAns(string s) {
	int ans = 0;
	for (int i = 0; i <= n - k; i++) {
		if (s[i] == 1)continue;
		for (int j = 0; j < k; j++)
			s[i + j] = 1 - s[i + j];
		ans++;
	}
	
	for (int i = n - k; i < n; i++) {
		if (s[i] == 1) continue;
		return n + 1;
	}
	
	return ans;
}

void solve(int tc) {
	cerr << tc << endl;
	cin >> s >> k;
	n = s.length();
	
	for (int i = 0; i < n; i++) 
		if (s[i] == '+') s[i] = 1;
		else s[i] = 0;
	
	int ans = n + 1;
	ans = min(ans, findAns(s));
	
	for (int i = 0; i < n / 2; i++)
		swap(s[i], s[n - i - 1]);
	
	ans = min(ans, findAns(s));
	
	cout << "Case #" << tc << ": "; 
	if (ans <= n) 
		cout << ans; 
	else 
		cout << "IMPOSSIBLE";
	cout << "\n";
}

int main() {
	int t;
	cin >> t;
	
	for (int tc = 1; tc <= t; tc++) 
		solve(tc);
	
	return 0;
}