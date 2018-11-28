#include <bits/stdc++.h>
using namespace std;

void solve(){
	string s;
	cin >> s;

	int cnt = 0;
	while (true) {
		bool happy = true;

		for (int i = s.length() - 1; i >= 0; i--) {
			if (s[i] == '-') {
				happy = false;
				if (s[0] == '-') {
					string t = "";
					for (int j = i; j >= 0; j--) {
						if (s[j] == '-') {
							t.push_back('+');
						}
						else {
							t.push_back('-');
						}
					}
					for (int j = i + 1; j < s.length(); j++) {
						t.push_back('+');
					}
					s = t;
					cnt++;
					break;
				}
				else {
					string t = "";
					int k = 0;
					for (int j = 0; j <= i; j++) {
						if (s[j] == '-') {
							k = j;
							break;
						}
					}
					for (int j = i; j >= k; j--) {
						if (s[j] == '-') {
							t.push_back('+');
						}
						else {
							t.push_back('-');
						}
					}
					for (int j = k - 1; j >= 0; j--) {
						if (s[j] == '-') {
							t.push_back('-');
						}
						else {
							t.push_back('+');
						}
					}
					for (int j = i + 1; j < s.length(); j++) {
						t.push_back('+');
					}
					s = t;
					cnt += 2;
					break;
				}
			}
		}

		if (happy) {
			break;
		}
	}
	cout << cnt;
}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
