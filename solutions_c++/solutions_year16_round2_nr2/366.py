#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	string file = "B-small-attempt2.in";
	ifstream input;
	input.open(file);
	ofstream output;
	output.open("out_" + file);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++)
	{
		output << "Case #" << cases << ": ";
		string a, b, c, d;
		input >> c >> d;
		if (c.size() == 1) {
			a = "00" + c;
			b = "00" + d;
		}
		else if (c.size() == 2) {
			a = "0" + c;
			b = "0" + d;
		}
		else {
			a = c;
			b = d;
		}
		int min = 1000;
		int A = 0, B = 0;

		for (int i = 0; i < 1000; i++) {
			for (int j = 0; j < 1000; j++) {
				if ((a[0] == '?' || a[0] - '0' == i / 100) && (a[1] == '?' || a[1] - '0' == (i / 10) % 10) && (a[2] == '?' || a[2] - '0' == i % 10) &&
					(b[0] == '?' || b[0] - '0' == j / 100) && (b[1] == '?' || b[1] - '0' == (j / 10) % 10) && (b[2] == '?' || b[2] - '0' == j % 10))
					if (abs(i - j) < min) {
						min = abs(i - j);
						A = i;
						B = j;
					}
			}
		}

		a = to_string(A);
		b = to_string(B);

		for (int i = c.size(); i > a.size(); i--)
			output << 0;
		output << a << " ";
		for (int i = d.size(); i > b.size(); i--)
			output << 0;
		output << b << endl;
	}
	output.close();
	input.close();
	return 0;
}