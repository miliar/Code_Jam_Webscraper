#include<stdio.h>

int main()
{
	freopen("in.txt","r",stdin);
	freopen("b_out_big.txt","w",stdout);

	int cas,cc;
	scanf("%d",&cas);
	double C,F,X;
	double TM;
	double SP;
	double temp1;
	double temp2;

	for(cc=1;cc<=cas;cc++)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		TM=0;
		SP=2.0;

		while(1){

			temp1=(X-C)/SP;
			temp2=X/(SP+F);

			if(temp1>temp2)
			{
				TM = TM + (C/SP);
				SP=SP+F;
			}
			else
			{
				break;
			}

		}

		TM=TM+(X/SP);

		printf("Case #%d: %lf\n",cc,TM);
	}
	return 0;
}