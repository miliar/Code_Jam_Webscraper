#include <iostream>
#include <string>
#include <vector>
using namespace std;
vector<int> cnt;
int totLen;
string ans;
string now;
int nowLen;

const string digit[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool canPut(int j) {

//	cout << "digit[j] = " << digit[j] << endl;

	bool ok = true;
	for (int k = 0; k < digit[j].size(); k ++) {
		cnt[digit[j][k] - 'A'] --;
		if (cnt[digit[j][k] - 'A'] < 0) ok = false;
	}
//	for (int k = 0; k < 26; k ++) cout << cnt[k] << " ";
	for (int k = 0; k < digit[j].size(); k ++) {
		cnt[digit[j][k] - 'A'] ++;
	}
	return ok;
}

void doPut(int j) {
	for (int k = 0; k < digit[j].size(); k ++) {
		cnt[digit[j][k] - 'A'] --;
	}
}

void undoPut(int j) {
	for (int k = 0; k < digit[j].size(); k ++) {
		cnt[digit[j][k] - 'A'] ++;
	}
}

void search() {
//	cout << "now = " << now << endl;
	if (nowLen == totLen) {
		ans = now;
		return;
	}
	for (int j = 0; j < 10; j ++) {
//		cout << "j = " << j << endl;
//		for (int k = 0; k < 26; k ++) cout << cnt[k] << " ";
//		cout << endl;
		if (canPut(j)) {
			doPut(j);
			now += char('0') + j;
			nowLen += digit[j].size();
			search();
			if (!ans.empty()) return;
			undoPut(j);
			now = now.substr(0, now.size() - 1);
			nowLen -= digit[j].size();
		}
	}
}

int main() {
	int testcases;
	cin >> testcases;
	for (int testcase = 0; testcase < testcases; testcase ++) {
		string s;
		cin >> s;
		cnt.clear();
		cnt.resize(26);
		for (int i = 0; i < s.size(); i ++) {
			cnt[s[i] - 'A'] ++;
		}
		totLen = s.size();
		ans = "";
		now = "";
		nowLen = 0;
		search();
		cout << "Case #" << testcase + 1 << ": " << ans << endl;
	}
	return 0;	
}