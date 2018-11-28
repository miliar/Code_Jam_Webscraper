#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

#define mp(a,b) make_pair(a,b)

int val[1005];
int arr[1005];

void Solve() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cin >> val[i];
		arr[i] = val[i];
	}
	sort(arr, arr + n);
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		int l = 0, r = 0;
		for (int j = 0; j < n; ++j) {
			if (val[j] > arr[i]) {
				++l;
			} else if (val[j] == arr[i]) {
				r = n - l - 1 - i;
				break;
			}
		}
		ret += min(l, r);
	}
	printf("%d\n", ret);
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}