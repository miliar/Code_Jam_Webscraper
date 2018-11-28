#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int arr[8];

int main()
{
	int T; scanf("%d",&T);
	for(int K = 0; K < T; ++K) {
		printf("Case #%d:\n",K + 1);
		int r, n, m, k;
		scanf("%d %d %d %d",&r, &n, &m, &k);
		while(r--) {
			memset(arr, 0, sizeof(arr));
			for(int j = 0; j < k; ++j) {
				int aux; scanf("%d",&aux);
				if(aux <= 1) continue;
				for(int i = 2; i <= m; ++i) {
					int cnt = 0;
					while(aux % i == 0) cnt++, aux /= i;
					arr[i - 2] = max(arr[i - 2], cnt);
				}
			}
			int cnt = 0;
			for(int i = 0; i < m - 1; ++i) {
				cnt += arr[i];
			}
			if(cnt > n) {
				while(cnt > n) cnt--, arr[0]-=2, arr[2]++;
				for(int i = 0; i < m - 1; ++i) {
					while(arr[i]--) printf("%d",i + 2);
				}
			}
			else if(cnt < n) {
				for(int i = 0; i < n - cnt; ++i) {
					printf("2");
				}
				for(int i = 0; i < m - 1; ++i) {
					while(arr[i]--) printf("%d",i + 2);
				}
			}
			else {
				for(int i = 0; i < m - 1; ++i) {
					while(arr[i]--) printf("%d",i + 2);
				}
			}
			putchar('\n');
		}
	}
	return 0;
}
