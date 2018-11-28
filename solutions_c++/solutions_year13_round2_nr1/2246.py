#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>


using namespace std;


///////////////
// constants //
///////////////
static const bool DEBUG = false;


///////////////
// variables //
///////////////
int T;
int A;
int N;
vector<int> motes;


///////////////
// functions //
///////////////
int solve (int idx, int size, int operation)
{
	if (idx == (N-1)) {
		if (size > motes[N-1]) {
			return operation;
		}
		return operation+1;
	}
	if (operation >= N) {
		return N;
	}
	if (motes[idx] < size) {
		return solve (idx+1, size + motes[idx], operation);
	}
	int max_remove = N - idx;
	int max_size = size;
	for (int i = 0; i < max_remove; ++i) {
		max_size += max_size-1;
	}
	if (max_size <= motes[idx]) {
		return solve (idx+1, size, operation+1);
	}
	int add = solve (idx, size + size-1, operation+1);
	int remove = solve (idx+1, size, operation+1);
	return min (add, remove);
}


//////////
// main //
//////////
int main (int argc, char** argv)
{
	ifstream fin;
	istream& input ((argc > 1) ? fin : cin);
	if (argc > 1) {
		fin.open (argv[1]);
	}

	input >> T;
	for (int t = 1; t <= T; ++t) {
		input >> A >> N;
		motes = vector<int> (N, 0);
		for (int n = 0; n < N; ++n) {
			input >> motes[n];
		}
		sort (motes.begin(), motes.end());
		if (DEBUG) {
			for (int n = 0; n < N; ++n) {
				cerr << motes[n] << ' ';
			}
			cerr << endl;
		}
		cout << "Case #" << t << ": " << solve (0, A, 0) << endl;
	}

	return 0;
}
