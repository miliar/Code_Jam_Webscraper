#include<stdio.h>
int main()
{
	int t,x;
	scanf("%d",&t);
	for(x=1;x<=t;x++)
	{
		int i,j,k,flag;
		char s[105];
		FILE *fptr;
        fptr=fopen("output.txt","a");
		scanf("%s",s);
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]=='+')
			break;
		}
		if(i!=0)
		k=1;
		j=i;
		for(i=j;s[i]!='\0';i++)
		{
			if(s[i]=='-')
			{
				if(flag==0)
				{
					k=k+2;
				}
				flag=1;
			}
			else
			{
				flag=0;
			}
		}
		fprintf(fptr,"Case #%d: %ld\n",x,k);
		k=0;
	}
	return 0;
}
