#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;


long long better_count(int n, int loose_count) {
	long long counter = 0;
	long long curr_pow = ((long long) 1) << (n - loose_count);
	for (int i = n - loose_count; i < n; i++) {
		counter += curr_pow;
		curr_pow <<= 1;
	}
		// printf("lc %d %d\n", loose_count, counter);

	return counter;
}

bool always(int n, long long i, int p) {
	long long loose_count = floor(log2(i + 1));
		// printf("%d p %d\n", loose_count, p);

	if (better_count(n, loose_count) < p) {
		return true;
	}
	return false;
}

long long best_always(int n, int p) {
	long long l = 0;
	long long h = ((long long) 1) << n;
	h -= 1;
	long long m;
	while (l < h) {
		m = l + (h - l + 1) / 2;
		// printf("m %d answ %d\n", m, always(n, m, p));
		if (always(n, m, p)) {
			l = m;
		} else {
			h = m -1;
		}
	}
	if (!always(n, l, p)) {
		printf("Oh no!");
	}
		return l;

}

bool can(int n, long long i, int p) {
	long long people_count = ((long long) 1) << n;

	long long people_worse = people_count - i;
	long long win_count = floor(log2(people_worse));

	long long better_or_eq_count = ((long long) 1) << (n - win_count);
	if (better_or_eq_count <= p) {
		return true;
	}
	return false;
}

long long best_can(int n, int p) {
	long long l = 0;
	long long h = ((long long) 1) << n;
	h -= 1;
	long long m;
	while (l < h) {
		m = l + (h - l + 1) / 2;
		// printf("m %d answ %d\n", m, always(n, m, p));
		if (can(n, m, p)) {
			l = m;
		} else {
			h = m -1;
		}
	}
	if (!can(n, l, p)) {
		printf("Oh no!");
	}
		return l;

}

int main() {
	int T, n, p;

	// FILE *fin = fopen("input.in", "r");
	FILE *fin = fopen("B-small-attempt0.in", "r");
	// FILE *fin = fopen("B-small-attempt1.in", "r");
	// FILE *fin = fopen("B-small-attempt2.in", "r");
	// FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	fscanf(fin, "%d", &T);
	for (int test_case = 0; test_case < T; test_case++) {
		cout << "Case #" << test_case + 1 << endl;
		fscanf(fin, "%d%d", &n, &p);


		
		fprintf(fout, "Case #%d: %lld %lld\n", test_case + 1, best_always(n, p), best_can(n, p));
		// fprintf(fout, "Case #%d: %lld\n", test_case + 1, best_always(n, p));
	}
	fclose(fin);
	fclose(fout);

	return 0;
}