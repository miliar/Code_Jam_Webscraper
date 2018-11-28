
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
using namespace std;


ofstream out("out.txt");

vector <long long> list;

bool isfair(long long n) {
	string s;
	ostringstream convert;
	convert << n;
	s = convert.str();

	for (int i = 0; i < s.length()/2; i++) {
		if (s.at(i) != s.at(s.length()-i-1))
			return false;
	}
	return true;
}

bool issquare(long long n) {
	int a;
	a = sqrt(n);
	return (a*a == n) and isfair(a);
}

bool isfairsquare(long long n) {

	return isfair(n) and issquare(n);

}

void generate() {
	for (long long n = 1; n < 10000000; n++) {
		if (isfair(n) && isfair(n*n)) {
			list.push_back(n*n);

		}
	}
}




int main() {
	ifstream f("C-large-1.in");
	int T;
	f >> T;
	generate();
	for (int x = 0; x < T; x++) {
	    long long a, b;
		f >> a >> b;


		int ai = 0, bi = 0;
		while (list.at(ai) < a) {
			ai++;
			if (ai >= list.size()) break;
		}
		while (list.at(bi) <= b) {
			bi++;
			if (bi >= list.size()) break;
		}

		out << "Case #" << x+1 << ": " << bi-ai << endl;
	}

	return 0;
}




