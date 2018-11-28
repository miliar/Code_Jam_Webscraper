#include <cassert>
#include <string>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>

#ifndef M_PI
#	define M_PI 3.1415926535
#endif

using namespace std;


int main()
{
#define SAMPLE_NAME "A"
	if( freopen(SAMPLE_NAME "-large.in", "rt", stdin) ) {
		freopen(SAMPLE_NAME "-large.out", "wt", stdout);
	} else 	if( freopen(SAMPLE_NAME "-small.in", "rt", stdin) ) {
		freopen(SAMPLE_NAME "-small.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;

	for(int case_num = 1; case_num <= T; ++case_num)
	{
		cerr << case_num << endl;
		int A, N;
		cin >> A >> N;

		int mts[101];

		for(int i = 0; i < N; ++i) {
			cin >> mts[i];
		}
		sort(&mts[0], &mts[N]);

		int c = 0, d = 0;
		int best = N;

		while(c < N) {
			while(A > mts[c]) {
				A += mts[c++];
				best = min(best, d + (N - c) );
				if(N == c) break;
			}
			if(c < N) {
				//added[d].at = c;
				A += A - 1;
				++d;
			}
			if(d >= N) break;
		}
		cout << "Case #" << case_num << ':' << ' ' << best << endl;
	}
 	return 0;
}
