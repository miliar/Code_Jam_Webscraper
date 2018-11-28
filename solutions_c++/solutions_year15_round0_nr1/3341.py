#include <iostream>

using namespace std;

int main (void) {
	int nc; 
	cin >> nc;
	for (int c = 1; c <= nc; ++c) {
		int sm;
		cin >> sm;
		string s;
		cin >> s;
		int tot = 0, res = 0;
		for (int i = 0; i < s.size(); ++i) {
			if (tot < i) {
				res += i - tot;
				tot = i;
			}
			tot += s[i] -  '0';
		}
		cout << "Case #" << c << ": " << res << endl;
	}

	return 0;
}