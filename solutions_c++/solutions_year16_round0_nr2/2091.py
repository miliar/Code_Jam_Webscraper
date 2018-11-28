#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;


ifstream infile;
ofstream outfile;
string s;

int T;
int N;

int ans[11][1 << 10];

int map[1 << 10][1 << 10];

void build_map(int N) {
	for (int i = 0; i < (1 << N); ++i) {
		for (int j = 0; j < (1 << N); ++j) {
			if (i != j)
				map[i][j] = 1 << 20;
			else
				map[i][j] = 0;
		}
	}

	for (int i = 0; i < (1 << N); ++i) {
		int a[11];
		int tmp = i;
		for (int j = 1; j <= N; ++j) {
			a[N - j + 1] = tmp % 2;
			tmp /= 2;
		}

		int b[11];
		for (int j = 1; j <= N; ++j) {
			for (int k = j + 1; k <= N; ++k)
				b[k] = a[k];
			for (int k = 1; k <= j; ++k)
				b[k] = 1 - a[j + 1 - k];

			tmp = 0;
			for (int k = 1; k <= N; ++k)
				tmp = tmp * 2 + b[k];

			map[i][tmp] = map[i][tmp] < 1 ? map[i][tmp] : 1;
		}
	}

	for (int k = 0; k < (1 << N); ++k) {
		for (int i = 0; i < (1 << N); ++i) {
			for (int j = 0; j < (1 << N); ++j) {
				map[i][j] = (map[i][j] < map[i][k] + map[k][j]) ? map[i][j] : (map[i][k] + map[k][j]);
			}
		}
	}

//	if (N <= 4) {
//		for (int i = 0; i < 1 << N; ++i) {
//			for (int j = 0; j < 1 << N; ++j)
//				outfile << map[i][j];
//			outfile << endl;
//		}
//	}
}

void reset() {
	return;
}

int proc(int stage, int N) {
	if (N % 2 == 1)
		return ans[stage - 1][N / 2];

	int tmp_min = 1 << 20;
	for (int i = 0; i < (1 << stage); ++i) {
		if (i % 2 == 1)
			tmp_min = (tmp_min < map[N][i] + ans[stage - 1][i / 2]) ? tmp_min : (map[N][i] + ans[stage - 1][i / 2]);
	}
	
	return tmp_min;
}


int main() {
	infile.open("input.txt");
	outfile.open("output.txt");

	for (int stage = 1; stage <= 10; ++stage)
		for (int N = 1; N < (1 << 10); ++N)
			ans[stage][N] = -1;

	ans[1][0] = 1;
	ans[1][1] = 0;

	for (int stage = 2; stage <= 10; ++stage) {
		ans[stage][0] = 1;
		ans[stage][(1 << stage) - 1] = 0;

		build_map(stage);

		for (int N = 1; N < (1 << stage) - 1; ++N)
			ans[stage][N] = proc(stage, N);
	}

	infile >> T;

	for (int p = 1; p <= T; ++p) {
//		reset();

		outfile << "Case #" << p << ": ";

		do {
			getline(infile, s);
		} while (s.length() < 1 || (s[0] != '+' && s[0] != '-'));

		N = 0;
		for (int i = 0; i < s.length(); ++i)
			N = N * 2 + ((s[i] == '+') ? 1 : 0);

		outfile << ans[s.length()][N] << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}