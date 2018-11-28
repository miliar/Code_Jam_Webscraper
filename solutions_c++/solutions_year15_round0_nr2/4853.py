#include <cstdio>
#include <cmath>
int a[1001], mini, ans;
int main () {
	int n;
	scanf("%d", &n);
	for (int m=1; m<=n; m++) {
		for (int i=0; i<=1000; i++) {
			a[i]=0;
		}
		int d;
		scanf("%d", &d);
		for (int i=0; i<d; i++) {
			scanf("%d", &a[i]);
		}
		mini=999999999;
		for (int k=1; k<=1000; k++) {
			ans=0;
			for (int i=0; i<d; i++) {
				if (a[i]>k) ans+=int(ceil(1.0*(a[i]-k)/k));
			}
			ans+=k;
			if (ans<mini&&ans!=0) mini=ans;
		}
		printf("Case #%d: %d\n", m, mini);
	}
	return 0;
}
