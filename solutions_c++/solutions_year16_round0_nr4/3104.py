#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

void solveSingleCase() {
	long long K, C, S;
	cin >> K >> C >> S;

	assert(K == S);

	for (int i=0; i < K; ++i) {
		long long pos = 0;
		long long offset = 1;
		for (int j=0; j < C; ++j) {
			pos += i * offset;
			offset *= K;
		}
		cout << " " << (pos + 1);
	}

	cout << endl;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ":";
		solveSingleCase();
	}
	
	return 0;
}
