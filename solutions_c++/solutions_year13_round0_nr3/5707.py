#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int palindrome_str(char a[],int n)
{
	int i;
	for(i=0;i<n/2;++i)
	{
		if(a[i]!=a[n-i-1])
		{
			return 0;
		}
	}
	return 1;
}
int palindrome_int(int num)
{
	char a[10];
	int count=0;
	while(num>0)
	{
		int t=num%10;
		num=num/10;
		a[count++]=t+'0';
	}
	return palindrome_str(a,count);
}
int issquare(int num)
{
	int t=(int)pow((double)num,0.5);
	if(t*t==num)
	{
		if(palindrome_int(t))
		{
			return 1;
		}
	}
	return 0;
}
int main(void)
{
	FILE *fr=fopen("C-small-attempt0.in","r");
	FILE *fw=fopen("2.txt","w");
	int test,count=0;
	fscanf(fr,"%d",&test);
	while(test--)
	{
		count++;
		int a,b,result=0;
		fscanf(fr,"%d %d",&a,&b);
		int i;
		for(i=a;i<=b;++i)
		{
			if(palindrome_int(i)&&issquare(i))
			{
				result++;
			}
		}
		fprintf(fw,"Case #%d: %d\n",count,result);

	}
	fclose(fr);
	fclose(fw);
	return 0;
}