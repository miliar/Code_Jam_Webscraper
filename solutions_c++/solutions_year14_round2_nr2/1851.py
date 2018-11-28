#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int case_num,A,B,K,win_count;
	FILE* in = fopen("data.in","r");
	FILE* out = fopen("data.out","w");

	fscanf(in,"%d",&case_num);
	for(unsigned int i=0; i<case_num;i++)
	{
		fscanf(in,"%u %u %u\n",&A,&B,&K);
		win_count=0;

		for(unsigned int a=0;a<A;a++)
		{
			for(unsigned int b=0;b<B;b++)
			{
				if( (a&b) < K) win_count++;
			}
		}


		fprintf(out,"Case #%u: %u\n",i+1,win_count);
	}

	fclose(in);
	fclose(out);
	return 0;
}

