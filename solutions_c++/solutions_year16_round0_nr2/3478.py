#include <iostream>
#include <vector>
#include <string>

using namespace std;

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {

		bool wasmin = false;
		char c;
		char cm;
		int dif = 0;
		string str;

		cin >> str;
		cm = str[0];
		c = str[0]; if (c == '-') wasmin = true;

		for (int j = 1; j < str.size(); j++) {
			c = str[j];
			if (c == '-') wasmin = true;
			if (c != cm) dif++;
			cm = c;
		}

		if (!wasmin) cout << "CASE #" << i + 1 << ": 0" << endl;
		else {
			if (c == '-') dif++;
			cout << "CASE #" << i + 1 << ": " << dif << endl;
		}
	}
	

}