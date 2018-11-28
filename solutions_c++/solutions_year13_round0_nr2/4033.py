//============================================================================
// Name        : GoogleCodeJam.cpp
// Author      : Luis Eduardo Oliveira Lizardo
// Version     :
// Copyright   :
// Description : Problem B. Lawnmower
//============================================================================

#include <iostream>
#include <stdio.h>
using namespace std;

int main() {

	int T, N, M, a;

	scanf("%d%*c", &T);

	for (int t = 1; t <= T; ++t) {
		scanf("%d %d%*c", &N, &M);

		int matrix[N][M];
		int biggestN[N];
		int biggestM[M];

		for (int i = 0; i < N; ++i) {
			biggestN[i] = 0;
		}
		for (int i = 0; i < M; ++i) {
			biggestM[i] = 0;
		}

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				scanf("%d", &a);

				matrix[i][j] = a;

				if (matrix[i][j] > biggestN[i]) {
					biggestN[i] = matrix[i][j];
				}

				if (matrix[i][j] > biggestM[j]) {
					biggestM[j] = matrix[i][j];
				}
			}
			scanf("%*c");
		}

		bool ok = true;

		for (int i = 0; i < N && ok; ++i) {
			for (int j = 0; j < M; ++j) {

				if (matrix[i][j] < biggestM[j] && matrix[i][j] < biggestN[i]) {
					ok = false;
					break;
				}
			}
		}

		if (ok) {
			printf("Case #%d: YES\n", t);
		}
		else {
			printf("Case #%d: NO\n", t);
		}

	}
	return 0;
}

/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1


1
2 3
2 1 2
2 2 2
 */

