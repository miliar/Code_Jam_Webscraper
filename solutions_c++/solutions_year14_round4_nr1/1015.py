#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#include<cfloat>

#include<iostream>
#include<string>
#include<limits>
#include<sstream>

#include<utility>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>

using namespace std;
typedef long long LL;
#undef DEBUG
int bucket[710];
int main() {
	int caseNum;
	char dummy; //read the '\n' after the caseNum
	scanf("%d%c", &caseNum, &dummy);
	for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
		int n;
		int size;
		scanf("%d%d", &n, &size);
		int i, j;
		memset(bucket, 0, sizeof(bucket));
		for (i = 0; i < n; i++) {
			int t;
			scanf("%d", &t);
			bucket[t]++;
		}
		int count = 0;
		for (i = 1; i <= size / 2; i++) {
			while (bucket[i] > 0) {
#ifdef DEBUG

#endif
				for (j = size - i; j > i; j--) {
					if (bucket[j] > 0) {
						bucket[j]--;
						bucket[i]--;
						count++;
#ifdef DEBUG
						printf("find a pair, i =%d , j = %d\n", i, j);
#endif
						break;
					}
				}
				if (j == i) {
					if (bucket[i] >= 2) {
						bucket[i] -= 2;
						count++;
#ifdef DEBUG
						printf("find the same i = %d\n", i);
#endif
					} else {
						break;
					}
				}
			}
		}
#ifdef DEBUG
		printf("count = %d\n", count);
#endif
		for (i = 1; i <= size; i++) {
			count += bucket[i];
#ifdef DEBUG
			printf("last i = %d\n", i);
#endif
		}
		printf("Case #%d: %d\n", caseCount, count);
	}
	return 0;
}
