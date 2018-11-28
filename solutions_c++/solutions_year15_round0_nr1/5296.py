#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	int kase = 1;
	cin >> t;
	while (t --) {
		int n;
		string s;
		cin >> n >> s;
		int cnt = 0;
		int ret = 0;
		for (int i=0; i<=n; i++) {
			if (cnt < i && s[i] > '0') {
				int diff = i - cnt;
				ret += diff;
				cnt += diff;
			}
			cnt += s[i] - '0';
		}
		cout << "Case #" << kase++ << ": " << ret << endl;
	}
	return 0;
}
