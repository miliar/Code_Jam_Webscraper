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
		vector<double> Naomi, Ken;
		for (int j = 0; j < N; ++j) {
			double x;
			in >> x;
			Naomi.push_back(x);
		}
		for (int j = 0; j < N; ++j) {
			double x;
			in >> x;
			Ken.push_back(x);
		}

		sort(Naomi.begin(), Naomi.end());
		sort(Ken.begin(), Ken.end());

		int war = 0, deceit = 0;

		for (int j = 0; j < N; ++j) {
			if (Naomi[j] > Ken[deceit]) {
				++deceit;
			}
		}

		for (int j = 0; j < N; ++j) {
			while (j + war < N && Naomi[j] > Ken[j + war]) {
				++war;
			}
		}

		out << "Case #" << i+1 << ": " << deceit << " " << war << endl;
	}
	return 0;
}