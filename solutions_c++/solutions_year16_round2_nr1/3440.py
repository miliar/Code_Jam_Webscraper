#include <iostream>
#include <map>
using namespace std;

string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool solve (int *count, int ind, string &ans) {
	bool flag = true;
	int size = nums[ind].length();
	for (int j = 0; j < size; j++) {
		count[(nums[ind][j] - 'A')]--;
		if (count[(nums[ind][j] - 'A')] < 0) {
			flag = false;
		}
	}
	if (flag) {
		ans = ans + (char)('0'+ind);
		bool tflag = true;
		for (int j = 0; j < 26; j++) {
			if (count[j] != 0) {
				tflag = false;
				break;
			}
		}
		if (tflag) {
			return true;
		}
		for (int i = ind; i < 10; i++) {
			if (solve (count, i, ans)) {
				return true;
			}
		}
		ans.pop_back ();
		for (int j = 0; j < size; j++) {
			count[(nums[ind][j] - 'A')]++;
		}
		return false;
	} else {
		for (int j = 0; j < size; j++) {
			count[(nums[ind][j] - 'A')]++;
		}
		for (int i = ind+1; i < 10; i++) {
			if (solve (count, i, ans)) {
				return true;
			}
		}
		return false;
	}
}

int main () {
	int t;
	cin >> t;
	for (int casei = 1; casei <= t; casei++) {
		string data;
		cin >> data;
		int count[26];
		for (int i = 0; i < 26; i++) {
			count[i] = 0;
		}
		int len = data.length();
		for (int i = 0; i < len; i++) {
			count[(data[i] - 'A')]++;
		}
		string ans = "";
		for (int i = 0; i < 10; i++) {
			if (solve (count, i, ans)) {
				break;
			}
		}
		cout << "Case #" << casei << ": " << ans << endl;
	}
	return 0;
}