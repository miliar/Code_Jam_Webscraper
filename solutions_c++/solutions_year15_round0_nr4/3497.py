#include <stdio.h>

int main()
{
	FILE * in = fopen("D-small-attempt3.in","r");
	FILE * out = fopen("output.out","w");

	int T;
	int X,R,C;

	fscanf(in,"%d",&T);

	for(int i=0;i<T;i++)
	{
		fscanf(in,"%d %d %d",&X,&R,&C);

		switch(X)
		{
		case 1:
			fprintf(out,"Case #%d: GABRIEL\n",i+1);
			break;

		case 2:
			if(R%2 == 0 || C%2 == 0)
			{
				fprintf(out,"Case #%d: GABRIEL\n",i+1);
				break;
			}
			else
			{
				fprintf(out,"Case #%d: RICHARD\n",i+1);
				break;
			}

		case 3:
			if(R%3 == 0 || C%3 == 0)
			{
				if(R == 1 || C == 1)
				{
					fprintf(out,"Case #%d: RICHARD\n",i+1);
					break;
				}
				else
				{
					fprintf(out,"Case #%d: GABRIEL\n",i+1);
					break;
				}
			}
			{
				fprintf(out,"Case #%d: RICHARD\n",i+1);
				break;
			}

		case 4:
			if(R%4 == 0 || C%4 == 0)
			{
				if(R == 1 || C == 1)
				{
					fprintf(out,"Case #%d: RICHARD\n",i+1);
					break;
				}
				else if(R == 2 || C == 2)
				{
					fprintf(out,"Case #%d: RICHARD\n",i+1);
					break;
				}
				else
				{
					fprintf(out,"Case #%d: GABRIEL\n",i+1);
					break;
				}
			}
			else
			{
				fprintf(out,"Case #%d: RICHARD\n",i+1);
				break;
			}	
		}
	}

	fclose(in);
	fclose(out);

	return 0;
}