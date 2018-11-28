#include <cstdio>
#include <algorithm>
int n,t,ans1,ans2,p,q;
double a[1010],b[1010];
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for (int T = 1;T <= t;T++){
		scanf("%d",&n);
		for (int i = 1;i <= n;i++) scanf("%lf",&a[i]);
		for (int i = 1;i <= n;i++) scanf("%lf",&b[i]);
		std::sort(a + 1,a + n + 1);
		std::sort(b + 1,b + n + 1);
		ans1 = 0;
		ans2 = n;
		p = 1;
		for (q = 1;q <= n;q++){
			while (p <= n && a[p] < b[q]) p++;
			if (p > n) break;
			ans1++;
			p++;
		}
		p = 1;
		for (q = 1;q <= n;q++){
			while (p <= n && a[q] > b[p]) p++;
			if (p > n) break;
			ans2--;
			p++;
		}
		printf("Case #%d: %d %d\n",T,ans1,ans2);
	}
}
