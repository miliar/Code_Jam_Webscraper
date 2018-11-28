#include<stdio.h>
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T, n, i, l;
	long double A, B, P, C, F, X;
	scanf("%d", &T);
	for(l=1; l<=T; l++)
	{
		scanf("%Lf%Lf%Lf", &C, &F, &X);
		A=B=P=0;
		P = X/2;
		for(i=1; ; i++)
		{
			A = X/(2+i*F);
			B += C/(2+(i-1)*F);
			if(A+B >= P)break;
			P = A+B;
		}
		printf("Case #%d: %.10lf\n", l, P);
	}
	return 0;
}