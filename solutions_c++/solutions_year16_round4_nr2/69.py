#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int tt;
int n,k;
double ans;
double a[210],b[210];
double f[210];

void solve(int l,int r) {
	for (int i=0;i<l;++i)
		b[i]=a[i];
	for (int i=0;i<r;++i)
		b[i+l]=a[n-r+i];

	memset(f,0,sizeof(f));
	f[0]=1;
	for (int i=0;i<k;++i)
		for (int j=n-1;j>=0;--j) {
			f[j]=(1-b[i])*f[j];
			if (j>0) f[j]+=b[i]*f[j-1];
		}
	ans=max(ans,f[k/2]);
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d",&tt);
	for (int ii=1;ii<=tt;++ii) {
		scanf("%d%d",&n,&k);
		for (int i=0;i<n;++i)
			scanf("%lf",&a[i]);
		sort(a,a+n);

		ans=0;
		for (int i=0;i<=k;++i)
			solve(i,k-i);

		printf("Case #%d: %.8lf\n",ii,ans);
	}
}