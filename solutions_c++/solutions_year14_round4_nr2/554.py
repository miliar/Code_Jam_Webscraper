#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		in >> N;
		vector<int> seq;
		for (int j = 0; j < N; ++j) {
			int t;
			in >> t;
			seq.push_back(t);
		}
		int count = 0;
		for (int j = 0; j < N; ++j) {
			int smallest = 0;
			for (int k = 1; k < seq.size(); ++k) {
				if (seq[k] < seq[smallest]) {
					smallest = k;
				}
			}
			count += min(smallest, (int)(seq.size() - 1 - smallest));
			seq.erase(seq.begin() + smallest);
		}
		out << "Case #" << (i + 1) << ": " << count << endl;
	}

	return 0;
}
