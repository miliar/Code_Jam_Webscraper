#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main() {
	ofstream ofs("pancakes.txt");
	int t;
	cin >> t;
	int c = 1;

	while (c <= t) {
		string str;
		cin >> str;
		int len = str.length();

		char ch = str[0];
		int in = 0;
		bool flag = true;
		int step = 0;
		while (flag) {

			int i = in + 1;
			while (i < len && str[i] == ch)
				i++;

			if (i == len) {
				if (ch == '+') {
					break;
				}
				else {
					step++;
					break;
				}
			}
			else {
				ch = (ch == '+') ? '-' : '+';
				for (int j = 0; j < i; j++) {
					str[j] = ch;
				}
				in = i;
			}

			step++;			
		}
		ofs << "Case #" << c++ << ": " << step << endl;
	}
}