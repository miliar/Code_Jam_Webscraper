#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main() {
	std::ifstream in("a.in");
	std::ofstream out("a.out");
	int n, t;
	string str, res;
	in >> t;
	for(int i = 1; i <= t; i++) {
		in >> str;
		char fir = str[0];
		res = str[0];
		for(int j = 1, len = str.length(); j < len; j++) {
			if (str[j] < fir) {
				res += str[j];
			} else {
				fir = str[j];
				res = str[j] + res;
			}
		}
		out << "Case #" << i << ": " << res;
		if (i < t) {
			out << endl;
		}
	}
}
