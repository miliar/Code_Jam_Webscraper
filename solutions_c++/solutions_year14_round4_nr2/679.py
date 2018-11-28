#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
	fstream fin("B-large.in");
	ofstream fout("out.txt");
	istream& in = fin;
	ostream& out = fout;
	int T;
	in >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		int n;
		in >> n;
		vector<int> a(n);
		for (auto& t : a) in >> t;
		int swaps = 0;
		for (int i = 0; i < n; i++) {
			int l = 0, r = 0;
			for (int j = 0; j < n; j++) {
				if (a[j] <= a[i]) continue;
				if (j < i) l++;
				else r++;
			}
			swaps += min(l, r);
		}
		out << "Case #" << test_case << ": " << swaps << endl;
	}
	return 0;
}