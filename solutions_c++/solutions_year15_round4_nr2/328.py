#include <iostream>
#include <math.h>
#include <fstream>
#include <stdio.h>
#include <algorithm>

using namespace std;

ifstream fin ("B-small-attempt1.in");
//ofstream fout ("B-small-attempt0.out");

int T, N;
long double V, X;
long double R[100], C[100];

int main() {
	fin >> T;
	for (int t = 1; t <= T; ++t) {
		fin >> N;
		fin >> V >> X;
		for (int i = 0; i < N; ++i)
			fin >> R[i] >> C[i];
		long double result = -1;
		if (N == 1) {
			if (X == C[0])
				result = V / R[0];
		} else if (N == 2) {
			if (X == C[0] && X == C[1])
				result = V / (R[0] + R[1]);
			else if (X == C[0])
				result = V / R[0];
			else if (X == C[1])
				result = V / R[1];
			else if ((C[0] < X && C[1] > X) || (C[1] < X && C[0] > X)) {
				result = max((X - C[1]) * V / (C[0] - C[1]) / R[0],
					   (X - C[0]) * V / (C[1] - C[0]) / R[1]);
//				printf(" max(%Lf, %Lf)\n", (X - C[1]) * V / (C[0] - C[1]) / R[0], (X - C[0]) * V / (C[1] - C[0]) / R[1]);
			}
		}

		if (result == -1)
			printf("Case #%d: IMPOSSIBLE\n", t);
//			fout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		else
			printf("Case #%d: %Lf\n", t, result);
	}

	return 0;
}
