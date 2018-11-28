#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;
#define lli long long int
const int N = 1e8;

int main() {
    ios_base::sync_with_stdio();
	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";
		int k;
		string s;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i < s.length(); ++i) {
			if (s[i] == '-') {
				if (i + k > s.length()) {
					ans = -1;
					break;
				}
				ans++;
				for (int j = 0; j < k; ++j) s[i + j] = (s[i+j] == '-' ? '+' : '-');
			}
		}
		if (ans == -1) cout << "IMPOSSIBLE"; else cout << ans;
		cout << endl;
	}
    return 0;
}