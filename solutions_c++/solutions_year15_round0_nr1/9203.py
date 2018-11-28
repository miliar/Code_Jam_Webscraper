#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream in = ifstream("A-large.in");
	int cases, s_max, nop;
	int friends = 0;
	int total = 0;
	int required = 0;
	char numberOfPeople;
	in >> cases;
	//cout << cases;
	for (int i = 1; i <= cases; i++) {
		total = 0;
		required = 0;
		friends = 0;
		cout << "Case #" << i << ": ";
		in >> s_max;

		for (int j = 0; j <= s_max; j++) {
			in >> numberOfPeople;
			nop = atoi(&numberOfPeople);
			
			if (nop != 0) {
				if (total - required < 0) {
					friends += required - total;
					total += required - total;
				}
			}

			total += nop;
			required++;
					
		}
		cout << friends;
		cout << "\n";
	}
	in.close();
}