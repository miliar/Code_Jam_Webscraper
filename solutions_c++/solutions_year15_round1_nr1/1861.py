#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
#include<fstream>
using namespace std;

int main() {
	ifstream input("input.in");
	ofstream output("output.txt");
	int testcase; input >> testcase;
	for (int k = 1; k <= testcase; ++k) {
		int n; input >> n;
		vector < int > mush(n);
		int bigfall = 0;
		long long total1 = 0, total2 = 0;
		for (int i = 0; i < n; ++i) {
			input >> mush[i];
			if (i > 0) {
				if (mush[i - 1] > mush[i]) {
					total1 += mush[i - 1] - mush[i];
					if (mush[i - 1] - mush[i] > bigfall) {
						bigfall = mush[i - 1] - mush[i];
					}
				}
			}
		}
		for (int i = 0; i < n - 1; ++i) {
			if (mush[i] <= bigfall) {
				total2 += mush[i];
			}
			else {
				total2 += bigfall;
			}
		}
		output << "Case #" << k << ": " << total1 << " " << total2 << endl;
	}
	return 0;
}