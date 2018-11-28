#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	fstream fin("A-large.in");
	ofstream fout("out.txt");
	istream& in = fin;
	ostream& out = fout;
	int a, b;

	int T;
	in >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		int n, x;
		in >> n >> x;
		vector<int> s(n);
		for (int i = 0; i < n; i++)	in >> s[i];
		sort(s.rbegin(), s.rend());
		
		int l = 0, r = n - 1, k = 0;
		while (l < r) {
			if (s[l] + s[r] <= x) r--;
			l++;
		}
		k = l;
		if (l == r) k++;

		out << "Case #" << test_case << ": " << k << endl;
	}

	return 0;
}
