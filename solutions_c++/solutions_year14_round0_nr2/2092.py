#include <stdio.h>
#include <string.h>
int T , Cnt = 1;
double C , F , X , ans;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("outputB.out","w",stdout);
	double tmp , rate;
	scanf("%d",&T);
	while ( T-- ){
		scanf("%lf%lf%lf",&C,&F,&X);
		ans = X / 2;
		tmp = C / 2; rate = 2 + F;
		while ( true ){
			double tans = tmp + X / rate;
			if ( tans > ans )
				break;
			ans = tans;
			tmp += C / rate;
			rate += F;
			
		}
		printf("Case #%d: %.7lf\n",Cnt++,ans);
	
	}
	
	
	return 0;	
}
