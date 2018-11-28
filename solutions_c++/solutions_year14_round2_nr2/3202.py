#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int lottery(int A, int B, int K) {
	int count = 0;
	for (int i = 0; i < A; i++)
		for (int j = 0; j < B; j++)
			if ((i & j) < K)
				count++;
	return count;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int A, B, K;
		cin >> A >> B >> K;
		printf("%d\n", lottery(A,B,K));
  }
}

	
