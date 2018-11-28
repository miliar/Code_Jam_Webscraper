#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

int N;
int A[1000];
int B[1000];

int D_inc[1000];
int D_dec[1000];

int abs(int a) {
	return (a) > 0 ? a : -(a);
}

int getAns(void) {
	int ret = 0;

	vector < int  > idx;

	for (int i = 0; i < N; i++)
		idx.push_back(A[i]);
	
	sort(idx.begin(), idx.end());

	for (int i = 0; i < N; i++) {

		int smallest_idx = -1;
		for (int j = 0; j < N; j++) {
			if (idx[i] == A[j]) {
				smallest_idx = j;
				break;
			}
		}

		int l = 0, r = 0;

		for (int j = 0; j < N; j++) {
			if (A[j] < idx[i])
				continue;
			l = abs(smallest_idx - j);
			break;
		}

		for (int j = N - 1; j >= 0; j--) {
			if (A[j] < idx[i])
				continue;
			r = abs(smallest_idx - j);
			break;
		}

		if (l < r) {
			for (int j = 0; j < l; j++) {
				swap(A[smallest_idx - j], A[smallest_idx - j - 1]);
				ret ++;
			}
		} else {
			for (int j = 0; j < r; j++) {
				swap(A[smallest_idx + j], A[smallest_idx + j + 1]);
				ret ++;
			}
		}
	}

	return ret;
}

int main(void) {
	int testNum;
	scanf("%d", &testNum);
	for (int testCase = 1; testCase <= testNum; testCase++) {

		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%d", &A[i]);
		}

		printf("Case #%d: %d\n", testCase, getAns());

	}

	return 0;
}
