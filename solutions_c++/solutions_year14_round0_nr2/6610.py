#include<stdio.h>
#include<stdlib.h>
double C, F, X;
double fun(double s, double t){
	double s1=X/s;
	double s2=C/s;
	if(s1<=s2+X/(s+F)) return t+s1;
	else {
	    return fun(s+F, t+s2);
	}
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T, i,j,k,cnt=0;
	scanf("%d",&T);
	while(cnt<T){
		scanf("%lf%lf%lf",&C,&F,&X);
		//printf("C=%lf, F=%lf, X=%lf\n", C,F,X);
		printf("Case #%d: ",cnt+1);	
		printf("%.7f\n",fun(2.0,0));
		cnt++;
	}
	return 0;
}
