#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAXN 1000

bool rotate(char arr[]);
int main()
{
	int t,T;
	char num[20];
	FILE * ip=fopen("C-small-attempt0.in","r");
	FILE * op=fopen("C-small-attempt0.out","w");

	fscanf(ip,"%d",&T);
	for(t=0;t<T;t++)
	{
		int A,B,count=0,i,original;
		fscanf(ip,"%d%d",&A,&B);
		i=(int)sqrt((float)A);
		if(i*i!=A)
			i++;
		for(;i*i<=B;i++)
		{
			itoa(i,num,10);
			if(rotate(num))
			{
				
				itoa(i*i,num,10);
				if(rotate(num))
				{
					count++;
				}
			}
		}
		fprintf(op,"Case #%d: %d\n",t+1,count);
	}
	return 0;
}

bool rotate(char arr[])
{
	int len=strlen(arr);
	int i;
	for(i=0;i<len/2;i++)
	{
		if(arr[i]!=arr[len-i-1])  // 5;;,, 0 4 1 3 2 2 4 0 3 1 2 
			return false;
	}
	return true;
}