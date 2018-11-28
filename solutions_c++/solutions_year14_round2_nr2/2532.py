#include <fstream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("out.txt");

void readCase(int &a, int &b, int &k) {
	fin >> a;
	fin >> b;
	fin >> k;
}

void output(vector <int> res) {
	for (int i = 0; i < res.size(); i++) {
		fout << "Case #" << i + 1 << ": ";
		fout << res[i] << endl;
	}
}

int lottery(int a, int b, int k) {
	int score = 0;
	for (int i = 0; i < a; i++) {
		for (int j = 0; j < b; j++) {
			if ((i & j) < k) {
				score++;
			}
		}
	}
	return score;
}

int main() {
	int cases = 0;
	vector <int> res;
	fin >> cases;
	for (int i = 0; i < cases; i++) {
		int a = 0, b = 0, k = 0;
		readCase(a, b, k);
		int score = lottery(a, b, k);
		res.push_back(score);
	}
	output(res);
	return 0;
}