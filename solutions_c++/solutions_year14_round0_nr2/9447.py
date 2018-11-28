#include<cstdio>
int main(){
	int T,z,i,j;
	double C,F,X,min,tmp;
	scanf("%d",&T);
	for(z=1;z<=T;z++){
		scanf("%lf%lf%lf",&C,&F,&X);
		min=X/2;
		for(i=0;;i++){
			tmp=0;
			for(j=0;j<i;j++){
				tmp+=C/(2+j*F);
			}
			tmp+=X/(2+i*F);
			if(min>=tmp) min=tmp;
			else break;
		}
		printf("Case #%d: %7lf\n",z,min);
	}
	return 0;
}
