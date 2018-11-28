#include <bits/stdc++.h>

using namespace std;

string nums[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

map<char, int> s;
map<char, int> n;
stack<int> digits;

bool sol(int lastd) {
	bool same = true;
	for(char c = 'A'; c <= 'Z'; c++) { 
		if(n[c] > s[c]) {
			return false;
		}
		else if(n[c] != s[c]) {
			same = false;
		}
	}
	if(same) {
		return true;
	}

	for(int i = lastd; i < 10; i++) {
		for(int j = 0; j < nums[i].length(); j++) {
			n[nums[i][j]]++;
		}
		if(sol(i)) {
			digits.push(i);
			return true;
		}
		for(int j = 0; j < nums[i].length(); j++) {
			n[nums[i][j]]--;
		}
	}

	return false;
}

void solve(string str) {
	for(int i = 0; i < str.length(); i++) {
		s[str[i]]++;
	}

	sol(0);
	while(digits.size() > 0) {
		cout << digits.top();
		digits.pop();
	}
	cout << endl;

	s.clear();
	n.clear();
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		string s;
		cin >> s;

		solve(s);
	}

	return 0;
}
