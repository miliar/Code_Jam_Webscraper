#include <cstring>
#include <string>

#include <fstream>
#include <iostream>
#include <sstream>

#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define FOR(i, n) for (int i=0; i<n; i++)
#define RFOR(i, n) for (int i=n-1; i>=0; i--)
#define ITER(i, t, c) for (t::iterator i=c.begin(); i!=c.end(); i++)
#define SPLIT(i, buf) split<vector<int> >(buf)[i]

#define SET(state, n) state |= 1<<n
#define CK(state, n) (state & 1<<n)
#define UNSET(state, n) state &= ~(1<<n)
#define FF(state, n) (state & (1<<n)-1)

#define DEBUG(msg) cout << endl << "***DEBUG: " << msg << endl;
#define OUT(msg) cout << msg; os << msg;

template <class T>
T split(string str, char delim=' ') {
	T t;
	string token;
	stringstream ss(str);
	while (getline(ss, token, delim))
		t.push_back(stoi(token));
	return t;
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
	int T = stoi(buf);
	FOR (t, T) {
		os << "Case #" << t+1 << ": ";
		cout << "Case #" << t+1 << ": ";

		getline(is, buf);
		int r = SPLIT(0, buf);
		int t = SPLIT(1, buf);

		int count = 0;
		double bucket = (double)t;
		do {
			bucket -= ((r+1)*(r+1)) - (r*r);
			r += 2;
			++count;
		} while (bucket >= 0);

		OUT(count-1);
		OUT(endl);


	}

	// wrap it up
	is.close();
	os.close();
	return 0;
}
