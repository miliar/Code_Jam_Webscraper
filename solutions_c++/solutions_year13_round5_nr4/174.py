#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX_N 22

using namespace std;

int tests;
int a, b, answer, n;
double cnt;
char in[MAX_N];
long double dp[1<<MAX_N];
long double cnt1[1<<MAX_N];

int main() {
	scanf("%d", &tests);
	for (int test = 0 ; test < tests ; test ++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: ", test + 1);
		scanf("%s", in);
		n = strlen(in);
		int b = 0;
		for (int i = 0 ; i < n ; i ++) {
			if (in[i] == 'X') {
				b += (1<<i);
			}
		}
		for (int i = 0 ; i < (1<<n) ; i ++) {
			cnt1[i] = 0;
			dp[i] = 0;
		}
		cnt1[b] = 1;
		for (int i = 0 ; i < (1<<n) - 1 ; i ++) {
			if ((i&b) == b) {
				for (int j = 0 ; j < n ; j ++) {
					//if ((((1<<j)&i) == 0) & in[j] == '.') {
						//int i1 = i - (1<<j);
						//cnt ++;
						int k;
						for (k = 0 ; k < n ; k ++) {
							int k1 = (k + j) % n;
							if (((1<<k1)&i) == 0) {
								break;
							}
						}
						dp[i + (1<<((k + j)%n))] += ((n - k) * cnt1[i] + dp[i]);
						cnt1[i + (1<<((k + j)%n))] += cnt1[i];
					//}
				}
			}
			//printf("%d %lf %lf\n", i, dp[i], cnt1[i]);
		}
		//printf("%d %lf %lf\n", (1<<n) - 1, dp[(1<<n) - 1], cnt1[(1<<n) - 1]);
		//for (int i = 0 ; i < n ; i ++) {
		//	if (in[i] == '.') dp[(1<<n) - 1] /= n;
		//}
		printf("%.12Lf\n", dp[(1<<n) - 1] / cnt1[(1<<n) - 1]);
	}
	return 0;
}