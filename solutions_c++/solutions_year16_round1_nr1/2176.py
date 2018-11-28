#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void solve(int c, const string &w) {

	string working;
	working += w[0];
	int N = int(w.length());
	for (int i = 1; i < N; i++) {
		string c;
		c += w[i];
		string A = c + working;
		string B = working + c;
		if (A > B) {
			working = A;
		} else {
			working = B;
		}
	}
	cout << "Case #" << c << ": " << working << endl;
}

int main(int argc, const char * argv[]) {

// #if __CMD__
// 	istream &fin = cin;
// #else
// 	fstream fin("tiny.in");
// #endif

	istream &fin = cin;

	int N;
	fin >> N;
	string W;
	for (int c = 1; c <= N; c++) {
		fin >> W;
		solve(c, W);
	}
    return 0;
}
