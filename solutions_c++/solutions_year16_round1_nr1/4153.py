#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int test;
	string s, ans;

	cin >> test;
	for (int t = 0; t < test; t++) {
		ans = "";
		cin >> s;
		for (int i = 0; i < s.length(); i++) {
			if (ans.length() != 0 && s[i] >= ans[0]) ans = s[i] + ans;
			else ans += s[i];
		}
		cout << "Case #" << t+1 << ": " << ans << "\n";
	}

	//system("pause");
    return 0;
}