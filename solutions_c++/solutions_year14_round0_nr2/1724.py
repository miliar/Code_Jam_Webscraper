#include <cstdio>
#include <cmath>
int t,k;
double c,f,x,v,t0,ans,dx;
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	for (int T = 1;T <= t;T++){
		scanf("%lf%lf%lf",&c,&f,&x);
		v = 2;
		ans = x / v;
		k = (f * (x - c) - 2 * c) / c / f;
		t0 = 0;
		for (int i = 1;i <= k;i++){
			t0 += c / v;
			v += f;
			if (t0 + x / v < ans) ans = t0 + x / v;
		}
		while (t0 + c / v + x / (f + v) < ans){
			t0 += c / v;
			v += f;
			if (t0 + x / v < ans) ans = t0 + x / v;
		}
		printf("Case #%d: %.7f\n",T,ans);
	}
}
