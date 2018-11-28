#include <iostream>
#include <string>
using namespace std;

int main () {
	int t;
	cin >> t;
	for (int q=1; q<=t; q++) {
		string str;
		cin >> str;
		int res = 0;
		for (unsigned i=1; i<str.size(); i++) {
			if (str[i] != str[i-1]) {
				res++;
			}
		}
		if ((str[0] == '+') == (res%2)) {
			res++;
		}
		cout << "Case #" << q << ": " << res << "\n";
	}
	return 0;
}
