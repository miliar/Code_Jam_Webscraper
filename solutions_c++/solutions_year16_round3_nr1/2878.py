#include <bits/stdc++.h>
using namespace std;

bool ChkMajority(int A[], int N, int C1, int C2) {
	int B[100];
	for (int i = 0; i < N; ++i) {
		B[i] = A[i];
	}

	if (B[C1] == 0 || B[C2] == 0)
		return false;

	if (C1 >= 0)
		B[C1]--;
	if (C2 >= 0)
		B[C2]--;

	float Sum = 0;
	for (int i = 0; i < N; ++i) {
		Sum += B[i];
	}

	for (int i = 0; i < N; ++i) {
		if (B[i] / Sum > 0.5f)
			return false;
	}
	return true;
}

bool myf(int i) {
	return i > 0;
}

int main() {
	ifstream fin("A-small-attempt0.in", ios::in);
	ofstream fout("A-small-attempt0.out", ios::out);
	int TestCase;
	int N, A[100];
	fin >> TestCase;
	for (int T = 0; T < TestCase; ++T) {
		fin >> N;
		fout << "Case #" << T + 1 << ": ";
		for (int var = 0; var < N; ++var) {
			fin >> A[var];
		}
		while (find_if(A, A + N, myf) < A + N) {
			for (int C1 = 0; C1 < N; ++C1) {
				for (int C2 = -1; C2 < N; ++C2) {
					if (ChkMajority(A, N, C1, C2)) {
						fout << (char) (C1 + 'A');
						if (C2 >= 0)
							fout << (char) (C2 + 'A');
						fout << " ";
						if (C1 >= 0)
							A[C1]--;
						if (C2 >= 0)
							A[C2]--;
					}
				}
			}
		}
		fout << endl;
	}
}
