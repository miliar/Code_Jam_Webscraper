#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

bool if_mrk_all(unsigned long long in, char mrk[]) {
        while (in) {
                mrk[in % 10] = 1;
                in = in / 10;
        }
        for (unsigned i = 0; i < 10; i ++) {
                if (!mrk[i]) {
                       return false;
                }
        }
        return true;
}

int main() {
        ifstream input;
        ofstream output;
        input.open("./Downloads/A-large.in");
        output.open("result20160101");

        unsigned T;
        input >> T;

	for (unsigned t = 0; t < T; t ++) {
		unsigned long long N;
		input >> N;
                if (N == 0) {
                        output << "Case #" << t + 1 << ": INSOMNIA" << endl;
                } else {
                        unsigned long long start = N;
                        char mark[10];
                        memset(mark, 0, 10);
                        while (!if_mrk_all(start, mark)) {
                                start += N;
                        }
		        output << "Case #" << t + 1 << ": " << start << endl;
                }
	}

	return 0;
}
