#include <stdio.h>
int main() {
	int casenum=0;
	FILE *fp = fopen("in","r");
	fscanf(fp, "%d",&casenum);
	for (int casei=1;casei<=casenum;casei++) {
		double c=1,f=1,x=1;
		fscanf(fp,"%lf %lf %lf",&c,&f,&x);
		double t0=0,speed=2.0;
		for (int i=0;i<100000;i++) {
			double t1=t0+x/speed;
			double t2=t0+c/speed+x/(speed+f);
			if (t2>t1) {
				t0=t1;
				break;
			}
			else {
				t0+=c/speed;
				speed+=f;
			}
		}
		fprintf(stdout,"Case #%d: %.7lf\n", casei, t0);
	}
	return 0;
}
