#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

void read(int arr[], int n) {
	int S0, A, C, R;
	cin >> S0 >> A >> C >> R;
	arr[0] = S0;
	for (int i = 1; i < n; ++i) {
		arr[i] = (1LL * A * arr[i - 1] + C) % R;
	}
}

const int MAX_N = int(1e6) + 10;
int n, D;
int S[MAX_N], P[MAX_N];
//[a,a+D]
int L[MAX_N], R[MAX_N];

int cnt[MAX_N * 2];

int main() {
	int nT;
	cin >> nT;
	for (int nc = 1; nc <= nT; ++nc) {
		cin >> n >> D;
		read(S, n);
		read(P, n);
		for (int i = 1; i < n; ++i) {
			P[i] %= i;
		}
		memset(cnt, 0, sizeof cnt);
		for (int i = 0; i < n; ++i) {
			int s = S[i];
			L[i] = s - D;
			R[i] = s;
			if (i > 0) {
				L[i] = max(L[i], L[P[i]]);
				R[i] = min(R[i], R[P[i]]);
			}

			if (L[i] <= R[i]) {
				cnt[L[i] + MAX_N]++;
				cnt[R[i] + 1 + MAX_N]--;
			}

		}

		for (int i = 1; i < MAX_N * 2; ++i) {
			cnt[i] += cnt[i - 1];
		}

		int ans = *max_element(cnt, cnt + MAX_N * 2);
		printf("Case #%d: %d\n", nc, ans);
	}
	return 0;
}
