#include<stdio.h>

void solve(int caseno)
{
	double C, F, X;
	double CS = 2;
	double T = 0;
	scanf("%lf %lf %lf", &C, &F, &X);

	while(true){
		if((X-C)/CS > X/(CS+F)){
			T+=C/CS;
			CS+=F;
		}
		else
			break;
	}
	T+= X/CS;

	printf("Case #%d: %.7lf\n",caseno, T);
}

int main()
{
	int t = 0;
	scanf("%d", &t);
	for(int i = 0; i<t; i++)
		solve(i+1);
	return 0;
}