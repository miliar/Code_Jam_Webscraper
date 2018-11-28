#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("D-small-attempt2.in");
	ofstream fout("output.txt");
	int n, x, r, c;
	string ans;
	fin >> n;
	for (int i=0; i<n; i++) {
		fin >> x >> r >> c;
		ans = "GABRIEL";
		while (1) {
			if (r*c % x != 0) {
				ans = "RICHARD";
				break;
			}
			if (x <= 2) {
				ans = "GABRIEL";
				break;
			}
			if (x == 3 ) {
				if (r == 1 || c == 1)
					ans = "RICHARD";
				break;
			} 
			if (x == 4) {
				if (!(r>2 && c > 2)) ans = "RICHARD";
				break;
			}
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
}
