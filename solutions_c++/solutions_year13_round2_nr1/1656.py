#include <stdio.h>
#include <algorithm>
using namespace std;

int t;
long long a;
int n;
int m[1000010];

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))

int main() {
	scanf("%d", &t);

	for (int cases=0; cases<t; cases++) {
		scanf("%lld %d", &a,&n);
		
		for (int i=0; i<n; i++)
			scanf("%d", &m[i]);

		sort(m,m+n);
		int best=n;
		int addcnt=0;

		if (a==1) {
			printf("Case #%d: %d\n", cases+1,n);
			continue;
		}

		for (int i=0; i<n; i++) {
			while (a<=m[i]) {
				a+=a-1;
				addcnt++;
			}

			a+=m[i];
			best=min(best,addcnt+n-i-1);
		}
		PRINT("\n");		

		printf("Case #%d: %d\n", cases+1,best);
	}

	return 0;
}
