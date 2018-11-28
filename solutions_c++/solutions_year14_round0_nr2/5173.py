#include <cstdio>

using namespace std;

int main()
{
	FILE *fp;
	fp=fopen("C:/Users/prabhusa/Desktop/ans.txt", "w");
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++) {
		double cost,fprod,X,curp=2.0000000,tim=0.0000000,tcx=0.0000000,tx=0.0000000,pttb=0.0000000;
		scanf("%lf%lf%lf",&cost,&fprod,&X);
		do{
			tcx=pttb+cost/curp+X/(curp+fprod);
			tx=pttb+X/curp;
			if(tx<=tcx)
				tim=tx;
			else {
				pttb+=cost/curp;
				curp+=fprod;
			}
		}while(tx>tcx);
		fprintf(fp,"Case #%d: %.7f\n",test,tim);
	}
	return 0;
}