#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	ifstream in("D-small-attempt1.in");
	ofstream out("smalloutput.txt");
	int cases, num;
	in >> cases;
	for (num = 1; num <= cases; ++num) {
		int K, C, S;
		in >> K >> C >> S;
		out << "Case #" << num << ": ";
		for (int i = 0; i < S; i++) {
			out << i + 1 << " ";
		}
		out << endl;
	}
	return 0;
}