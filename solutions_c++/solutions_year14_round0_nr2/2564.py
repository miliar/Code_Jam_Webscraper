#include<stdio.h>
FILE *in = fopen("B-large.in","r");
FILE *out= fopen("output.txt","w");

int main()
{
	int T;
	double C, F, X;
	fscanf(in, "%d", &T);
	for(int testCase = 1; testCase <= T; testCase++){
		fscanf(in, "%lf%lf%lf", &C, &F, &X);
		double ans = 0, cur = 2, testAns = 9999999999999;
		while(X/cur > C/cur + X/(cur+F)){
			ans = ans + C/cur;
			cur += F;
		}
		fprintf(out, "Case #%d: %.7lf\n", testCase,	ans+X/cur);
	}
	return 0;
}