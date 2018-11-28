#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
        ifstream input;
        ofstream output;
        input.open("./Downloads/B-large.in");
        output.open("result20160102");

        unsigned T;
        input >> T;

	for (unsigned t = 0; t < T; t ++) {
		string pile;
		input >> pile;
                int char_sz = 0;
                int last = 0;
                for (unsigned i = 0; i < pile.size(); i ++) {
                       if (i == 0 || pile[i] != pile[i - 1]) {
                              char_sz ++;
                       }
                       if (pile[i] == '+') {
                              last = 1;
                       } else {
                              last = 0;
                       }
                }
                if (last == 1) {
                       char_sz --;
                }
		output << "Case #" << t + 1 << ": " << char_sz << endl;
	}

	return 0;
}
