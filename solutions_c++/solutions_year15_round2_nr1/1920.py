#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

unsigned long reverse(unsigned long n){
	string temp = to_string(n);
	reverse(temp.begin(), temp.end());
	return stoul(temp);
}

int main() {
	ifstream ifs("input.in");
	ofstream ofs("output.out");
	int T;
	ifs >> T;
	// precompute
	vector<unsigned> minsteps(1000001, 0);
	for (unsigned i = 1; i <= 1000000; i++){
		minsteps[i] = minsteps[i - 1]+1;
		if ( i % 10 != 0 ){
			unsigned long rev = reverse(i);
			if ( rev < i )
				minsteps[i] = min(minsteps[i], minsteps[rev]+1);
		}
	}

	for (int tt = 1; tt <= T; tt++){
		unsigned long N;
		ifs >> N;
		ofs << "Case #" << tt << ": " << minsteps[N] << endl;
	}
	return 0;
}
