#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <sstream>
using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int A, B, K;
		scanf ("%d %d %d", &A, &B, &K);
		int sum = 0;
		for (int i = 0; i < A; ++i) {
			for (int j = 0; j < B; ++j) {
				if ((i & j) < K)
					sum++;
			}
		}
		//if (K > A) K = A;
		//if (K > B) K = B;
		//int bit = 0, val = 1;
		//while (val < K) {
		//	val *= 2;
		//	bit++;
		//}
		//// 1 << bit < K
		//int sum = 1;
		//for (int i = 0; i < bit; ++i)
		//	sum *= 4;

		//for (int lottery = val; lottery < K; ++lottery) {
		//	for (int bit = 1; bit < lottery; bit <<= 1) {
		//		if (lottery & bit)
		//			sum += 1;
		//		else
		//			sum += 3;
		//	}
		//}
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}