#include<stdio.h>
int main(){
	int t,l=1;
	FILE *f1;
	f1=fopen("out1.txt","w");
	scanf("%d",&t);
	while(t--){
		double total=0,c,f,x,r=2.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(((c/r)+x/(f+r))<(x/r)){
			total=total+c/r;
			r=r+f;
		}
		total=total+x/r;
		fprintf(f1,"Case #%d: %.7lf\n",l,total);
		l++;
	}
}
