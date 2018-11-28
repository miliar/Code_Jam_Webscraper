#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <utility>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;


int N;
int arr[701];
int solve() {
	int tot=0;
	int i = 0;
	int j = N-1;
	for (int xx = 0; xx < N; ++xx) {
		int min = INT_MAX;
		int mi = -1;
		for (int k = i; k <= j; ++k) {
			if (arr[k] < min) {
				min = arr[k];
				mi = k;
			}
		}
		if (mi - i < j - mi) {
			for (int l = mi; l >i; --l) {
				arr[l] = arr[l-1];
				++tot;
			}
			++i;
		} else {
			for (int l = mi; l < j; ++l) {
				arr[l] = arr[l+1];
				++tot;
			}
			--j;
		}
	}
	return tot;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		scanf("%d", &N);
		for (int j = 0; j < N; ++j) {
			scanf("%d", &arr[j]);
		}
		int p = solve();
		printf("Case #%d: %d\n", i+1, p);
	}
	return 0;
}