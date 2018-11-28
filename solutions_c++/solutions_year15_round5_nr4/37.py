#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

#define MAXN 10005

int N;
int n;
int val[MAXN];
int freq[MAXN];

inline void solve()
{
	scanf("%d",&N);
	int i,j;
	for (i=1;i<=N;i++) {
		scanf("%d",val+i);
	}
	int cnt=0;
	for (i=1;i<=N;i++) {
		scanf("%d",freq+i);
		cnt+=freq[i];
	}
	for (i=1;i<=20;i++) {
		if ((1<<i)==cnt) {
			break;
		}
	}
	n=i;
	--freq[1];
	for (i=1;i<=n;i++) {
		for (j=1;j<=N;j++) {
			if (freq[j]) {
				break;
			}
		}
		printf("%d",val[j]);
		if (i<n) putchar(' ');
		--freq[j];
		int x=val[j];
		if (x==0) {
			for (j=1;j<=N;j++) {
				freq[j]>>=1;
			}
		} else {
			int k=1;
			for (j=1;j<N;j++) {
				while (k<=N && val[k]-val[j]<x) ++k;
				freq[k]-=freq[j];
			}
		}
	}
	puts("");
}

int main()
{
	int T;
	scanf("%d",&T);
	int i;
	for (i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
	}
}