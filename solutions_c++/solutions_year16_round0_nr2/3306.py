#include <stdio.h>
#define maxn 202

using namespace std;

int digit[102];
FILE *fp, *fp2;

int main()
{
	fp = fopen("B-large.in", "r");
	fp2 = fopen("Boutput2.txt", "w");
	int test_case;
	fscanf(fp, "%d", &test_case);
	fgetc(fp); 
	for(int i=1;i<=test_case; i++)
	{
		int c, pc='A';
		for(int j=0;j<102;j++)
			digit[j]=0;
		fprintf(fp2, "Case #%d: ", i);
		int numr=1;
		while(c=fgetc(fp))
		{
			if(c=='\n')
				break;
			if(c!=pc)
			{
				digit[numr]=digit[numr-1]+1;
				numr++;
				pc=c;
			}
		}
		
		if(pc=='+')
			fprintf(fp2, "%d\n", digit[numr-1]-1);
		else
			fprintf(fp2, "%d\n", digit[numr-1]);
	}
	
	fclose(fp);
	fclose(fp2);
	return 0;
}
