#include <bits/stdc++.h>
using namespace std;
int j = 0, tc = 0;
void solver();
int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	solver();
}
void solver() {
	cin >> tc;
	while (tc--) {
		j++;
		string s;
		cin >> s;
		int i = 0, cnt = 0;
		while (i < (int) s.length() - 1) {
			if (s[i] != s[i + 1])
				cnt++;
			i++;
		}
		if (s[s.length() - 1] == '-')
			cnt++;
		cout << "Case #" << j << ": " << cnt << endl;
	}

}
