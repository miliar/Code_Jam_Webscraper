#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#define LL long long

using namespace std;

int n;
int tt;
LL bud;
LL a[40];
LL b[40];

double getans(LL bet) {
	double res=0;
	int pp=0;
	sort(b,b+37);
	for (int i=0;i<37;++i)
		if (b[i]<=bet) pp++;
	for (int i=0;i<37;++i)
		if (b[i]<=bet) res+=(double)(b[i]-a[i])*(double)36/(double)pp;
	for (int i=0;i<37;++i)
		res-=b[i]-a[i];
	return res;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	cin >> tt;
	for (int ii=1;ii<=tt;++ii) {
		memset(a,0,sizeof(a));
		cin >> bud >> n;
		for (int i=0;i<n;++i) cin >> a[i];
		sort(a,a+37);

		double ans=0;
		b[37]=(LL)10000000*(LL)10000000;
		for (int i=1;i<=37;++i)
			for (int j=1;j<=i;++j) {
				for (int k=0;k<37;++k) b[k]=a[k];
				LL res=0;
				LL cap=b[i-1];
				for (int k=0;k<i;++k)
					res+=cap-b[k],b[k]=cap;
				for (int k=0;k<i-j;++k)
					b[k]++,res++;
				if (i<=j+2 && i>=33) {
					i++,i--;
				}
				if (res<=bud) {
					LL pp1=bud-res;
					pp1/=i;
					pp1=min(pp1,max(0LL,b[i]-b[i-1]-1));
					for (int k=0;k<i;++k)
						b[k]+=pp1;
					ans=max(getans(b[i-1]),ans);
				}
			}
		printf("Case #%d: %.12lf\n",ii,ans);
	}
}
