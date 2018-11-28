#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int n;
double a[1100];
double b[1100];

int main() {
	int t,tt,i,j,ans;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++) {
		scanf("%d",&n);
		for (i=0;i<n;i++) scanf("%lf",&a[i]);
		for (i=0;i<n;i++) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		printf("Case #%d: ",tt);
		ans=0;
		i=0;j=0;
		while (i<n) {
			if (a[i]>b[j]) {
				ans++;
				j++;
			}
			i++;
		}
		printf("%d ",ans);
		ans=0;
		i=0;j=0;
		while (j<n) {
			if (a[i]>b[j]) {
				ans++;
				j++;
			} else {
				i++;
				j++;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
