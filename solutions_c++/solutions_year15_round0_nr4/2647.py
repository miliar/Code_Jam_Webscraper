#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int eat_time(int d) {
	if (d <= 3) {
		return d;
	}
	if (d == 4) {
		return 2;
	}
	return 3;
}

int spec_time(int d) {
	if (d <= 3) {
		return 0;
	}
	if (d == 4) {
		return 1;
	}
	return (d - 1)/3;
}

int main()
{
	ifstream in;
	in.open("D-small-attempt0.in");
	//in.open("omino.in");
	ofstream out;
	out.open("answerOmSmall.txt");
	int t;
	in >> t;
	int win = 0;
	for (int ti = 1; ti <= t; ti++) {
		int x, r, c;
		in >> x >> r >> c;
		if (r > c) {
			swap(r,c);
		}
		if (x == 1) {
			win = 2;
		} else if (x == 2) {
			if (r == 1) {
				if (c % 2 == 1) {
					win = 1;
				} else {
					win = 2;
				}
			} else if (r == 2) {
				win = 2;
			} else if (r == 3) {
				if (c == 3) {
					win = 1;
				} else {
					win = 2;
				}
			} else{
				win = 2;
			}
		} else if (x == 3) {
			if (r == 1) {
				win = 1;
			} else if (r == 2) {
				if (c == 3) {
					win = 2;
				} else {
					win = 1;
				}
			} else if (r == 3) {
				win = 2;

			} else {
				win = 1;
			}
		} else {
			if (r == 1 || r == 2) {
				win = 1;
			} else if (r == 3) {
				if (c == 3) {
					win = 1;
				} else {
					win = 2;
				}
			} else {
				win = 2;
			}
		}
		out << "Case #" << ti << ": ";
		if (win == 1) {
			out << "RICHARD" << endl;
		} else {
			out << "GABRIEL" << endl;
		}
	}
	return 0;
}
