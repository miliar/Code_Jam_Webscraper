#include <stdio.h>
int main()
{
	FILE *in =fopen ("input.txt","r");
	FILE *out =fopen ("output.txt","w");
	int T;
	double C,F,X;
	double ans;
	double ans2;
	double temp;
	double k,ANS;
	fscanf(in,"%d",&T);
	for(int t=1;t<=T;t++){
		fscanf(in,"%lf%lf%lf",&C,&F,&X);
		k = 2.0;
		ans = X/k;
		ANS = ans;
		temp = (C/k);

		for(int c=0;;c++){
			ans2 = temp + (X/(k+F));
			k+=F;
			temp += (C/k);
			if(ans2 > ANS){
				break;
			}
			ANS = ans2;
		}
		fprintf(out,"Case #%d: %.7lf\n",t,ANS);
	}
	return 0;
}
