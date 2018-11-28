#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main() {
	ifstream input( "1.in" );
	ofstream output("1.out");
	string line;
	getline(input, line);
	int count = atoi(line.c_str());
	
	for (int k = 0; k < count; k++) {
		if (k != 0) {
			output << "\n";
		}
		int ans = 0;
		bool cheat = 0;
		bool bad = 0;
		int rowa, rowb;
		int a[4];
		int b[4];
		input >> rowa;
		
	//	cout << "rowa: " << rowa << "\n";
		
		int arow = 4-rowa;
		while (rowa > 1) {
			int null;
			input >> null >> null >> null >> null;
			rowa--;
		}
		input >> a[0] >> a[1] >> a[2] >> a[3];
		
	//	cout << "Row A: " << a[0] << "|" << a[1] << "|" << a[2] << "|" << a[3] << "\n";
		
		while (arow > 0) {
			int null;
			input >> null >> null >> null >> null;
			arow--;
		}
	
		input >> rowb;
		
	//	cout << "rowb: " << rowb << "\n";
		
		int brow = 4-rowb;
		while (rowb > 1) {
			int null;
			input >> null >> null >> null >> null;
			rowb--;
		}
		input >> b[0] >> b[1] >> b[2] >> b[3];
		
	//	cout << "Row B: " << b[0] << "|" << b[1] << "|" << b[2] << "|" << b[3] << "\n";
		
		while (brow > 0) {
			int null;
			input >> null >> null >> null >> null;
			brow--;
		}
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				if (a[i] == b[j]) {
					if (ans == 0 || a[i] == ans) {
						ans = a[i];
					} else {
						cheat = 1;
					}
				}
			}
		}
		if (ans == 0) {
			bad = 1;
		}
		output <<  "Case #" << k+1 << ": ";
		if (bad) {
			output << "Volunteer cheated!";
		} else if (cheat) {
			output << "Bad magician!";
		} else {
			output << ans;
		}
	}
	
	return 0;

}
