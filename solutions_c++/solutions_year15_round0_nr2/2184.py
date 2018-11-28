#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int getmax(int total, int divisions) {
	return total / (divisions + 1) + (total % (divisions + 1) ? 1 : 0);
}

int main(){
	ifstream input("input.txt");
	ofstream output("output.txt");

	int T;
	input >> T;
	for (int i = 0; i < T; ++i) {
		int D;
		vector<int> pancakes;
		vector<int> divisions;
		input >> D;
		int most = 0;
		for (int j = 0; j < D; ++j) {
			int next;
			input >> next;
			pancakes.push_back(next);
			divisions.push_back(0);
			most = max(most, next);
		}
		int best = most;
		for (int j = 0; j < most; ++j) {
			int top = 0;
			int second = 0;
			if (D > 1) {
				if (getmax(pancakes[1], divisions[1]) > getmax(pancakes[0], divisions[0])) {
					top = 1;
				}
				else {
					second = 1;
				}
			}
			for (int k = 2; k < D; ++k) {
				int curr = getmax(pancakes[k], divisions[k]);
				if (curr > getmax(pancakes[top], divisions[top])) {
					second = top;
					top = k;
				}
				else if (curr > getmax(pancakes[second], divisions[second])) {
					second = k;
				}
			}
			++divisions[top];
			int roundmax = max(getmax(pancakes[top], divisions[top]), getmax(pancakes[second], divisions[second]));
			best = min(best, roundmax + j + 1);
		}

		output << "Case #" << (i + 1) << ": " << best << endl;
	}

	return 0;
}