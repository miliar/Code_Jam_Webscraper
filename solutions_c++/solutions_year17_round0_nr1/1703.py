#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

string s;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int NumberOfTestCases;
	cin >> NumberOfTestCases;
	for(int TC = 1; TC <= NumberOfTestCases; TC++) {
		cout << "Case #" << TC << ": ";
		int k, n, cnt = 0;
		cin >> s >> k;
		n = s.size();
		for(int i=0; i<=n-k; i++) {
			if(s[i] == '-') {
				cnt++;
				for(int j=0; j<k; j++) {
					if(s[i+j] == '+') s[i+j] = '-';
					else s[i+j] = '+';
				}
			}
		}
		bool flag = 0;
		for(int i=n-k+1; i<n; i++) if(s[i] == '-') {
			flag = 1;
			break;
		}
		if(flag) cout << "IMPOSSIBLE" << endl;
		else cout << cnt << endl;
	}
	return 0;
}