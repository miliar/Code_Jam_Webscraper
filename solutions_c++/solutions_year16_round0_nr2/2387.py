#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>
using namespace std;

string HStmp;

int main() {
	int Ncase;
	cin >> Ncase;
	ostringstream output;
	for (int i0 = 1; i0 <= Ncase; ++i0){
		string HS;
		cin >> HS;
		int numFlips = 0;
		char last = HS[0];
		for (int i = 1; i < HS.size(); ++i){
			if (HS[i] != last) {
				last = HS[i];
				numFlips++;
			}
		}
		if (HS.back() == '-') {
			numFlips++;
		}
		output << "Case #" << i0 << ": " << numFlips << endl;
	}
	cout << output.str();
	return 0;
}
