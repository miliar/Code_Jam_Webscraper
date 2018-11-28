#define _CRT_SECURE_NO_DEPRECATE
//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

#include <stdint.h>
#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;

#include <gmpxx.h>
typedef mpz_class mpz;
mpz z_sq(mpz x) { return x*x; }

char w[128];
int is_pali(mpz n) {
	gmp_sprintf(w, "%Zd", n.get_mpz_t());
	int l = 0; for (l = 0; w[l]; l++);
	for (int i = 0; i < l-1 - i; i++)
		if (w[i] != w[l-1 - i]) return 0;
	return 1;
}

void gen_brute_force() {
	for (mpz n = 1; ; n++) {
		mpz np1 = n, np2 = n, t = n;
		for (int i = 0; t > 0; i++) {
			mpz r = t % 10; t /= 10;
			if (i > 0) np1 = np1 * 10 + r;
			np2 = np2 * 10 + r;
		}
		if (is_pali(z_sq(np1))) gmp_sprintf(w, "%Zd\n", np1.get_mpz_t()), printf("%s", w), fflush(stdout);
		if (is_pali(z_sq(np2))) gmp_sprintf(w, "%Zd\n", np2.get_mpz_t()), printf("%s", w), fflush(stdout);
	}
}

#define SZ 100
void gen_by_pattern() {
	mpz w[SZ/2];
	w[0] = 1;
	for (int i = 1; i < SZ/2; i++)
		w[i] = w[i - 1] * 10;
	
	vector<mpz> v;
	v.push_back(2);
	v.push_back(3);
	
	// '.' stands for zero (used for clarity only)
	// pattern 1 (all possible combinations of 1 and 0, needs check)
	for (int u = 1; u < (1 << (SZ/2+1)/2); u++) {
		mpz n = 0, w = 1;
		for (int t = u; t > 0; t >>= 1, w *= 10)
			if (t & 1) n += w;
		mpz np1 = n, np2 = n, t = n;
		for (int i = 0; t > 0; i++) {
			mpz r = t % 10; t /= 10;
			if (i > 0) np1 = np1 * 10 + r;
			np2 = np2 * 10 + r;
		}
		if (is_pali(z_sq(np1))) v.push_back(np1);
		if (is_pali(z_sq(np2))) v.push_back(np2);
		if (u % 100000 == 0) fprintf(stderr, "%d ms\n", clock());
	}
	
	// pattern 2 (2.............2)
	for (int i = 0; i <= SZ/2-2; i++)
		v.push_back(2 * w[i+1] + 2 * w[0]);
	
	// pattern 3 (2......1......2)
	for (int i = 0; i <= (SZ/2-3)/2; i++)
		v.push_back(2 * w[i+1+i+1] + 1 * w[i+1] + 2 * w[0]);
	
	// pattern 4 (1......2......1)
	for (int i = 0; i <= (SZ/2-3)/2; i++)
		v.push_back(1 * w[2*i+2] + 2 * w[i+1] + 1 * w[0]);
	
	// pattern 5 (1...1..2..1...1)
	for (int i = 0; i <= (SZ/2-5)/2; i++)
		for (int j = 0; j <= i; j++)
			v.push_back(1 * w[2*i+4] + 1 * w[2*i-j+3] + 2 * w[i+2] + 1 * w[j+1] + 1 * w[0]);

	sort(v.begin(), v.end());
	gmp_printf("%d\n", v.size());
	for (int i = 0; i < (int) v.size(); i++)
		gmp_printf("%Zd\n", v[i].get_mpz_t());
	for (int i = 0; i < (int) v.size(); i++)
		if (!is_pali(v[i]) || !is_pali(z_sq(v[i]))) gmp_printf("ERROR: %Zd\n", v[i].get_mpz_t());
	fprintf(stderr, "%d ms\n", clock());
}

int main() {
	// "palindromes.txt" is precomputed once and then just loaded later
	//gen_by_pattern();

	vector<mpz> v;
	FILE *fin = fopen("palindromes.txt", "r");
	int n; fscanf(fin, "%d", &n);
	for (int i = 0; i < n; i++) {
		fscanf(fin, "%s", w);
		v.push_back(mpz(w));
	}
	fclose(fin);
	
	for (int i = 0; i < (int) v.size(); i++)
		v[i] = z_sq(v[i]);
	sort(v.begin(), v.end());
	
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s", w); mpz a = mpz(w);
		scanf("%s", w); mpz b = mpz(w);
		int r = upper_bound(v.begin(), v.end(), b)
			  - lower_bound(v.begin(), v.end(), a);
		printf("Case #%d: %d\n", t, r);
	}
	return 0;
}
