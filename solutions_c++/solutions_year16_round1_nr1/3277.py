#include <stdlib.h>
#include <stdio.h>

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <unordered_set>
#include <stdlib.h>

using namespace std;

string solve(const string &s) {
	vector<char> v;
	v.push_back(s[0]);
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] >= v[0]) {
			v.insert(v.begin(), s[i]);
		} else {
			v.push_back(s[i]);
		}
	}
	string result(v.size(), 'A');
	for (int i = 0; i < s.size(); ++i) {
		result[i] = v[i];
	}
	return result;
}

void read(string &s) {
	getline(cin, s);
	cerr << endl;
}

void write(int iter, string t) {
	cout << "Case #" << iter << ": " << t << "\n";
}

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	string s_;
	getline(cin, s_);
	stringstream ss(s_);
	int T;
	ss >> T;
	string s;
	for (int iter = 1; iter <= T; ++iter) {
		read(s);
		write(iter, solve(s));
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}
