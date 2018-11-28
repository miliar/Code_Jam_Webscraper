#include <cstdio> // freopen
#include <iostream>
#include <string> // getline
#include <sstream> // stringstream
#include <vector>
#include <utility> // pair
#include <algorithm> // min
using namespace std;

//#define TEST
//#define SMALL
#define LARGE

int minRevenge(const string &S);

int main() {
	string filename = "B";
#ifdef TEST
	string testin = filename + ".txt";
	freopen(testin.c_str(), "rt", stdin);
#endif

#ifdef SMALL
	string smallin = filename + "-small-attempt0.in";
	if (freopen(smallin.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-small.in!" << endl;
		return -1;
	}
	string smallout = filename + "-small.out";
	freopen(smallout.c_str(), "wt", stdout);
#endif
#ifdef LARGE
	string largein = filename + "-large.in";
	if (freopen(largein.c_str(), "rt", stdin) == nullptr) {
		cout << "error open B-large.in!" << endl;
		return -1;
	}
	string largeout = filename + "-large.out";
	freopen(largeout.c_str(), "wt", stdout);
#endif

	int T;
	string line;
	cin >> T;
	getline(cin, line);
	for (int i = 1; i <= T; ++i) {
		string S;
		getline(cin, S);
		
		cout << "Case #" << i << ": " << minRevenge(S) << endl;
	}
	return 0;
}

int minRevenge(const string &S) {
	int len = S.size();
	int count = 1;
	for (int i = 1; i < len; ++i) {
		if (S[i] != S[i - 1]) {
			++count;
		}
	}
	if (S[len - 1] == '+') {
		--count;
	}
	return count;
}