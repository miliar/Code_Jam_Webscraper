#include <iostream>
#include <string>

using namespace std;

int main()
{
	int tests;
	string s;
	cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		cin >> s;
		int end = s.length();
		int flips = (s[end-1] == '+') ? 0 : 1;
		char curr = s[0];
		for (int j = 1; j < end; ++j) {
			if (s[j] != curr) ++flips;
			curr = s[j];
		}
		cout << "Case #" << i << ": " << flips << endl;
	}	
	return 0;
}
