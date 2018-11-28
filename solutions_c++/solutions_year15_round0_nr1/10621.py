#include <stdio.h>
#include <stdlib.h>
int main()
{
	int T=0;
	int* p;
	char** chr;
	int sumOva = 0;
	int brFr = 0;
	int si = 0;
	FILE *in= fopen("A-small-attempt4.in","r");
	FILE *out= fopen("A-small-attempt4.out","w");

	fscanf(in,"%d",&T);

	p=(int*)malloc(sizeof(int)*T);
	chr=(char**)malloc(sizeof(char*)*T);
	

	for (int i = 0; i < T; i++)
	{
		fscanf(in,"%d",&p[i]);
		chr[i] = (char*)malloc(sizeof(char)*p[i]+2);
		for (int j = 0; j < p[i]+2; j++)
		{
			fscanf(in,"%c",&chr[i][j]);
		}
	}

	for (int i = 0; i < T; i++)
	{
		si = -1;
		for (int j = 1; j < p[i]+2; j++)
		{
			si++;
			if (j == 1)
			{
				sumOva =  chr[i][j]-48;
			}else
			{
				if (chr[i][j]-48 != 0)
				{
					if (sumOva >= si)
					{
						sumOva += (chr[i][j]-48);
					}else
					{
						brFr += si - sumOva;
						sumOva += brFr;
						sumOva += (chr[i][j]-48);
					}
				}
			}
		}
		
		fprintf(out,"Case #%d: %d\n",i+1,brFr);
		brFr = 0;
		sumOva = 0;
	}
	fclose(in);
	fclose(out);
	return 0;
}