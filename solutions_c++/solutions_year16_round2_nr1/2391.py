#include <bits/stdc++.h>

using namespace std;

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; ++t) {
		string s;
		cin >> s;
		vector<int> freq(26, 0);
		for (char c : s) {
			++freq[c - 'A'];
		}
		vector<int> ans;
		while (freq['Z' - 'A'] > 0 && freq['E' - 'A'] > 0 && freq['R' - 'A'] > 0 && freq['O' - 'A'] > 0) {
			--freq['Z' - 'A'];
			--freq['E' - 'A'];
			--freq['R' - 'A'];
			--freq['O' - 'A'];
			ans.push_back(0);
		}
		while (freq['T' - 'A'] > 0 && freq['W' - 'A'] > 0 && freq['O' - 'A'] > 0) {
			--freq['T' - 'A'];
			--freq['W' - 'A'];
			--freq['O' - 'A'];
			ans.push_back(2);
		}
		while (freq['E' - 'A'] > 0 && freq['I' - 'A'] > 0 && freq['G' - 'A'] > 0 && freq['H' - 'A'] > 0 && freq['T' - 'A'] > 0) {
			--freq['E' - 'A'];
			--freq['I' - 'A'];
			--freq['G' - 'A'];
			--freq['H' - 'A'];
			--freq['T' - 'A'];
			ans.push_back(8);
		}
		
		while (freq['F' - 'A'] > 0 && freq['O' - 'A'] > 0 && freq['U' - 'A'] > 0 && freq['R' - 'A'] > 0) {
			--freq['F' - 'A'];
			--freq['O' - 'A'];
			--freq['U' - 'A'];
			--freq['R' - 'A'];
			ans.push_back(4);
		}
		while (freq['S' - 'A'] > 0 && freq['I' - 'A'] > 0 && freq['X' - 'A'] > 0) {
			--freq['S' - 'A'];
			--freq['I' - 'A'];
			--freq['X' - 'A'];
			ans.push_back(6);
		}
		
		while (freq['S' - 'A'] > 0 && freq['E' - 'A'] > 1 && freq['V' - 'A'] > 0 && freq['N' - 'A'] > 0) {
			--freq['S' - 'A'];
			--freq['N' - 'A'];
			--freq['V' - 'A'];
			--freq['E' - 'A'];
			--freq['E' - 'A'];
			ans.push_back(7);
		}
		while (freq['T' - 'A'] > 0 && freq['H' - 'A'] > 0 && freq['R' - 'A'] > 0 && freq['E' - 'A'] > 1) {
			--freq['T' - 'A'];
			--freq['H' - 'A'];
			--freq['R' - 'A'];
			--freq['E' - 'A'];
			--freq['E' - 'A'];
			ans.push_back(3);
		}
		
		while (freq['F' - 'A'] > 0 && freq['I' - 'A'] > 0 && freq['V' - 'A'] > 0 && freq['E' - 'A'] > 0) {
			--freq['F' - 'A'];
			--freq['I' - 'A'];
			--freq['V' - 'A'];
			--freq['E' - 'A'];
			ans.push_back(5);
		}
		while (freq['N' - 'A'] > 1 && freq['I' - 'A'] > 0 && freq['E' - 'A'] > 0) {
			--freq['N' - 'A'];
			--freq['N' - 'A'];
			--freq['I' - 'A'];
			--freq['E' - 'A'];
			ans.push_back(9);
		}
		
		while (freq['O' - 'A'] > 0 && freq['N' - 'A'] > 0 && freq['E' - 'A'] > 0) {
			--freq['O' - 'A'];
			--freq['N' - 'A'];
			--freq['E' - 'A'];
			ans.push_back(1);
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << t << ": ";
		for (auto i : ans) {
			cout << i;
		}
		cout << '\n';
	}
	return 0;
}