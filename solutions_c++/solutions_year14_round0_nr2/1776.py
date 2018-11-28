#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
double X,F,C;
int T;
int main(int argc, char *argv[])
{
	scanf("%d",&T);
	for(int cases=1;cases<=T;cases++)
	{
		cin>>C>>F>>X;
		int K = ceil((X*F-2*C-C*F)/(C*F));
		if (K<0)
			K=0;
		double res=0;
		res += X/(2+K*F);
		for (int i=1; i<=K; i++)
		{
			res += C/(2+(i-1)*F);
		}
		printf("Case #%d: %.7lf\n",cases,res);
	
	}
	return 0;
}
