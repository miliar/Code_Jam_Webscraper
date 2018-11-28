#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int check(int D, vector<int>& v, int t) {

	int it = 0;
	for (auto element : v) {
		it += (element - 1) / t;
	}
	return it;
}

int solve() {

	int D;
	in >> D;
	vector<int> v(D);
	for (int i = 0; i < D; ++i)
		in >> v[i];

	int ans = 1000000;

	for (int t = 1; t <= 1000; ++t)
		ans = min(ans, t + check(D, v, t));

	return ans;

}

int main() {



	int T;
	in >> T;

	for (int i = 1; i <= T; ++i) {
		cerr << "i = " << i << "\n";
		out << "Case #" << i << ": " << solve() << "\n";
	}

	return 0;
}