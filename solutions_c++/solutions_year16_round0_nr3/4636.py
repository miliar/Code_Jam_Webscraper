#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>

typedef long long ll;
using namespace std;

ll isPrime(ll target) {
	for (ll i = 2; i * i <= target; i++) {
		if (target % i == 0) return i;
	}
	return 0;
}

vector < pair < string, vector < ll > > > findAns(int N, int remain) {
	vector < pair < string, vector < ll > > > ret;
	for (ll add = 0; remain; add++) {
		ll now = (1LL << (N-1)) + (add * 2) + 1;
		
		int base;
		vector < ll > res;
		for (base = 2; base <= 10; base++) {
			ll recalc = 0, flag = 1, b = 1;
			while (flag < now) {
				flag <<= 1;
				b *= base;
			}

			while (flag) {
				if (flag & now) {
					recalc += b;
				}
				flag >>= 1;
				b /= base;
			}

			ll divider = isPrime(recalc);
			if (divider == 0) break;

			res.push_back(divider);
		}

		if (base == 11) {
			remain--;
			char buf[99], *ptr = buf;
			ll current = 1LL << (N-1);
			while (current) {
				*ptr = (now & current) ? '1' : '0';
				*ptr++;
				current >>= 1;
			}
			*ptr = 0;
			ret.push_back(make_pair(string(buf), res));

			printf("%d %d\n", N, remain);
		}
	}
	
	return ret;
}

int main() {
	FILE *f = fopen("output.txt", "w");

	const int NUM_SMALL = 50, NUM_LARGE = 500;

	auto resSmall = findAns(16, NUM_SMALL);

	fprintf(f, "Case #1:\n");

	for (auto val : resSmall) {
		fprintf(f, "%s", val.first.c_str());
		for (auto num : val.second) {
			fprintf(f, " %lld", num);
		}
		fprintf(f, "\n");
	}
	fprintf(f, "\n");

	/*
	auto resLarge = findAns(32, NUM_LARGE);

	fprintf(f, "%d\n", NUM_LARGE);

	for (auto val : resLarge) {
		fprintf(f, "%s", val.first.c_str());
		for (auto num : val.second) {
			fprintf(f, " %lld", num);
		}
		fputs("", f);
	}
	fputs("", f);
	*/

	fclose(f);

	return 0;
}