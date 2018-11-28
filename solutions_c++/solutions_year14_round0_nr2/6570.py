#include <stdio.h>
#include <stdlib.h>

int main(int atgc, char *argv[]){
	int T = 0;
	double C,F,X;
	C=F=X=0.0;
	int T_cnt = 0;
	
	double base, P;
	P = base = 2.0;
	int F_cnt = 0;

	double epsilon = 2.5;
	double sum = 0.0;//total time cost
	double ans = 0.0;

	FILE *f = fopen("output.txt", "w");
	if (f == NULL)
	{
    	printf("Error opening file!\n");
    	exit(1);
	}

	scanf("%d", &T);
	while(T--){
		sum = 0.0;
		F_cnt = 0;
		scanf("%lf %lf %lf",&C,&F,&X);
		P = base + F * F_cnt;
		while( ( C/P + X/(P+F)) < (X/P) ){
			//fprintf(f,"   \nP=%f, sec=%.7f\n", P,C/P);
			sum += C/P;
			F_cnt++;
			P = base + F * F_cnt;
		}	
		//fprintf(f,"         \nsum=%f, C/P=%.7f, X/P=%.7f\n", sum, C/P,X/P);
		ans=sum+X/P;

		T_cnt++;
		fprintf(f, "Case #%d: ", T_cnt);
		fprintf(f,"%.7f\n", ans);
	}

	fclose(f);
	return 0;
}
