#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>

using namespace std;

string st[] = {"ZWXG", "HS", "V", "F", "OI"};
map<char, int> numbers;
map<char, string> m;

string process(string s) {
	string res = "";
	for(int i = 0; i < 5; ++i) {
		string current = st[i];
		for(int j = 0; j < current.size(); ++j) {
			char current_char = current[j];
			int num_char = 0, found[10];
			for(int k = 0; k < s.size(); ++k) {
				if(s[k] == current_char)
					num_char++;
			}
			for(int k = 0; k < m[current_char].size(); ++k) {
				found[k] = num_char;
			}
			for(int k = 0; k < s.size(); ++k) {
				int pos = m[current_char].find(s[k]);
				if(pos != string::npos && found[pos] > 0) {
					s.erase(k, 1);
					--k;
					found[pos] --;
				}
			}
			for(int k = 0; k < num_char; ++k) {
				char to_add = numbers[current_char] + '0';
				res += to_add;
			}
		}
	}
	sort(res.begin(), res.end());
	return res;
}

int main() {
	m['Z'] = "ZERO"; m['W'] = "TWO"; m['H'] = "THREE"; m['F'] = "FOUR"; m['X'] = "SIX"; m['G'] = "EIGHT";
	m['S'] = "SEVEN"; m['V'] = "FIVE"; m['O'] = "ONE"; m['I'] = "NINE";
	numbers['Z'] = 0; numbers['W'] = 2; numbers['H'] = 3; numbers['X'] = 6; numbers['G'] = 8;
	numbers['S'] = 7; numbers['V'] = 5; numbers['O'] = 1; numbers['I'] = 9; numbers['F'] = 4;
	int t;
	string s;
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tst = 1; tst <= t; ++tst) {
		cin >> s;
		cout << "Case #" << tst << ": " << process(s) << '\n';
	}
	return 0;
}