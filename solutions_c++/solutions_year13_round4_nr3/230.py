#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_N = 2000;

int N;

int A[MAX_N];
int B[MAX_N];
int X[MAX_N];

bool LESS_THAN[MAX_N][MAX_N];

void read_input()
{
	cin >> N;

	for (int i = 0; i < N; ++i) {
		cin >> A[i];
	}

	for (int i = 0; i < N; ++i) {
		cin >> B[i];
	}
	
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			LESS_THAN[i][j] = false;
		}
	}
}

void solve()
{
	for (int i = 0; i < N; ++i) {
		for (int j = i-1; j >= 0; --j) {
			if (A[j] >= A[i]) {
				LESS_THAN[i][j] = true;
			}
		}
		for (int j = i-1; j >= 0; --j) {
			if (A[j]+1 == A[i]) {
				LESS_THAN[j][i] = true;
				break;
			}
		}
		for (int j = i+1; j < N; ++j) {
			if (B[j] >= B[i]) {
				LESS_THAN[i][j] = true;
			}
		}
		for (int j = i+1; j < N; ++j) {
			if (B[j]+1 == B[i]) {
				LESS_THAN[j][i] = true;
				break;
			}
		}
	}	

	for (int i = 0; i < N; ++i) {
		X[i] = 0;
	}

	for (int v = 1; v <= N; ++v) {
		int k = 0;
		while (X[k] > 0) ++k;
		while (true) {
			bool hop = false;
			for (int j = 0; j < N; ++j) {
				if (X[j] < 1 && LESS_THAN[j][k]) {
					k = j;
					hop = true;
					break;
				}
			}
			if (!hop) {
				break;
			}
		}
		X[k] = v;
	}
}

int main()
{
	int numOfTests;
	cin >> numOfTests;

	for (int t = 1; t <= numOfTests; ++t) {
		read_input();
		solve();
		cout << "Case #" << t << ": " << X[0];
		for (int i = 1; i < N; ++i) {
			cout << " " << X[i];
		}
		cout << endl;
	}	
}