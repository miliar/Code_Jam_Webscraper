#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
#include <vector>

using std::scanf;
using std::printf;

const int N = 32;

static int modpow(int n, int e, int m) {
	long long b = n;
	long long r = 1;
	while(e) {
		if(e & 1) {
			r *= b;
			r %= m;
		}
		e /= 2;
		b *= b;
		b %= m;
	}
	return r;
}

static int mod(const char *s, int base, int m) {
	long long r = 0;
	int e = strlen(s + 1);
	while(*s) {
		r += (*s - '0') * modpow(base, e, m);
		r %= m;
		++s;
		--e;
	}
	return r;
}

static void itoa(unsigned a, int base, char *out) {
	char r[N];
	int l = 0;
	while(a) {
		r[l++] = a % base + '0';
		a /= base;
	}
	while(l)
		*out++ = r[--l];
	*out++ = '\0';
}

static void load(std::vector<short>& primes) {
	FILE *f = std::fopen("primes.txt", "r");
	assert(f);
	char line[21];
	while(std::fgets(line, sizeof(line), f))
		primes.push_back(atoi(line));
	std::fclose(f);
}

static std::vector<short> small_primes;

static int small_divisor(char *s, int base) {
	for(auto div : small_primes)
		if(mod(s, base, div) == 0)
			return div;
	return -1;
}

static void testcase(int t) {
	int N, J;
	scanf("%i%i", &N, &J);
	std::puts("Case #1:");
	int v = 0;
	int proof[10 + 1];
	char n2[N + 1];
	for(int found = 0; found < J; ++v) {
		unsigned n = (1U << (N - 1)) | (v << 1) | 1;
		itoa(n, 2, n2);
		bool has_proof = true;
		for(int base = 2; has_proof && base <= 10; ++base) {
			int div = small_divisor(n2, base);
			proof[base] = div;
			has_proof = div >= 2;
		}
		if(has_proof) {
			printf("%s", n2);
			for(int base = 2; base <= 10; ++base)
				printf(" %d", proof[base]);
			putchar('\n');
			++found;
		}
	}
}

int main() {
	load(small_primes);
	int T;
	scanf("%i", &T);
	for(int t = 1; t <= T; ++t)
		testcase(t);
}
