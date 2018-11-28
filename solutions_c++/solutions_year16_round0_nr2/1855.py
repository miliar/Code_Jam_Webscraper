#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int cases;
	cin >> cases;
	for (int cas = 1; cas <= cases; ++cas) {
		string s;
		cin >> s;
		int steps = (s[s.size()-1] == '-');
		for (int i = 1; i < s.size(); ++i) steps += s[i] != s[i-1];
		cout << "Case #" << cas << ": "<< steps << endl;
	}
}
