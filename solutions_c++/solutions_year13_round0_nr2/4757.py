//b.cpp
//By λKT345

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

const int MAXN = 102;
const int MAXM = MAXN;

#define TR(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)

int N, M;
int arr[MAXN][MAXM];
int maxI[MAXN], maxJ[MAXM];

bool checkPossible() {
	for(int i = 0; i < N; ++i) {
		for(int j = 0; j < M; ++j) {
			if(arr[i][j] != min(maxI[i], maxJ[j])) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; ++t) {
		for(int i = 0; i < MAXN; i++) {
			maxI[i] = maxJ[i] = 0;
		}
		scanf("%d%d", &N, &M);
		for(int i = 0; i < N; ++i) {
			for(int j = 0; j < M; ++j) {
				scanf("%d", &arr[i][j]);
				maxI[i] = max(maxI[i], arr[i][j]);
				maxJ[j] = max(maxJ[j], arr[i][j]);
			}
		}
		if(checkPossible()) {
			printf("Case #%d: YES\n", t + 1);
		} else {
			printf("Case #%d: NO\n", t + 1);
		}
	}
	return 0;
}
