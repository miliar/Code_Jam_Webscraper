#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
const double eps=1e-9;
double dcmp(double x){ 
    if(fabs(x)<eps) return 0;
	if(x>0) return 1;
	return -1;
}
int main(){ 
	//freopen("B--large.in","r",stdin);
	//freopen("B--large.out","w",stdout);
    int T;
	double C,F,X;
	scanf("%d",&T);
	for(int kase=0;kase<T;kase++){ 
	     scanf("%lf%lf%lf",&C,&F,&X);
		 double now=2,time=0;
		 while(1){
	         double t1=C/now+X/(now+F);
		     double t2=X/now;
		     if(dcmp(t1-t2)<0){          
		         time+=C/now;
			     now+=F;
		     }else{ 
		         time+=t2;
				 break;
		     }
		 }
		 printf("Case #%d: %.7f\n",kase+1,time);
	}
	return 0;
}
