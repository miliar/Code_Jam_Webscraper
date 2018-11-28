#include<iostream>
#include<cstdio>

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

using namespace std;
int P[1001];
int main()
{
	int tot_test;
	scanf("%d", &tot_test);
	int D;
	for (int test = 1; test <= tot_test; test++) {
		scanf("%d", &D);
		int maxCake = 0;
		for (int i = 0; i < D; i++) {
			scanf("%d", &P[i]);
			maxCake = max(P[i], maxCake);
		}
		int res = maxCake;
		for (int i = maxCake; i >= 1; i--) {
			int v = i;
			for (int j = 0; j < D; j++) {
				v += ((P[j] - 1)/i);
			}
			res = min(res, v);
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
