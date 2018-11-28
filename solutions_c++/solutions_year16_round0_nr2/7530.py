#include <stdio.h>
#include <string.h>

char pan[1005];

main()
{
	FILE *f=fopen("i.in","r");
	FILE *p=fopen("o.txt","w");
	int test;
	int num_p,sum;
	fscanf(f,"%d",&test);
	for(int i=0;i<test;i++)
	{
		sum=0;
		fscanf(f,"%s",pan);
		for(int m=0;m<strlen(pan)-1;m++)
		{
			if(pan[m]!=pan[m+1])	//printf("-%d-",m);
				sum++;
		}
		if(pan[strlen(pan)-1]=='+')
			fprintf(p,"Case #%d: %d\n",i+1,sum);
		else
			fprintf(p,"Case #%d: %d\n",i+1,sum+1);
	}
}
