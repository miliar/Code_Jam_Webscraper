#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <iomanip>
#include <queue>
#include "string.h"
#include "assert.h"
#include "math.h"

using namespace std;

#define abs(x)		((x) > 0 ? (x) : -(x))
#define max(x,y)	((x) > (y) ? (x) : (y))
#define min(x,y)	((x) < (y) ? (x) : (y))
typedef unsigned __int64 uint64;


void solve(unsigned N) {
	if (N == 0) {
		cout << "INSOMNIA"; return;
	}

	bool seen[10];
	for (int i = 0; i < 10; i++)
		seen[i] = false;
	int count = 0;

	unsigned z = N;
	while (true) {
		unsigned a = z;
		while (a > 0) {
			unsigned d = a % 10;
			if (!seen[d]) count++;
			seen[d] = true;
			a = a / 10;
			if (count == 10) {
				cout << z; return;
			}
		}
		z += N;
	}
}

int main(int argc, char** argv) {
	int T;
	cin >> T; // number of test cases
	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		int N; cin >> N;
		solve(N);
		cout << endl;
	}
}

	