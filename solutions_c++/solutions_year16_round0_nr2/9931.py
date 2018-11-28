#include<stdio.h>
#include<string.h>

int main(void)
{
	int T;
	char S[106];
	FILE *fi,*fo;

	fi = fopen("intput.txt","r");
	fo = fopen("output.txt","w");

	fscanf(fi,"%d",&T);
	int testcase;
	int result;
	int lenS;
	int i,j;
	for(testcase=1;testcase<=T;testcase++)
	{
		fscanf(fi,"%s",S);
		lenS = strlen(S);
		result = 0;
		for(i=lenS-1;i>=0;i--)
		{
			if(S[i]=='+');
			else
			{
				result++;
				for(j=i;j>=0;j--)
				{
					if(S[j]=='+') S[j]='-';
					else S[j]='+';
				}
			}
		}
		fprintf(fo,"Case #%d: %d\n",testcase,result);
	}
}