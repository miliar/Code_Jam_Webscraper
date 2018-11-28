#include <algorithm>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template <class T>
T split(string str, char delim) {
	T t;
	string token;
	stringstream ss(str);
	while (getline(ss, token, delim))
		t.push_back(stoi(token));
	return t;
}

bool test(vector<vector<int> > lawn, int x, int y) {
	int maxr = 0;
	int maxc = 0;
	int cur = lawn[x][y];
	for (int n=0; n<lawn[0].size(); n++) {
		if (n != y && lawn[x][n] >= maxr)
			maxr = lawn[x][n];
	}
	for (int m=0; m<lawn.size(); m++) {
		if (m != x && lawn[m][y] >= maxc)
			maxc = lawn[m][y];
	}
	if (cur >= maxr || cur >= maxc) return true;
	else return false;
}

int main(int argc, char **argv) {
	// Setup input and output files
	if (argc != 2) {
		cout << "Input file!" << endl;
		return 1;
	}
	string filename(argv[1]);
	ifstream is(filename);
	ofstream os(filename.replace(filename.end()-2, filename.end(), "out"));

	string buf;

	// Loop over test cases
	getline(is, buf);
	int numTests = stoi(buf);
	for (int n=1; n<=numTests; n++) {
		os << "Case #" << n << ": ";
		cout << "Case #" << n << ": ";

		vector<vector<int> > lawn;
		getline(is, buf);
		int N = stoi(buf.substr(0, buf.find(' ')));
		int M = stoi(buf.substr(buf.find(' ')));
		bool mowed = true;
		for (int x=0; x<N; x++) {
			getline (is, buf);
			lawn.push_back(split<vector<int> >(buf, ' '));
		}

		for (int x=0; x<N; x++) {
			for (int y=0; y<M; y++) {
				if (!test(lawn, x, y))
					mowed = false;
			}
		}
		if (mowed) {
			os << "YES" << endl;
			cout << "YES" << endl;
		} else {
			os << "NO" << endl;
			cout << "NO" << endl;
		}
	}

	// wrap it up
	is.close();
	os.close();
	return 0;
}

// USEFULL STUFF
// for (XXX::iterator it=XXX.begin(); it!=XXX.end(); it++) {
