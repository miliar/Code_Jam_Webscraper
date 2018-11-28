#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace	std;

vector<int> GettingDigits(string s) {
	int a[26] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 };
	int len = s.size();
	vector<int> ans;

	for (int i = 0; i < len; ++i) {
		a[s[i] - 'A']++;
	}

	cout << a['Z'-'A'] << endl;

	// check zero
	if (a['Z' - 'A'] != 0) {
		for (int i = 0; i < a['Z' - 'A']; ++i) {
			ans.push_back(0);
			cout << "add 0" << endl;
		}
		a['E' - 'A'] -= a['Z' - 'A'];
		a['R' - 'A'] -= a['Z' - 'A'];
		a['O' - 'A'] -= a['Z' - 'A'];
		a['Z' - 'A'] = 0;
	}

	//check two
	if (a['W' - 'A'] != 0) {
		for (int i = 0; i < a['W' - 'A']; ++i) {
			ans.push_back(2);
		}
		a['T' - 'A'] -= a['W' - 'A'];
		a['O' - 'A'] -= a['W' - 'A'];
		a['W' - 'A'] = 0;
	}

	// check four
	if (a['U' - 'A'] != 0) {
		for (int i = 0; i < a['U' - 'A']; ++i) {
			ans.push_back(4);
		}
		a['F' - 'A'] -= a['U' - 'A'];
		a['O' - 'A'] -= a['U' - 'A'];
		a['R' - 'A'] -= a['U' - 'A'];
		a['U' - 'A'] = 0;
	}

	// check six
	if (a['X' - 'A'] != 0) {
		for (int i = 0; i < a['X' - 'A']; ++i) {
			ans.push_back(6);
		}
		a['S' - 'A'] -= a['X' - 'A'];
		a['I' - 'A'] -= a['X' - 'A'];
		a['X' - 'A'] = 0;
	}

	// check eight
	if (a['G' - 'A'] != 0) {
		for (int i = 0; i < a['G' - 'A']; ++i) {
			ans.push_back(8);
		}
		a['E' - 'A'] -= a['G' - 'A'];
		a['I' - 'A'] -= a['G' - 'A'];
		a['H' - 'A'] -= a['G' - 'A'];
		a['T' - 'A'] -= a['G' - 'A'];
		a['G' - 'A'] = 0;
	}

	// after checking all even numbers
	// check one
	if (a['O' - 'A'] != 0) {
		for (int i = 0; i < a['O' - 'A']; ++i) {
			ans.push_back(1);
		}
		a['N' - 'A'] -= a['O' - 'A'];
		a['E' - 'A'] -= a['O' - 'A'];
		a['O' - 'A'] = 0;
	}

	// check three
	if (a['T' - 'A'] != 0) {
		for (int i = 0; i < a['T' - 'A']; ++i) {
			ans.push_back(3);
		}
		a['H' - 'A'] -= a['T' - 'A'];
		a['R' - 'A'] -= a['T' - 'A'];
		a['E' - 'A'] -= a['T' - 'A'] * 2;
		a['T' - 'A'] = 0;
	}

	// check five
	if (a['F' - 'A'] != 0) {
		for (int i = 0; i < a['F' - 'A']; ++i) {
			ans.push_back(5);
		}
		a['I' - 'A'] -= a['F' - 'A'];
		a['V' - 'A'] -= a['F' - 'A'];
		a['E' - 'A'] -= a['F' - 'A'];
		a['F' - 'A'] = 0;
	}

	// check seven
	if (a['S' - 'A'] != 0) {
		for (int i = 0; i < a['S' - 'A']; ++i) {
			ans.push_back(7);
		}
		a['E' - 'A'] -= a['S' - 'A'] * 2;
		a['V' - 'A'] -= a['S' - 'A'];
		a['N' - 'A'] -= a['S' - 'A'];
		a['S' - 'A'] = 0;
	}

	// at last check nine
	if (a['I' - 'A'] != 0) {
		for (int i = 0; i < a['I' - 'A']; ++i) {
			ans.push_back(9);
		}
		a['N' - 'A'] -= a['I' - 'A'] * 2;
		a['E' - 'A'] -= a['I' - 'A'];
		a['I' - 'A'] = 0;
	}

	for (int i = 0; i < 26; ++i) {
		if (a[i] != 0) {
			cout << "something is wrong!" << endl;
			cout << i << " != 0" << endl;
		}
	}

	sort(ans.begin(), ans.end());
	return ans;
}

int main() {
	ifstream input("A-large.in");
	ofstream output("small_case_ans.txt");
	string num;
	getline(input, num);
	int n = stoi(num);
	for (int i = 0; i < n; ++i) {
		output << "case #" << i + 1 << ": ";
		getline(input, num);
		vector<int> res = GettingDigits(num);
		for (int j = 0; j < res.size(); ++j) {
			output << res[j];
		}
		output << endl;
	}

	

	return 0;
}