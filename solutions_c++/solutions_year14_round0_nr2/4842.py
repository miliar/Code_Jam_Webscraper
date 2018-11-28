#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define inf 1000000000.0
#define eps 0.00000001

int main(){
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 int tes;
 
 scanf("%d",&tes);
 for(int tcase=1;tcase<=tes;tcase++){
    double cost,inc,X;
	 double cps = 2.0;
	 double time = inf;
	 
	 scanf("%lf%lf%lf",&cost,&inc,&X);
	 
	 double cnt = 0.0;
	 double ptime = 0.0, ttime;
	 while(true){
		 double tmp;
		 if(cnt == 0) tmp = X / cps;
		 else{
			 ptime += cost / cps; 		// time to buy cnt farms
		    cps += inc;					// cps increased
			 tmp = ptime + X / cps;		// time to collect X 		
		 }
		 
		 if(tmp <= time && time - tmp > eps) time = tmp, cnt++;
		 else{
		    printf("Case #%d: %.7lf\n",tcase,time);
			 break;		
		 }
//		 printf("%.7lf\n",time);
	 }		
 }
 
 fclose(stdin);
 fclose(stdout);
// system("pause");
 return 0;	
}
