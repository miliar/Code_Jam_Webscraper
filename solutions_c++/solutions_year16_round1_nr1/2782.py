#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		string S;
		cin >> S;
		vector<char> largest(S.size());
		largest[S.size()-1] = S.back();
		for (int i = S.size()-2; i >= 0; --i) {
			largest[i] = max(largest[i+1], S[i]);
		}
		string ans = S.substr(0, 1);
		for (int i = 1; i < S.size(); ++i) {
			if (S[i] >= ans.front())
				ans = S.substr(i,1) + ans;
			else
				ans.push_back(S[i]);
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
