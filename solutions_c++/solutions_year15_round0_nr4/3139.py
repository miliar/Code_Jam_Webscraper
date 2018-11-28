#include<iostream>
#include<string>
#include<fstream>

using namespace std;
int main() {
	ifstream input("input.in");
	ofstream output("output.txt");
	
	int t; input >> t;
	for (int k = 1; k <= t; ++k) {
		int x, r, c; input >> x >> r >> c;
		if (x == 1) {
			output << "Case #" << k << ": GABRIEL" << endl;
		}

		if(x == 2){
			if (r == 1) {
				if (c == 2 || c == 4) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
			if (r == 2) {
				output << "Case #" << k << ": GABRIEL" << endl;
			}
			if (r == 3) {
				if (c == 2 || c == 4) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
			if (r == 4) {
				output << "Case #" << k << ": GABRIEL" << endl;
			}
		}




		if (x == 3) {
			if (r == 1) {
				output << "Case #" << k << ": RICHARD" << endl;
			}
			if (r == 2) {
				if (c == 3) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
			if (r == 3) {
				if (c == 2 || c == 3 || c == 4) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
			if (r == 4) {
				if (c == 3) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
		}


		if (x == 4) {
			if (r == 3) {
				if (c == 4) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}else if (r == 4) {
				if (c == 3 || c == 4) {
					output << "Case #" << k << ": GABRIEL" << endl;
				}
				else {
					output << "Case #" << k << ": RICHARD" << endl;
				}
			}
			else {
				output << "Case #" << k << ": RICHARD" << endl;
			}
		}
	}
	
	return 0;
}