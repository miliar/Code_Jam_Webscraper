#include <cstring>
#include <string>

#include <fstream>
#include <iostream>
#include <sstream>

#include <algorithm>
#include <bitset>
#include <utility>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define FOR(i, n) for (int i=0; i<n; i++)
#define RFOR(i, n) for (int i=n-1; i>=0; i--)
#define ITER(i, t, c) for (t::iterator i=c.begin(); i!=c.end(); i++)
#define SPLIT(i, buf) split<vector<int> >(buf)[i]

#define DEBUG
#ifdef DEBUG
#define DMSG(msg) cout << endl << "***DEBUG: " << msg << endl;
#else
#define DMSG(msg)
#endif // DEBUG

#define OUT(msg) cout << msg; os << msg;

int main(int argc, char **argv) {
	// Setup input and output files
	if (argc != 2) {
		cout << "Input file!" << endl;
		return 1;
	}
	string filename(argv[1]);
	ifstream is(filename);
	ofstream os(filename.replace(filename.end()-2, filename.end(), "out"));

	// Loop over test cases
	int T;
	is >> T;
	FOR (t, T) {
		os << "Case #" << t+1 << ": ";
		cout << "Case #" << t+1 << ": ";

		int A, N;
		is >> A >> N;
		int motes[N];
		FOR(n, N) {
			is >> motes[n];
		}

		int size = A;
		int res = 0;

		if (size == 1) {
			OUT(N);
			OUT(endl);
			continue;
		}

		sort(motes, motes+N);
		for (int n=0; n<N; n++) {
			DMSG(">>>" << size << " " << motes[n]);
			if (size > motes[n]) {
				DMSG("eat " << size << " " << motes[n]);
				size += motes[n];
				continue;
			}
			if (n == N-1) {
				DMSG("delete last");
				++res; 
				break;
			}

			int tmp = size;
			int adds = 0;
			while (tmp<=motes[n]) {
				adds++;
				tmp+=tmp-1;
			}

			DMSG("tmp " << adds << " " << tmp << " " << motes[n]);
			// Does deleting the remaining elements cost less than adding
			if (N-n <= adds) {
				DMSG("delete " << N-n);
				res += (N-n);
				break;
			}
			DMSG("add " << size << " => " << tmp << " + " << motes[n]);
			res += adds;
			size = tmp+motes[n];
		}

		OUT(res);
		OUT(endl);

	}

	// wrap it up
	is.close();
	os.close();
	return 0;
}
