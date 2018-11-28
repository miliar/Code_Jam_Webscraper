#include <iostream>
#include <vector>
#include <climits>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

long long solve(long long r, long long t) {
	long long sq = 2 * r - 1;
	double sqr = (double) ( sq * sq + 4 * 2 * t );
	long long ret = (1 - 2 * r ) + (long long)sqrt( sqr );
	ret /= 4;
	return ret;
}

int main() {
	int numCases;
	cin >> numCases;

	for(int c = 0; c < numCases; c++) {
		long long r, t;
		cin >> r >> t;
		cout << "Case #" << c+1 << ": " << solve(r,t) << endl;
	}

	return 1;
}