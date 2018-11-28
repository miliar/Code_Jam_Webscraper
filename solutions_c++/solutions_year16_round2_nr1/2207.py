#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <Math.h>

using namespace std;
int main() {
	freopen("A-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	
	for (int dd = 0; dd < n; dd++) {
		string st;
		cin >> st;
		map <char, int> letter;
		for (char i = 'A'; i <= 'Z'; i++) {
			letter[i] = 0;

		}
		for (int i = 0; i < st.length(); i++) {
			letter[st[i]]++;
		}
		vector<int> ans(10);
		for (int i = 0; i < 10; i++) {
			ans[i] = 0;
		}
		//zero
		if (letter['Z'] != 0) {
			int temp = letter['Z'];
			ans[0] += temp;
			letter['O'] -= temp;
			letter['R'] -= temp;
			letter['E'] -= temp;
			letter['Z'] -= temp;
		}
		//, "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
		// TWO
		if (letter['W'] != 0) {
			int temp = letter['W'];
			ans[2] += temp;
			letter['O'] -= temp;
			letter['T'] -= temp;
			letter['W'] -= temp;
		}
		//, "ONE", ", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
		// four
		if (letter['U'] != 0) {
			int temp = letter['U'];
			ans[4] += temp;
			letter['F'] -= temp;
			letter['O'] -= temp;
			letter['R'] -= temp;
			letter['U'] -= temp;
		}
		//, "ONE", ", "THREE", , "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
		// five
		if (letter['F'] != 0) {
			int temp = letter['F'];
			ans[5] += temp;
			letter['I'] -= temp;
			letter['V'] -= temp;
			letter['E'] -= temp;
			letter['F'] -= temp;
		}
		//, "ONE", ", "THREE", , , "SIX", "SEVEN", "EIGHT", "NINE"
		// seven
		if (letter['V'] != 0) {
			int temp = letter['V'];
			ans[7] += temp;
			letter['S'] -= temp;
			letter['V'] -= temp;
			letter['E'] -= temp;
			letter['E'] -= temp;
			letter['N'] -= temp;
		}
		//, "ONE", ", "THREE", , , "SIX",, "EIGHT", "NINE"
		//six
		if (letter['S'] != 0) {
			int temp = letter['S'];
			ans[6] += temp;
			letter['S'] -= temp;
			letter['I'] -= temp;
			letter['X'] -= temp;
		}
		//, "ONE", ", "THREE", , ,, "EIGHT", "NINE"
		//three
		if (letter['R'] != 0) {
			int temp = letter['R'];
			ans[3] += temp;
			letter['T'] -= temp;
			letter['H'] -= temp;
			letter['R'] -= temp;
			letter['E'] -= temp;
			letter['E'] -= temp;
		}
		//, "ONE", ",, , ,, "EIGHT", "NINE"
		//eight
		if (letter['G'] != 0) {
			int temp = letter['G'];
			ans[8] += temp;
			letter['E'] -= temp;
			letter['I'] -= temp;
			letter['G'] -= temp;
			letter['H'] -= temp;
			letter['T'] -= temp;
		}
		//, "ONE", ",,"NINE"
		//eight
		if (letter['I'] != 0) {
			int temp = letter['I'];
			ans[9] += temp;
			letter['N'] -= temp;
			letter['I'] -= temp;
			letter['N'] -= temp;
			letter['E'] -= temp;
		}
		//, "ONE", 
		//ONE
		if (letter['O'] != 0) {
			int temp = letter['O'];
			ans[1] += temp;
			letter['O'] -= temp;
			letter['N'] -= temp;
			letter['E'] -= temp;
		}

		cout << "Case #"<<dd+1<<": ";
		for (int i = 0; i < ans.size(); i++) {
			for (int j = 0; j < ans[i]; j++) {
				cout << i;
			}
		}
		cout << endl;
	}
	//system("pause");
	return 0;
}