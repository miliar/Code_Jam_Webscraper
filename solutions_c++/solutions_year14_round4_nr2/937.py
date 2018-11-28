#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

const int maxn=1005;
const int inf=1000000000;

struct node {
	int data, num;
} a[maxn];

int f[maxn][maxn],g[maxn],h[maxn];

bool cmp(const node &a, const node &b) {
	return a.data<b.data;
}

int main() {
	int cases;
	scanf("%d",&cases);
	for (int o=0; o<cases; ++o) {
		printf("Case #%d: ",o+1);
		int n;
		scanf("%d",&n);
		for (int i=0; i<n; ++i) {
			scanf("%d",&a[i].data);
			a[i].num=i;
		}
		sort(a,a+n,cmp);
		memset(g,0,sizeof(g));
		memset(h,0,sizeof(h));
		for (int i=0; i<n; ++i) {
			for (int j=i+1; j<n; ++j) {
				if (a[i].num<a[j].num) {
					++g[i];
				} else {
					++h[i];
				}
			}
		}
		f[0][0]=0;
		for (int i=1; i<=n; ++i) {
			for (int j=0; j<=i; ++j) {
				f[i][j]=inf;
				if (j>0) {
					f[i][j]=min(f[i][j],f[i-1][j-1]+h[i-1]);
				}
				if (j<i) {
					f[i][j]=min(f[i][j],f[i-1][j]+g[i-1]);
				}
			}
		}
		int ans=inf;
		for (int i=0; i<=n; ++i) {
			ans=min(ans,f[n][i]);
		}
		printf("%d\n",ans);
	}
	return 0;
}