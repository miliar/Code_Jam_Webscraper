#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "math.h"
int main()
{
	
	FILE *input;
	FILE *output;	
	unsigned long int result,k,M,T,L,lengt,i;
	long int temp;
	char *str1;
	char *str4;
	str4=(char*)malloc(5*sizeof(char));
	str1=(char*)malloc(10000000*sizeof(char));
	
	input=fopen("F:A-small-attempt0.in","rw");
	output=fopen("F:A-small-attempt0.out","awr");
	if(input!=NULL)
	{
		fscanf(input,"%d",&T);
		fgets(str4,5,input);
		M=T;
		while(T--)
		{
			fscanf(input,"%s",str1);
			fscanf(input,"%ld",&L);
			lengt=strlen(str1);
			temp=-1;
			result=0;
			for (k=0;k<=lengt-L;k++)
			{
				
				for (i=0;i<L;i++)
				{
					if (*(str1+k+i)!='a'&&*(str1+k+i)!='e'&&*(str1+k+i)!='i'&&*(str1+k+i)!='o'&&*(str1+k+i)!='u')
						continue;
					else
						break;
				}
				if(i==L)
				{	result=result+(k-temp)*(lengt-k-L+1);
				temp=k;}
			}
			fprintf(output,"Case #%d: %ld\n",M-T,result);
		}
	}
	free(str4);
	return 0;
}