#include <set>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <climits>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int maxn = 110;
long long A, B;
char buf1[20];
char buf2[20];
int ok(char a[]) {
	int n = strlen(a);
	for (int i = 0, j = n - 1; i < j; i++, j--) {
		if (a[i] != a[j])
			return 0;
	}
	return 1;
}
int count() {
	int cnt = 0;
	long long beg = static_cast<long long>(sqrt(A) - 1);
	long long end = static_cast<long long>(sqrt(B) + 1);
	for (long long i = beg; i <= end; i++) {
		long long si = i * i;
		if (si < A || si > B)
			continue;
		sprintf(buf1, "%I64d", i);
		sprintf(buf2, "%I64d", si);
		if (ok(buf1) && ok(buf2))
			cnt++;
	}
	return cnt;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	int nc = 0;
	scanf("%d", &T);
	while (T--) {
		scanf("%I64d%I64d", &A, &B);
		printf("Case #%d: ", ++nc);
		printf("%d\n", count());
	}
	return 0;
}
