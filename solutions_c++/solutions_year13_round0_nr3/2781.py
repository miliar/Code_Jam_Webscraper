#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long LL;

int sroot(LL a) {
	int le = 1, ri = 1e7 + 1;
	while (le + 1 != ri) {
		int mid = (le + ri) / 2;
		if (mid * (LL)mid <= a)
			le = mid;
		else
			ri = mid;
	}
	return le;
}

int prep[10000010];

bool tell(LL a) {
	static char s[100];
	sprintf(s, "%I64d", a);
	int len = strlen(s);
	for (int i = 0; i < len / 2; ++i)
		if (s[i] != s[len - 1 - i])
			return false;
	return true;
}

int get_answer(LL a) {
	if (a == 0) return 0;
	return prep[sroot(a)];
}

int main() {
	for (int i = 1; i <= 1e7; ++i) {
		prep[i] = tell(i) && tell(i * (LL)i);
		prep[i] += prep[i - 1];
	}
	int test; scanf("%d", &test);
	for (int cas = 1; cas <= test; ++cas) {
		LL a, b; scanf("%I64d%I64d", &a, &b);
		printf("Case #%d: %d\n", cas, get_answer(b) - get_answer(a - 1));
	}
	return 0;
}
