#include <fstream>
#include <string>

using namespace std;

ifstream in("input");
ofstream out("output");

string players[3] = {"RICHARD","GABRIEL","MISSED CASE"};

int main() {
	int t;
	in >> t;
	for(int tt = 1; tt <= t; ++tt) {
		int x,r,c;
		in >> x >> r >> c;
		int winner = 0;

		if(x == 1) {
			winner = 1;
		}

		if(x == 2) {
			if(r%2 == 0 || c%2 == 0) {
				winner = 1;
			}
		}

		if(x == 3) {
			if(r == 2) {
				if(c % 3 == 0) 
					winner = 1;
			}
			if(c == 2) {
				if(r % 3 == 0) 
					winner = 1;
			}

			if(r == 3) {
				if(c%2 == 0 || c%3 == 0) 
					winner = 1;
			}
			if(c == 3) {
				if(r % 2 == 0 || r % 3 == 0)
					winner = 1;
			}
		}

		if(x == 4) {
			if(r == 4) {
				if(c > 2) winner = 1;
			}
			if(c == 4) {
				if(r > 2) winner = 1;
			}
		}

		out << "Case #" << tt << ": ";
		//out << x << ' ' << r << ' ' << c << ' ';
		out << players[winner] << '\n';
	}
}