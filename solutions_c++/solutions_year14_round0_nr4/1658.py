#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
#define LL long long

struct S {
	double a;
	int p;
} s[2500];

bool cmp(S a,S b) {
	return a.a < b.a;
}

int n,x[2][1005],cnt[2];

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		for (int i=0; i<2*n; i++) {
			scanf("%lf",&s[i].a);
			if (i < n) s[i].p = 0;
			else s[i].p = 1;
 		}
 		sort(s,s+2*n,cmp);
 		cnt[0] = cnt[1] = 0;
		for (int i=0; i<2*n; i++)
			x[s[i].p][cnt[s[i].p]++] = i;

		/*
		for (int i=0; i<n; i++)
			printf("%d ",x[0][i]);
		puts("");
		for (int i=0; i<n; i++)
			printf("%d ",x[1][i]);
		puts("");
		*/

		int osco = 0,pos = n-1;
		for (int i=n-1; i>=0; i--) {
			if (x[0][i] > x[1][pos]) osco++;
			else pos--;
		}
		int nsco = 0; pos = 0;
		for (int i=0; i<n; i++) {
			if (x[0][i] > x[1][pos]) { nsco++; pos++; }
		}
		printf("Case #%d: %d %d\n",t,nsco,osco);
	}
	return 0;
}
