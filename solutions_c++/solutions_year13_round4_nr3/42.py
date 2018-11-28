#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#define LL long long

using namespace std;

int g[2000][2000];
int tt;
int n;
int a[2000],b[2000];
int d[2000];
int ans[2000];

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d",&n);
		for (int i=0;i<n;++i)
			scanf("%d",&a[i]);
		for (int i=0;i<n;++i)
			scanf("%d",&b[i]);

		memset(g,0,sizeof(g));
		memset(d,0,sizeof(d));

		for (int i=0;i<n;++i) {
			int pre=-1;
			for (int j=0;j<i;++j) {
				if (a[j]>=a[i]) {
					g[i][j]++;
					d[j]++;
				}
				if (a[j]+1==a[i]) pre=j;
			}
			if (pre!=-1) {
				g[pre][i]++;
				d[i]++;
			}
		}
		for (int i=0;i<n;++i) {
			int pre=-1;
			for (int j=n-1;j>i;--j) {
				if (b[j]>=b[i]) {
					g[i][j]++;
					d[j]++;
				}
				if (b[j]+1==b[i]) pre=j;
			}
			if (pre!=-1) {
				g[pre][i]++;
				d[i]++;
			}
		}

		for (int i=0;i<n;++i) {
			int idx=-1;
			for (int j=0;j<n;++j)
				if (d[j]==0) {
					idx=j;
					break;
				}
			d[idx]--;
			ans[idx]=i;
			for (int j=0;j<n;++j)
				d[j]-=g[idx][j];
		}

		printf("Case #%d:",ii);
		for (int i=0;i<n;++i)
			printf(" %d",ans[i]+1);
		printf("\n");
	}
}
