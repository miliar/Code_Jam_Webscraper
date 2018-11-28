#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

#define MAXN 1005

int n,k;

int sum[MAXN];
int f[MAXN];

inline void solve()
{
	scanf("%d%d",&n,&k);
	int i,j;
	for (i=1;i+k-1<=n;i++) {
		scanf("%d",sum+i);
	}
	int S=sum[1];
	int max_f=0;
	for (i=1;i<=k;i++) {
		int l=0,r=0,now=0;
		for (j=i+k;j<=n;j+=k) {
			now+=sum[j-k+1]-sum[j-k];
			l=std::min(l,now);
			r=std::max(r,now);
		}
		S+=l;
		f[i]=r-l;
		max_f=std::max(max_f,f[i]);
	}
	S%=k;
	S=(S+k)%k;
	int tmp=0;
	for (i=1;i<=k;i++) {
		tmp+=max_f-f[i];
	}
	if (tmp>=S) {
		printf("%d\n",max_f);
	} else {
		printf("%d\n",max_f+1);
	}
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