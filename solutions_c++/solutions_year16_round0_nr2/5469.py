#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		string s;
		cin >> s;
		int count = 1;
		for (int i = 1; i < s.size(); ++i)
			if (s[i] != s[i-1])
				++count;
		if (s[s.size() - 1] == '+')
			--count;
		cout << count << endl;
	}
}