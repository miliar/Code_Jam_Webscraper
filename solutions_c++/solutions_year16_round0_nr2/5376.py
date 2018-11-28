#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

string flip(const string& s, int i) {
	string res;
	for (int l = i-1; l >= 0; --l) res += s[l];
	for (int l = i; l < s.size(); ++l) res += s[l];

	return res;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		string s;
		cin >> s;
		int costPlus[200] = {0}, costMinus[200] = {0};
		for (int l = 0; l < s.size(); ++l) {
			if (s[l] == '+') {
				costPlus[l+1] = min(costPlus[l], costMinus[l] + 1);
				costMinus[l+1] = costPlus[l] + 1;
			} else {
				costPlus[l+1] = costMinus[l] + 1;
				costMinus[l+1] = min(costMinus[l], costPlus[l] + 1);
			}
		}

		int res = min(costPlus[s.size()], 1 + costMinus[s.size()]);
		cout << "Case #" << i << ": " << res << endl;
	}

	return 0;
}
