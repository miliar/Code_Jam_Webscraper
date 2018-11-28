#include<stdio.h>
#include<stdlib.h>
int main()
{
	int t,tcase=1;
	double c,f,x,rate,nrate,tm=0,t1,t2;
	FILE *fp1,*fp2;

	fp1 = fopen("Blarge.in","r");
	fp2 = fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	while(tcase<=t)
	{
		tm = 0;
		fscanf(fp1,"%lf",&c);
		fscanf(fp1,"%lf",&f);
		fscanf(fp1,"%lf",&x);
		rate = 2;
		fprintf(fp2,"Case #%d: ",tcase);

		while(1)
		{

			nrate = rate + f;
			t1 = x/rate;
			t2 = (c/rate) + (x/nrate);
			if(t1<t2)
			{
				tm = tm + t1;
				fprintf(fp2,"%.7f",tm);
				fprintf(fp2,"\n");
				break;
			}
			else
			{
				tm = tm + (c/rate);
				rate = nrate;
			}

		}
		tcase++;
	}
	fclose(fp1);
	fclose(fp2);

	return 0;
}