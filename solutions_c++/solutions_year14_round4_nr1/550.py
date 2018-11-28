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
		int N, X;
		in >> N >> X;
		vector<int> files;
		for (int j = 0; j < N; ++j) {
			int t;
			in >> t;
			files.push_back(t);
		}
		sort(files.begin(), files.end());
		int s = 0, count = 0;
		for (int e = N - 1; e >= s; --e) {
			if (files[e] + files[s] <= X) {
				++s;
			}
			++count;
		}
		out << "Case #" << (i + 1) << ": " << count << endl;
	}
	return 0;
}