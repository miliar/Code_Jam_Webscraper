#include <cstdio>

double C,F,X;
void input(){
	scanf("%lf %lf %lf",&C,&F,&X);
}

double tnow,tnew,ratenow,buy;
void solve(){
	ratenow = 2.0,buy = 0.0;
	tnow = X/ratenow;
	while(true){
		tnew = buy + C/ratenow + X/(ratenow+F);
		if(tnew < tnow){
			tnow = tnew;
			buy += C/ratenow;
			ratenow += F;
		}else break;
	}
	printf("%.7lf\n",tnow);
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		printf("Case #%d: ",i);
		input();
		solve();
	}
	return 0;
}