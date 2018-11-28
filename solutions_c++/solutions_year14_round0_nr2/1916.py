#include <stdio.h>
#include <stdlib.h>
#include <string.h>
double c,f,x;
double solve(){
	double total=0;
	double cur_speed=2;
	for(;x>c;){
		if(x/cur_speed>(x)/(cur_speed+f)+c/cur_speed)
		total+=c/cur_speed,cur_speed+=f;
		else
		total+=x/cur_speed,x=0;
	}
	total+=x/cur_speed;
	return total;
}
int main(){
	int i,t;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",i,solve());
	}
	return 0;
}
