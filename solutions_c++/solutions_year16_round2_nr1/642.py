#include <bits/stdc++.h>
using namespace std;

int n_test;
int counter[256];
string name[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int occur[10];

void eliminate(int x) {
	for (int j = 0; j < name[x].length(); ++j)
		counter[name[x][j]] -= occur[x];
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> n_test;
	for (int test = 1; test <= n_test; ++test) {
		string s;
		cin >> s;
		memset(counter, 0, sizeof counter);
		for (int i = 0; i < s.length(); ++i) 
			counter[s[i]]++;
		occur[0] = counter['Z']; eliminate(0);
		occur[8] = counter['G']; eliminate(8);
		occur[3] = counter['H']; eliminate(3);
		occur[2] = counter['T']; eliminate(2);
		occur[4] = counter['U']; eliminate(4);
		occur[5] = counter['F']; eliminate(5);
		occur[1] = counter['O']; eliminate(1);
		occur[7] = counter['V']; eliminate(7);
		occur[6] = counter['S']; eliminate(6);
		occur[9] = counter['I']; eliminate(9);

		cout << "Case #" << test << ": ";
		for (int i = 0; i < 10; ++i)
			for (int j = 0; j < occur[i]; ++j)
				cout << i;
		cout << endl;
	}
}
