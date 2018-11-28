#include "stdio.h"
#include "iostream"


int main()
{
	FILE * finp;
	FILE * foutp;

	int t;
	int an;
	int x, r, c;
	int temp;
	if((finp=fopen("1.in","r"))==NULL)
	{
		printf("error");
		exit(0);
	}
	if((foutp=fopen("1.out","w"))==NULL)
	{
		printf("error");
		exit(0);
	}

	fscanf(finp,"%d",&t);

	for(int i=0;i<t;i++)
	{
		fscanf(finp, "%d%d%d", &x,&r,&c);
		temp = r*c;
		if (x == 1)
		{
			an = 0;
		}
		if (x == 2)
		{
			if (temp == 3 || temp == 1 || temp == 9)an = 1;
			else an = 0;
		}
		if (x == 3)
		{
			if (temp == 6 || temp==9||temp == 12)an = 0;
			else an = 1;
		}
		if (x == 4)
		{
			if (temp == 12 || temp == 16)an = 0;
			else an = 1;
		}
		if (an==0)
			fprintf(foutp,"Case #%d: GABRIEL\n",i+1);
		else
			fprintf(foutp, "Case #%d: RICHARD\n", i + 1);
	}

	fclose(finp);
	fclose(foutp);

	return 0;
}
