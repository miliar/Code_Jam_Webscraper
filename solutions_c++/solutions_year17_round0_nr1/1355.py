#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

void solve(int CASE, string s, int K) {
	int L = s.length();
	int S[1024];

	for (int i = 0; i < L; i++) {
		S[i] = s[i] == '-' ? 0 : 1;
	}

	int effort = 0;
	for (int i = 0; i < L; i++) {
		int sign = S[i];
		if (sign == 0) {
			int last = i + K - 1;
			if (last >= L) {
				effort = -1; break;
			}
			for (int j = 0; j < K; j++) {
				S[i + j] = 1 - S[i + j];
			}
			effort++;
		} else {
			;
		}
	}

	if (effort == -1) {
		printf("Case #%d: IMPOSSIBLE\n", CASE);
	} else {
		printf("Case #%d: %d\n", CASE, effort);
	}
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	string s;
	int K;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> s;
		fin >> K;
		solve(CASE, s, K);
	}
    return 0;
}
