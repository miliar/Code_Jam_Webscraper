#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

vector<int> sortable;

void solve(int c, int N) {
	sort(sortable.begin(), sortable.end());
	int L = (int) sortable.size();
	vector<int> result;
	int ii = 0;
	while (ii < L) {
		int v = sortable[ii];
		int i = ii + 1;
		while (i < L && sortable[i] == v) { i++; }
		int count = i - ii;
		if ((count % 2) == 1) result.push_back(v);
		ii = i;
	}
	cout << "Case #" << c << ":";
	for (int i = 0; i < int(result.size()); i++)
		cout << " " << result[i];
	cout << endl;
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
 //	fstream fin("tiny.in");

// #if __CMD__
// 	istream &fin = cin;
// #else
// #endif

	int T;
	fin >> T;
	string W;
	for (int c = 1; c <= T; c++) {
		int N;
		fin >> N;
		sortable.clear();
		for (int i = 0; i < (2 * N - 1) * N; i++) {
			int v;
			fin >> v;
			sortable.push_back(v);
		}
		solve(c, N);
	}
    return 0;
}
