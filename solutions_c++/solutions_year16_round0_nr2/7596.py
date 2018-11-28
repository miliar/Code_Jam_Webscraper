#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mk make_pair
#define pi pair<int, int>
#define fi first
#define se second
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		string s;
		cin >> s;
		int n = s.length();
		int ans = 0;
		char las;
		for(int i = 0; i < n; i++) {
			if(i == 0) {
				if(s[i] == '-') {
					ans++;
				}
			} else {
				if(s[i] == '-' && las == '+') ans += 2;
			}
			las = s[i];
		}
		cout << ans << endl;
	}
	return 0;
}

