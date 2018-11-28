#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define LEN 2000
int ds[LEN];
int T, D, step, max0, min0, sum;

int main()
{
	scanf("%d", &T);
	for (int it = 0; it < T; it++) {
		scanf("%d", &D);
		max0 = -1;
		for (int j = 0; j < D; j++) {
			scanf("%d", &ds[j]);
			max0 = max(ds[j], max0);
		}
		min0 = max0;
		for (int i = 1; i <= max0; i++) {
			sum = i;
			for (int j = 0; j < D; j++) {
				if (ds[j] > i) {
					if ( ds[j] % i ) 
						sum += (ds[j]/i);
					else
						sum += (ds[j]/i-1);
				}
			}
			min0 = min(min0, sum);
		}
		printf("Case #%d: %d\n",it+1, min0);
	}
	return 0;
}