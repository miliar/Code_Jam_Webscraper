#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>

using namespace std;

int main() {
	std::ifstream in("B-large.in");
	std::ofstream out("b.out");
	int t;
	char ch[100];
	string str;
	in >> t;
	for(int i = 1; i <= t; i++) {
		in.ignore();
		in >> str;
		bool begin = true;
		char prev = '-';
		int count = 0;
		for(int j = 0; j < str.length(); j++) {
			if (str[j] == '+') {
				prev = '+';
				continue;
			}
			if (str[j] == '-') {
				int k = j+1;
				while (str[k] == '-' && k < str.length()) {
					k++;
				}
				if (j > 0 && str[j-1] == '+') {
					count += 2;
				} else {
					count += 1;
				}
				j = k-1;
			}
		}
		out << "Case #" << i << ": " << count;
		if (i < t) {
			out << endl;
		}
	}
}
