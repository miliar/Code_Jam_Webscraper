#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

struct con {
	double r,c;
} a[105];

int n;
double vol,x;
double mv[105];

bool cmp(con aa,con bb) {
	return aa.c < bb.c;
}

int main() {
	int tc;
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%lf%lf",&n,&vol,&x);
		for (int i=0; i<n; i++)
			scanf("%lf%lf",&a[i].r,&a[i].c);

		sort(a,a+n,cmp);

		if (a[0].c > x+1e-8 || a[n-1].c < x-1e-8) {
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}

		double mi=0,mx=1e15,mid;
		while (mi+1e-10 < mx && mi*(1+1e-10)< mx) {
			mid = (mi+mx)/2;
			for (int i=0; i<n; i++)
				mv[i] = mid*a[i].r;
			double totv = 0,minheat = 0,maxheat = 0;
			for (int i=0; i<n; i++) {
				if (vol-totv > mv[i]) {
					minheat += mv[i]*a[i].c;
					totv += mv[i];
				}
				else {
					minheat += (vol-totv)*a[i].c;
					totv += vol-totv;
					//printf("%f * %f\n",vol-totv,a[i].c);
					break;
				}
			}
			totv = 0;
			for (int i=n-1; i>=0; i--) {
				if (vol-totv > mv[i]) {
					maxheat += mv[i]*a[i].c;
					totv += mv[i];
				}
				else {
					maxheat += (vol-totv)*a[i].c;
					totv += vol-totv;
					break;
				}
			}
			//printf("%f: %.10f = %.10f [%.12f < %.12f < %.12f]\n",mid,totv,vol,minheat,x*vol,maxheat);
			if (totv+1e-10 < vol) {
				mi = mid;
			}
			else {
				if ((minheat*(1-1e-15) < x*vol && maxheat*(1+1e-15) > x*vol) || (minheat-1e-15 < x*vol && maxheat+1e-15 > x*vol)) {
					mx = mid;
				}
				else mi = mid;
			}
		}
		printf("Case #%d: %.8f\n",t,mid);
		fflush(stdout);
	}
    return 0;
}
