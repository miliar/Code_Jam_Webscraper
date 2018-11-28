#include <stdio.h>
#include <algorithm>

using namespace std;

long long array[38];
long long invest[38];
long long eb;
long long remain;

double fig() {
	long long re = 0;
	int can = 0;
	long long small = 100000000000000LL;
	for (int i = 0; i < 37; i++)
		if (array[i] < small)
			small = array[i];
	for (int i = 0; i < 37; i++) 
		if (array[i] == small) {
			re += invest[i] * 36;
			can++;
		}
	return (double)re / can - (eb - remain);
}

inline void maxx(double &a, double b) {
	if (b > a)
		a = b;
}

int main() {
	int ecase, ecount;
	int en;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		for (int i = 0; i < 37; i++) {
			array[i] = 0;
			invest[i] = 0;
		}
		scanf("%I64d%d", &eb, &en);
		for (int i = 0; i < en; i++)
			scanf("%I64d", &array[i]);
		array[37] = 1000000000000LL;
		sort(array, array+38);

		double ans = 0.0;
		remain = eb;

		long long ntry = array[0];
		for (int i = 1; i < 38; i++) {
			if (ntry < array[i]) {
				long long t = remain / i;
				long long d = array[i] - 1 - ntry;
				//printf("x: i=%d, %I64d+%I64d\n", i, ntry, t, d);
				if (t <= d) {
					for (int j = 0; j < i; j++) {
						array[j] += t;
						invest[j] += t;
						remain -= t;
					}
					maxx(ans, fig());

					int last = -1;
					for (int j = 0; j < i; j++) {
						if (invest[j] == 0) 
							break;
						array[j]--;
						invest[j]--;
						remain++;
						maxx(ans, fig());
						last = j;
					}
					for (int j = 0; j <= last; j++) {
						array[j]++;
						invest[j]++;
						remain--;
					}
					ntry += t;
				}
				else {
					//printf("B: i=%d, %d+%d\n", i, ntry, d);
					for (int j = 0; j < i; j++) {
						array[j] += d;
						invest[j] += d;
						remain -= d;
					}
					maxx(ans, fig());
					ntry += d;
					
					int last = -1;
					for (int j = 0; j < i; j++) {
						if (invest[j] == 0) 
							break;
						array[j]--;
						invest[j]--;
						remain++;
						maxx(ans, fig());
						last = j;
					}
					for (int j = 0; j <= last; j++) {
						array[j]++;
						invest[j]++;
						remain--;
					}
				}
				/*if (remain < i) {
					break;
				}
				else {
					int count = 0;
					for (int j = i; j < 37; j++)
						if (array[j] == array[i])
							count++;
					int last = i + count;
					for (int j = 0; j < i; j++) {
						remain--;
						array[j]++;
						invest[j]++;
					}
					maxx(ans, fig());
					ntry++;
				}*/
				for (int j = i-1; j >= 0; j--) {
					if (remain == 0)
						break;
					array[j]++;
					invest[j]++;
					remain--;
					maxx(ans, fig());
				}
				ntry++;
			}

//			printf("i=%d, %lf\n", i, ans);
		}

		//printf("%lf\n", ans);
		printf("Case #%d: %.15lf\n", ecount, ans);
		fprintf(stderr, "Case #%d: %.15lf\n", ecount, ans);
	}

	return 0;
}
