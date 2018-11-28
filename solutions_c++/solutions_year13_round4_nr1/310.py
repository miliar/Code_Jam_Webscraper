#include <stdio.h>
#include <set>

using namespace std;

const long long int mod = 1000002013LL;

inline long long f(long long a, long long b, long long n) {
	long long d = b - a;
	return ((2 * n - d + 1) * (d) / 2) % mod;
}

int main() {
	int ecase, ecount;

	long long en;
	int em;
	long long es[1010], ee[1010], ep[1010];
	long long ori;

	long long pp[2020];
	int pmany;
	long long many[2020];
	
	long long after;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%I64d%d", &en, &em);

		set<long long> crip;
		ori = 0;
		for (int i = 0; i < em; i++) {
			scanf("%I64d%I64d%I64d", &es[i], &ee[i], &ep[i]);
			crip.insert(es[i]);
			crip.insert(ee[i]);
			long long t = f(es[i], ee[i], en);
			t *= ep[i];
			t %= mod;
			ori += t;
			ori %= mod;
		}

		pmany = crip.size();
		int count = 0;
		for (set<long long>::iterator it = crip.begin(); it != crip.end(); it++)
			pp[count++] = *it;
		for (int i = 0; i < em; i++) {
			for (int j = 0; j < pmany-1; j++)
				if (es[i] <= pp[j] && pp[j+1] <= ee[i])
					many[j] += ep[i];
		}

		//		for (int k = 0; k < pmany; k++)
		//			printf("%2I64d ", many[k]);
		//		printf("\n");
		after = 0;
		for (int i = 0; i < pmany; i++)
			while (many[i] > 0) {
				int j;
				long long sm = many[i];
				for (j = i+1; many[j] != 0; j++)
					if (many[j] < sm)
						sm = many[j];
				for (int k = i; k < j; k++)
					many[k] -= sm;
				long long t = f(pp[i], pp[j], en);
				t *= sm;
				//printf("<%I64d--%I64d> * %I64d\n", pp[i], pp[j], sm);
				t %= mod;
				after += t;
				after %= mod;

				//for (int k = 0; k < pmany; k++)
				//	printf("%2I64d ", many[k]);
				//printf("\n");
			}
		
		long long ans = ((ori + mod) - after) % mod;

		//printf("Case #%d: %I64d %I64d %I64d\n", ecount, ans, ori, after);
		printf("Case #%d: %I64d\n", ecount, ans);
	}

	return 0;
}
