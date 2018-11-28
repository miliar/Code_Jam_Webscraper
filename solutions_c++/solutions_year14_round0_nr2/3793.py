#include<stdio.h>

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int T;
	scanf("%d",&T);

	for(int t=1;t<=T;t++){
		double C,F,X,r,nr,tp,t1,t2;
		scanf("%lf%lf%lf",&C,&F,&X);

		r=2;
		t1 = X/r;
		nr = r + F;
		t2 = C/r + X/nr;
		tp=0;
		while(t1 > t2){
			tp += C/r;
			r=nr;
			t1=X/r;
			nr = r + F;
			t2 = C/r + X/nr;
		}
		tp += t1;

		printf("Case #%d: %.7lf\n",t,tp);
	}
}
