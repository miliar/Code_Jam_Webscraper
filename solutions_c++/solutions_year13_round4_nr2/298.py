#include <stdio.h>
#include <set>

using namespace std;

int main() {
	int ecase, ecount;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		int ea;
		long long eb;
		scanf("%d%I64d", &ea, &eb);
		eb--;

		int tl = 0;
		for (int i = ea - 1; i >= 0; i--) {
			if (eb & (1LL << i))
				tl++;
			else
				break;
		}

		int tw = 0;
		for (int i = ea - 1; i >= 0; i--) {
			if (!(eb & (1LL << i)))
				tw++;
			else
				break;
		}
		if (tw != ea && eb != (1LL << (ea - tw)) - 1) {
			tw++;
		}

		long long aa;
		if (eb != (1LL << ea) - 1)
			aa = (1LL << (tl+1)) - 2;
		else
			aa = (1LL << ea) - 1;
		long long ab = (1LL << ea) - (1LL << tw);
		//printf("%d %d\n", tl, tw);
		printf("Case #%d: %I64d %I64d\n", ecount, aa, ab);
	}

	return 0;
}
