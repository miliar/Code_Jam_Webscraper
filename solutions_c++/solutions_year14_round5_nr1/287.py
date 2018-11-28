#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <thread>
#include <future>
#include <iomanip>
#include <cassert>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

// const char* inputFile  = "file.in";
// const char* outputFile = "file.out";

// const char* inputFile  = "A-small-attempt0.in";
// const char* outputFile = "A-small-attempt0.out";

const char* inputFile  = "A-large.in";
const char* outputFile = "A-large.out";

class Solver {
public:
	Solver() {
	}

	void readInput() {
		cin >> N >> p >> q >> r >> s;
	}

	string solveTest() {
		for (int i = 0; i < N; ++i) {
			transistors.push_back((i * 1ll * p + q) % r + s);

			sums.push_back(transistors[i]);
			if (i > 0) {
				sums[i] += sums[i - 1];
			}
			// cerr << i << " " << transistors[i] << endl;
		}

		answer = 0;
		// DB(sums[N - 1]);

		for (int i = 0; i < N; ++i) {
			long long S1 = 0;
			if (i > 0) {
				S1 = sums[i - 1];
			}

			long long S2 = 0;
			long long S3 = 0;
			int L = i;
			int R = N - 1;
			while (L + 1 < R) {
				int M = (L + R) / 2;
				S2 = sums[M] - S1;
				S3 = sums[N - 1] - S1 - S2;
				if (S2 > S3) {
					R = M;
				} else {
					L = M;
				}
			}
			updateAnswer(i, L - 2);
			updateAnswer(i, L - 1);
			updateAnswer(i, L);
			updateAnswer(i, L + 1);
			updateAnswer(i, L + 2);
		}

		stringstream ss;
		// DB(answer);
		// DB(sums[N - 1]);
		ss << fixed << setprecision(12) << fixed << (long double)(answer) / sums[N - 1];
		return ss.str();
	}

	void updateAnswer(int L, int R) {
		if (L < 0) {
			return;
		}
		if (R >= N) {
			return;
		}
		if (R < 0) {
			return;
		}
		long long S1 = 0;
		long long S2 = 0;
		long long S3 = 0;

		if (L > 0) {
			S1 = sums[L - 1];
		}
		S2 = sums[R] - S1;
		S3 = sums[N - 1] - S1 - S2;

		vector<long long> S = {S1, S2, S3};
		sort(S.begin(), S.end());

		assert(S1 + S2 + S3 == sums[N - 1]);

		long long curAnswer = sums[N - 1] - S[2];
		if (curAnswer > answer) {
			// DB(L);
			// DB(R);
			// DB(curAnswer);
			answer = curAnswer;
		}
	}

	long long answer;
	int N, p, q, r, s;
	vector<int> transistors;
	vector<long long> sums;
};

void simpleSolve() {
	int T;
	scanf("%d", &T);
	for (int testNumber = 1; testNumber <= T; ++testNumber) {
		Solver solver;
		solver.readInput();
		string verdict = solver.solveTest();
		printf("Case #%d: %s\n", testNumber, verdict.c_str());
	}
}

void asyncSolve() {
	int T;
	scanf("%d", &T);
	vector< std::future<string> > results;
	vector< Solver > solvers;
	for (int testNumber = 1; testNumber <= T; ++testNumber) {
		Solver solver;
		solver.readInput();
		solvers.push_back(solver);
	}

	for (int testNumber = 1; testNumber <= T; ++testNumber) {
		results.emplace_back(std::async(std::launch::async, &Solver::solveTest, solvers[testNumber - 1]));
	}

	for (int testNumber = 1; testNumber <= T; ++testNumber) {
		string verdict = results[testNumber - 1].get();
		printf("Case #%d: %s\n", testNumber, verdict.c_str());
	}
}

int main() {
	freopen(inputFile, "r", stdin);
	freopen(outputFile, "w", stdout);
	simpleSolve();
	// asyncSolve();
	return 0;
}
