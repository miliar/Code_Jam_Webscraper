#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int t,tcase;
	int A,B,x,y;
	int i,j,re;
	char num[22],rev[22];
	
	FILE *in,*out;
	in=fopen("C-small-attempt0.in","r");
	out=fopen("output.out","w");

	fscanf(in,"%d",&tcase);
	for(t=0;t<tcase;t++)
	{
		fprintf(out,"Case #%d: ",t+1);
		fscanf(in,"%d",&A);
		fscanf(in,"%d",&B);

		i=1;
		re=0;
		while(1)
		{
			if(i*i<A)
			{
				i++;
				continue;
			}
			if(i*i>B)
				break;
			sprintf(num,"%d",i);
			strcpy(rev,num);
			strrev(num);
			if(strcmp(num,rev)==0)
			{
				sprintf(num,"%d",i*i);
				strcpy(rev,num);
				strrev(num);
				if(strcmp(num,rev)==0)
					re++;
			}
			i++;
		}
		fprintf(out,"%d\n",re);
	}

	return 0;
}