#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int main() {
	freopen("input1.txt", "r", stdin);
	freopen("output1.txt", "w", stdout);
	int i, j, n, t, ans, p = 1;
	string s;
	cin >> t;
	while (t--) {
		ans = 0;
		s = "";
		cin >> n >> s;
		j = (s[0] - '0');
		for (i = 1; i <= n; i++) {
			if (j < i && s[i] != '0') {
				ans += (i - j);
				j = i;
			}
			j += (s[i] - '0');
		}
		cout << "Case #" << p << ": " << ans << endl;
		p++;
	}
	return 0;
}