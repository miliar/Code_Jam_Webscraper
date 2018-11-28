#include <iostream>
#include <fstream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

#define pb push_back
#define mp make_pair

using namespace std;

int T;
string s, ans, ansW;
map <char, string> toWord;

void init() {
	toWord['0'] = "ZERO";
	toWord['1'] = "ONE";
	toWord['2'] = "TWO";
	toWord['3'] = "THREE";
	toWord['4'] = "FOUR";
	toWord['5'] = "FIVE";
	toWord['6'] = "SIX";
	toWord['7'] = "SEVEN";
	toWord['8'] = "EIGHT";
	toWord['9'] = "NINE";
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin); freopen("output.out", "w", stdout);

	init();
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		cin >> s;
		sort(s.begin(), s.end());
		ans = "0";
		while (true) {
			ansW = "";
			for (int i = 0; i < ans.size(); ++i)
				ansW += toWord[ans[i]];
			sort(ansW.begin(), ansW.end());
			if (ansW == s) {
				cout << "Case #" << t << ": " << ans << endl;
				break;
			}
			int i = ans.size() - 1;
			while (ans[i] == '9') {
				--i;
				if (i == -1)
					break;
			}
			if (i == -1) 
				ans = string(ans.size() + 1, '0');
			else {
				++ans[i];
				for (int j = i + 1; j < ans.size(); ++j)
					ans[j] = ans[i];
			}
		}
	}

	return 0;
}