#include <iostream>

using namespace std;

typedef long long ll;

int main() {
	int t;
	cin >> t;
	cin.ignore();
	for (int cas = 0; cas < t; ++cas) {
		string s;
		getline(cin, s);
		char last = '+';
		int k = 0;
		for (int i = s.size()-1; i>=0; --i) {
			if (s[i] != last) k++;
			last=s[i];
		}
		cout << "Case #" << cas+1 << ": " << k << endl;
	}
}

