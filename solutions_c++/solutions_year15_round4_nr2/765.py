#include<stdio.h>
double V[2];
double C[2];

double min(double a,double b){return a<b?a:b;}
double max(double a,double b){return a>b?a:b;}
double abs(double x){return x>=0?x:-x;}

int main(){
	int dn;
	scanf("%d",&dn);
	for(int di=0;di<dn;di++){
		int n,i;
		double S,T;
		scanf("%d %lf %lf",&n,&S,&T);
		for(i=0;i<n;i++)scanf("%lf %lf",&V[i],&C[i]);
		printf("Case #%d: ",di+1);
		if(n==1){
			if(T!=C[0])puts("IMPOSSIBLE");
			else printf("%.12lf\n",S/V[0]);
		}
		if(n==2){
			if(T<min(C[0],C[1])||T>max(C[0],C[1]))puts("IMPOSSIBLE");
			else{
				double D=abs(C[0]-C[1]);
				if(D==0){
					printf("%.12lf\n",S/(V[0]+V[1]));
					continue;
				}
				double A=abs(C[0]-T);
				double B=abs(C[1]-T);
				printf("%.12lf\n",max((S*B/D)/V[0],(S*A/D)/V[1]));
			}
		}
	}
	return 0;
}