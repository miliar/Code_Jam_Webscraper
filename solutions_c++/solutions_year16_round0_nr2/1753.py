#include <iostream>
#include <string>

using namespace std;
int main() {
	long long t, test, n, i;
	cin >> t;
	string s;
	for (test=1;test<=t;test++) {
		cin >> s;
		int count = 0;
		for (i=1;i<s.length();i++)
			if (s[i] != s[i-1]) count++;
		if (s[s.length()-1] == '-') count++;

		cout << "Case #" << test << ": " << count << endl;
	}
	return 0;
}
