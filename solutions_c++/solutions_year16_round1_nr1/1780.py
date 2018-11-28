#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL), cout.precision(15);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		string s; cin >> s;
		string res = string(1, s[0]);
		
		for (int i = 1; i < s.length(); i++) {
			if (s[i] >= res[0]) res = string(1, s[i]) + res;
			else res = res + string(1, s[i]);
		}
		cout << "Case #" << t << ": "<<res << "\n";
	}

	return 0;
}
