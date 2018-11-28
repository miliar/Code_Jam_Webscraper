#include <stdio.h>
#include <algorithm>

using namespace std;

int t,n;
double V,X;
double R[120],C[120];

//double rec(int a,double V,double X){
	//double lo=0,hi=V+1e-20;
	//for(int w=0;w<100;++w){
		//double v1=(lo*2+hi)/3.;
		//double v2=(lo+hi*2)/3.;
		//if (rec(a+1,V-v1,(X*V-v1*C[a])/(V-v1))<-0.1){
		//}
	//}
	//return 0;
//}

int main(){
	scanf("%d",&t);
	for(int tt=1;tt<=t;++tt){
		printf("Case #%d: ",tt);
		scanf("%d%lf%lf",&n,&V,&X);
		for(int i=0;i<n;++i){
			scanf("%lf%lf",R+i,C+i);
		}
		if (n==1){
			if (abs(C[0]-X)>1e-11) puts("IMPOSSIBLE");
			else printf("%.9lf\n",V/R[0]);
			continue;
		} else if (n==2){
			if (abs(C[0]-X)<1e-11||abs(C[1]-X)<1e-11){
				if (abs(C[0]-X)<1e-11&&abs(C[1]-X)<1e-11){
					printf("%.9lf\n",V/(R[0]+R[1]));
				} else if (abs(C[0]-X)<1e-11){
					printf("%.9lf\n",V/R[0]);
				} else if (abs(C[1]-X)<1e-11){
					printf("%.9lf\n",V/R[1]);
				}
				continue;
			}
			if (abs(C[0]-C[1])<1e-11){
				puts("IMPOSSIBLE");
				continue;
			}
			double v1=V*(X-C[0])/(C[1]-C[0]);
			double v0=V-v1;
			double t0=v0/R[0];
			double t1=v1/R[1];
			if (t0<0||t1<0) puts("IMPOSSIBLE");
			else printf("%.9lf\n",max(t0,t1));
			continue;
		} else puts("neviem");
		//double V_less=0,V_more=0;
		//for(int i=0;i<n;++i){
			//if (C[i]<X) V_less+=C[i];
			//if (C[i]>X) V_more+=C[i];
		//}
		//double lo=0,hi=1e20;
		//for(int w=0;w<100;++w){
			//double t1=(lo*2+hi)/3.;
			//double t2=(lo+hi*2)/3.;
		//}
	}
	return 0;
}
