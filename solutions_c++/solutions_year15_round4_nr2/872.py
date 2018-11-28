#include <cstdio>
double r[110];
double c[110];
double abs(double a){
	return a>0?a:-a;
}
double min(double a,double b){return a<b?a:b;}
double max(double a,double b){return a>b?a:b;}
int main(){
	int T;
	scanf("%d",&T);
	int count=0;
	while(count++<T){
		double V,X;
		int N;
		scanf("%d %lf %lf",&N,&V,&X);
		for(int i=0;i<N;i++)scanf("%lf %lf",&r[i],&c[i]);
		printf("Case #%d: ",count);
		if(N==1){
			if(c[0]!=X)puts("IMPOSSIBLE");
			else printf("%lf\n",V/r[0]);
		}
		else if(N==2){
			if(c[0]>X && c[1]>X)puts("IMPOSSIBLE");
			else if(c[0]<X && c[1]<X)puts("IMPOSSIBLE");
			else if(c[0]==X && c[1]==X){
				printf("%.12lf\n",V/(r[1]+r[0]));
			}
			else if(c[0]==X)printf("%.12lf\n",V/r[0]);
			else if(c[1]==X)printf("%.12lf\n",V/r[1]);
			else{
				double p0 = abs(c[0]-X);
				double p1 = abs(c[1]-X);
				double v0 = V*p1/(p0+p1);
				double v1 = V*p0/(p0+p1);
				printf("%.12lf\n",max(v0/r[0],v1/r[1]));
			}
		}
	}

}
