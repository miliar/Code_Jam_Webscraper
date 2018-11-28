#include <cstdio>
#include <cstdlib>
#include <cstdlib>

int t,tes;
double ans,kiri,bawah,c,f,x,EPS;

int main() {
	EPS = 1e-9;

	scanf("%d",&t);
	for (tes=1; tes<=t ; tes++) {
		scanf("%lf%lf%lf",&c,&f,&x);
		
		ans = x/2;
		kiri = c/2;
		bawah = 2+f;
		
		while (kiri + x/bawah < ans && ans - (kiri + x/bawah) > EPS) {
			ans = kiri + x/bawah;
			kiri += c/bawah;
			bawah += f;
		}
		
		printf("Case #%d: %.7lf\n",tes,ans);
	}
}