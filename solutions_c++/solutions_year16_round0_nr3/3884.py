#include <cstdlib>
#include <cstdio>
#include <unordered_set>

using std::unordered_set;

typedef unsigned u32;
typedef unsigned long long u64;
typedef unordered_set<u64> hash_set;

#define P 1000009
int n, m, c;
unsigned r[19], prime[P];
bool np[P],d[32];
u64 p[19][39];
hash_set s;

u64 get(int b) {
	u64 res = 0;
	for (int i = 0; i < n; ++i) res += d[i] * p[b][i];
	return res;
}

u32 div(u64 num) {
	for (int i = 0; i < c && (u64)prime[i] * prime[i] <= num; ++i)
		if (num % prime[i] == 0) return prime[i];
	return 1;
}

bool check() {
	for (int i = 2; i <= 10; ++i) if (r[i] == 1) return false;
	return true;
}

int main() {
	srand(233);
	printf("Case #%d:\n", 1);
	n = 16, m = 50;
	for (int i = 2; i * i < P; ++i) {
		if (!np[i]) {
			for (int j = i * i; j < P; j += i) np[j] = true;
		}
	}
	for (int i = 2; i < P; ++i) if (!np[i]) prime[c++] = i;
	for (int i = 2; i <= 10; ++i) {
		p[i][0] = 1;
		for (int j = 1; j < n; ++j) p[i][j] = p[i][j - 1] * i;
	}
	d[0] = d[n - 1] = true;
	while (m) {
		for (int i = 1; i < n - 1; ++i) d[i] = rand() & 1;
		for (int i = 2; i <= 10; ++i) {
			u64 num = get(i);
			r[i] = 1;
			if (i == 2 && s.count(num)) break;
			s.insert(num);
			if ((r[i] = div(num)) == 1) break;
		}
		if (check()) {
			--m;
			for (int i = n - 1; ~i; --i) putchar('0' + d[i]);
			for (int i = 2; i <= 10; ++i) printf(" %u", r[i]);
			putchar('\n');
		}
	}
	return 0;
}
