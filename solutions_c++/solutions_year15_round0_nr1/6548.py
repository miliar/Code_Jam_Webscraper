#include <iostream>
#include <iomanip>
#include <fstream>
#include <math.h>
using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T;
	in >> T;
	for (int i=0; i<T; i++) {
		int Smax;
		in >> Smax;
		int r = 0;
		int s = 0;
		for (int j=0; j<Smax+1; j++) {
			char ci;
			in >> ci;
			int si = ci - '0';
			if (si != 0) {
				while (s < j) {
					r++;
					s++;
				}
				s += si;
			}
		}
		out << "Case #" << i+1 << ": " << r << '\n';
	}
	out.close();
	in.close();
	return 0;
}