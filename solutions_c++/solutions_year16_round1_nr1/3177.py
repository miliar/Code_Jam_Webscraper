#include <cstdio> // freopen
#include <iostream>
#include <string> // getline
#include <sstream> // stringstream
#include <vector>
#include <utility> // pair
#include <algorithm> // min
#include <bitset>
using namespace std;

//#define TEST
//#define SMALL
#define LARGE


string lastAl(const string S);
int main() {
	string filename = "A";
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
	string S;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> S;
		//J = 500; // for large
		cout << "Case #" << i << ": " << lastAl(S) << endl;
		
	}
	return 0;
}
string lastAl(const string S) {
	char maxch = 0;
	string res = "";
	for (char ch : S) {
		if (ch >= maxch) {
			maxch = ch;
			res.insert(res.begin(), ch);
		}
		else {
			res.insert(res.end(), ch);
		}
	}
	return res;
}