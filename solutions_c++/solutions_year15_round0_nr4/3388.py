#include <iostream>
#include <iomanip>
#include <fstream>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	ifstream in("D-small-attempt1.in");
	ofstream out("D-small-attempt1.out");
	int T;
	in >> T;

	for (int i=0; i<T; i++) {
		int X,R,C;
		in >> X >> R >> C;
		if (X == 1) {
			out << "Case #" << i+1 << ": " << "GABRIEL" << '\n';
		} else if (X == 2) {
			if (R*C % 2 == 0) {
				out << "Case #" << i+1 << ": " << "GABRIEL" << '\n';
			} else {
				out << "Case #" << i+1 << ": " << "RICHARD" << '\n';
			}
		} else if (X == 3) {
			if ((R>=2 && C==3) || (C>=2 && R==3)) {
				out << "Case #" << i+1 << ": " << "GABRIEL" << '\n';
			} else {
				out << "Case #" << i+1 << ": " << "RICHARD" << '\n';
			}
		} else if (X == 4) {
			if ((R>=3 && C==4) || (C>=3 && R==4)) {
				out << "Case #" << i+1 << ": " << "GABRIEL" << '\n';
			} else {
				out << "Case #" << i+1 << ": " << "RICHARD" << '\n';
			}
		}
	}
	out.close();
	in.close();
	return 0;
}