#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
	int t;
	double c,f,x,buy,regen,time_end,time_end_upgrade,hasil;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		hasil = 0;
		regen = 2;
		scanf("%lf%lf%lf",&c,&f,&x);
		while(1){
			buy = c/regen;
			time_end = hasil + x/regen;
			time_end_upgrade = hasil + buy + (x/(regen+f));	
		//	printf("%lf %lf\n",time_end,time_end_upgrade);
			//system("pause");
			if(time_end - time_end_upgrade < 1e-8) {
				hasil = time_end;
				break;
			}
			else{
				hasil += buy;
				regen+=f;
			}
		}
		printf("Case #%d: ",tt);
		printf("%.7lf\n",hasil);
	}
}