#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string digits[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int dc[10][32];
int idc[32];
int main() {
	int tests;
	string input, ans;

	for (int d = 0; d < 10; ++d) {
		for (int i = 0; i < digits[d].size(); ++i) {
			dc[d][digits[d][i] - 'A']++;
		}
	}


	cin >> tests;
	for (int case_no = 1; case_no <= tests; ++case_no) {
		cin >> input;
		ans = "";
		int last = 0;
		for (int i = 0; i < 26; ++i) idc[i] = 0;
		for (int i = 0; i < input.size(); ++i) {
			idc[input[i] - 'A']++;
		}

		int order[] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};

		for (int x = 0; x < 10; ++x) {
			int i = order[x];
			int max_possible = 2001;
			for (int j = 0; j < 26; ++j) {
				if (idc[j] < dc[i][j]) {
					max_possible = 2001;
					break;
				}
				if (dc[i][j] == 0) continue;
				max_possible = min(max_possible, idc[j] / dc[i][j]);
			}
			if (max_possible == 2001)
				continue;
			for (int j = 0; j < max_possible; ++j) {
				ans += (char) (i + '0');
				for (int k = 0; k < 26; ++k)
					idc[k] -= dc[i][k];
			}
		}
		sort(ans.begin(),ans.end());
		string ans_r = "";
		for (int i = 0; i < ans.size(); ++i) {
			ans_r += digits[ans[i] - '0'];
		}
		sort(ans_r.begin(),ans_r.end());
		sort(input.begin(),input.end());
		if (input != ans_r)
			cout << input << " " << ans_r << " BAD! " << endl;
		cout << "Case #" << case_no << ": " << ans << endl;
	}
}