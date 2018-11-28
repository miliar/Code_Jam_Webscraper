#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;

int al[26];

int main() {
	int T; cin >> T;
	for (int a0 = 1; a0 <= T; ++a0) {
		string s; cin >> s;
		vector<int> a;
		int n = s.size();
		for (int i = 0; i < n; ++i) {
			al[s[i] - 'A']++;
		}
		for (int i = 0; i < n; ++i) {
			if (s[i] == 'Z') {
				al['Z' - 'A']--;
				al['E' - 'A']--;
				al['R' - 'A']--;
				al['O' - 'A']--;
				a.push_back(0);
			}
			else if (s[i] == 'W') {
				al['T' - 'A']--;
				al['W' - 'A']--;
				al['O' - 'A']--;
				a.push_back(2);
			}
			else if (s[i] == 'U') {
				al['F' - 'A']--;
				al['O' - 'A']--;
				al['U' - 'A']--;
				al['R' - 'A']--;
				a.push_back(4);
			}
			else if (s[i] == 'X') {
				al['S' - 'A']--;
				al['I' - 'A']--;
				al['X' - 'A']--;
				a.push_back(6);
			}
			else if (s[i] == 'G') {
				al['E' - 'A']--;
				al['I' - 'A']--;
				al['G' - 'A']--;
				al['H' - 'A']--;
				al['T' - 'A']--;
				a.push_back(8);
			}
		}

		int seven = al['S' - 'A'];
		while (seven > 0) {
			al['S' - 'A']--;
			al['E' - 'A']--;
			al['V' - 'A']--;
			al['E' - 'A']--;
			al['N' - 'A']--;
			a.push_back(7);
			seven--;
		}
		int three = al['H' - 'A'];
		while (three > 0) {
			al['T' - 'A']--;
			al['H' - 'A']--;
			al['R' - 'A']--;
			al['E' - 'A']--;
			al['E' - 'A']--;
			a.push_back(3);
			three--;
		}
		int one = al['O' - 'A'];	
		while (one > 0) {
			al['O' - 'A']--;
			al['N' - 'A']--;
			al['E' - 'A']--;
			a.push_back(1);
			one--;
		}
		int five = al['V' - 'A'];
		while (five > 0) {
			al['F' - 'A']--;
			al['I' - 'A']--;
			al['V' - 'A']--;
			al['E' - 'A']--;
			a.push_back(5);
			five--;
		}
		int nine = al['I' - 'A'];	
		while (nine > 0) {
			al['N' - 'A']--;
			al['I' - 'A']--;
			al['N' - 'A']--;
			al['E' - 'A']--;
			a.push_back(9);
			nine--;
		}

		sort(a.begin(), a.end());
		cout << "Case #" << a0 << ": ";
		for (auto x : a) {
			cout << x;
		}
		cout << endl;
	}

	return 0;
}