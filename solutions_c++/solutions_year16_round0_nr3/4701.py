#include <cstdio>
#include <vector>

using namespace std;

typedef long long llint;

int n, k, sol;

llint comp(int i, int b) {
	llint ret = 0;
	for (; i; i >>= 1) {
		ret = ret * b + (i & 1);
	}
	return ret;
}

int find(llint x) {
	for (llint i = 2; i * i <= x; ++i)
		if (x % i == 0) return i;
	return 1;
}

int main() {
	scanf("%*d%d%d", &n, &k);
	printf("Case #1:\n");
	for (int i = (1 << (n-1)) + 1; i < (1 << n) - 1 && sol != k; i += 2) {
		vector < llint > v;
		bool flag = 1;
		for (int b = 2; b <= 10 && flag; ++b) {
			llint n = comp(i, b);
			llint div = find(n);
			if (div == 1) flag = 0;
			v.push_back(div);
		}
		if (flag) {
			sol++;
			for (llint x = i; x; x >>= 1)
				printf("%lld", x & 1);
			printf(" ");
			for (auto j: v)
				printf("%lld ", j);
			printf("\n");
		}
	}

	return 0;
}
