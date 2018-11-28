#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int count(string str) {
	if (str.length() == 1) {
		return str != "+";
	}
	int c = 0;
	for (int i = 1; i < str.length(); ++i) {
		if (str[i] != str[i - 1])
			++c;
	}
	return c + (str[str.length() - 1] == '-');
}

int main() {
	ifstream in("B-large.in");
	ofstream out("largeoutput.txt");
	int cases, num;
	in >> cases;
	for (num = 1; num <= cases; ++num) {
		string str;
		in >> str;
		out << "Case #" << num << ": " << count(str) << endl;
	}
	return 0;
}