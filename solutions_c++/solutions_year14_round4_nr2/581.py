#include <cstdio>
#include <algorithm>

int N;
int org[1001];
int arr[1001];
int narr[1001];
int midx;
int mx = 0;

inline int Abs(int x) { return x > 0 ? x : -x; }

void swap(int &a, int &b) {
	int tmp = a;
	a = b;
	b = tmp;
}

int go2(int dep) {

}

int go(int idx) {
	int cnt = 0;
	for (int i = 0; i < N; ++i) {
		if (i == idx) narr[i] = mx;
		else {
			if (arr[cnt] == mx) ++cnt;
			narr[i] = arr[cnt++]; 
		}
	}
	//for (int i = 0; i < N; ++i)
	//	printf("%d ", narr[i]);
	//putchar('\n');
	int ret = 0;
	for (int i = 0; i < idx; ++i) 
		for (int j = 1; j < idx; ++j) {
			if (narr[j - 1] > narr[j]) {
				swap(narr[j - 1], narr[j]);
				++ret;
			}
		}
	for (int i = idx + 1; i < N; ++i) 
		for (int j = idx + 2; j < N; ++j) {
			if (narr[j - 1] < narr[j]) {
				swap(narr[j - 1], narr[j]);
				++ret;
			}
		}
	/*for (int i = 0; i < N; ++i)
		printf("%d ", narr[i]);
	putchar('\n');*/
	return ret + Abs(idx - midx);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		mx = 0;
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &arr[i]);
			org[i] = narr[i] = arr[i];
		}
		std::sort(narr, narr + N);
		int ans = 0;
		int l = 0, r = N - 1;
		for (int i = 0; i < N; ++i) {
			int t = 0;
			while (arr[t] != narr[i]) ++t;
			//printf("%d %d %d %d\n", l, r, narr[i], t);
			if (t - l < r - t) {
				ans += (t - l);
				while (t > l) {
					swap(arr[t], arr[t - 1]);
					--t;
				}
				++l;
			} else {
				ans += (r - t);
				while (t < r) {
					swap(arr[t], arr[t + 1]);
					++t;
				}
				--r;
			}
		}/*
		for (int i = 0; i < N; ++i)
			arr[i] = org[i];
		for (int i = 0; i < N; ++i)
			if (arr[i] > mx) {
				mx = arr[i];
				midx = i;
			}
		int ans2 = 2147483647;
		for (int i = 0; i < N; ++i) {
			int tmp = go(i);
			if (ans2 > tmp) ans2 = tmp;
		}*/
		printf("Case #%d: %d\n", t, ans);
	}

}