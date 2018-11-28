#include<stdio.h>
#include<string.h>
long long int checkstr(char str[],int length)
{
	int i,j,k;
	if(length==1)
	{
		if(str[0]=='+')
		return 0;
		else
		return 1;
	}
	else if(str[0]=='+')
	{
		k=1;
		while(str[k]=='+'&&k<length)
		{
			k++;
		}
		if(k==length)
		{
			return 0;
		}
		else
		{
			for(j=0;j<k;j++)
			{
				str[j]='-';
				
			}
			//puts(str);
			return (1+checkstr(str,length));
		}
		
	}
	else
	{
		int k=1;
		while(str[k]=='-'&&k<length)
		{
			k++;
		}
		for(j=0;j<k;j++)
		{
			str[j]='+';
		}
		return (1+checkstr(str,length));
		
	}
}
int main()
{
	FILE *fp;
	fp=fopen("mylargeoutput.txt","w");
	FILE *fp1=fopen("mylargeinput.txt","r");
	long long int test,loop=1;
	fscanf(fp1,"%lld",&test);
	char ch;
	char str[105];
	fscanf(fp1,"%c",&ch);
	while(test>0)
	{
		fscanf(fp1,"%s",str);
		int length=strlen(str);
		long long int ans=checkstr(str,length);
		fprintf(fp,"Case #%lld: %lld\n",loop,ans);
		test--;
		loop++;
	}
	fclose(fp1);
	fclose(fp);
}
