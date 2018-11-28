#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


int main() {
#ifdef LOCAL
	freopen("in", "r", stdin);
	freopen("out1", "w", stdout);
#endif // LOCAL
	ios::sync_with_stdio(0);
	int t, s, cas = 0;
	string str;
	cin >> t;
	while(t-- && cin >> s >> str) {
		int cot = 0, ans = 0;
		for(int i = 0; i <= s; ++i) {
			for(int j = 0; j < str.at(i) - '0'; ++j) {
				if(cot >= i) {
					++cot;
				}
				else {
					ans += i - cot;
					cot += i - cot + 1;
				}
			}
		}
		cout << "Case #" << ++cas << ": " << ans << endl;
	}
	return 0;
}
