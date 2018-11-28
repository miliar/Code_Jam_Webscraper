#include <cstdio>
#include <utility>
#include <algorithm>

using namespace std;

int n;
double v,x;
pair<double,double> a[100];
double sumr;
double lsumrc,rsumrc,lsumr,rsumr;

int main() {
	int t,tt,i;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d%lf%lf",&n,&v,&x);
		sumr=0;
		lsumrc=rsumrc=0;
		lsumr=rsumr=0;
		for (i=0;i<n;i++) {
			scanf("%lf%lf",&a[i].first,&a[i].second);
			if (a[i].second==x) sumr+=a[i].first;
			else if (a[i].second<x) {
				lsumr+=a[i].first;
				lsumrc+=a[i].first*(x-a[i].second);
			} else if (a[i].second>x) {
				rsumr+=a[i].first;
				rsumrc+=a[i].first*(a[i].second-x);
			}
		}
		sort(a,a+n);
		if (sumr==0&&(lsumr==0||rsumr==0)) printf("Case #%d: IMPOSSIBLE\n",tt);
		else {
			if (lsumrc<rsumrc) {
				sumr+=lsumr;
				for (i=0;i<n;i++) if (a[i].second>x) {
					if (a[i].first*(a[i].second-x)<lsumrc) {
						sumr+=a[i].first;
						lsumrc-=a[i].first*(a[i].second-x);
					} else {
						sumr+=lsumrc/(a[i].second-x);
						lsumrc=0;
					}
				}
			} else {
				sumr+=rsumr;
				for (i=n-1;i>=0;i--) if (a[i].second<x) {
					if (a[i].first*(x-a[i].second)<rsumrc) {
						sumr+=a[i].first;
						rsumrc-=a[i].first*(x-a[i].second);
					} else {
						sumr+=rsumrc/(x-a[i].second);
						rsumrc=0;
					}
				}
			}
			//printf("%lf\n",sumr);
			printf("Case #%d: %.9lf\n",tt,v/sumr);
		}
	}
	return 0;
}
