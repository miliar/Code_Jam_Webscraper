#include<stdio.h>
#include<string.h>
int main()
{
	FILE *ftp;
	ftp=fopen("B.txt","w");
	long i,j,k,t,n,m,p;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		p=0;
		char a[110],c;
		scanf("%s",&a);
		n=strlen(a);
		for(j=n-1;j>=0;j--)
		{
			if(a[j]=='+')
			continue;
			else if(a[0]=='-')
			{
				for(k=0;k<=j/2;k++)
				{
					c=a[k];
					a[k]=a[j-k];
					a[j-k]=c;
				}
				for(k=0;k<=j;k++)
				{
					if(a[k]=='+')
					a[k]='-';
					else a[k]='+';
				}
				p++;
			}
			else
			{
				for(k=0;k<j+1;k++)
				{
					if(a[k]=='-')
					{
						break;
					}
					else
					{
						a[k]='-';
					}
				}
				p++;
				for(k=0;k<=j/2;k++)
				{
					c=a[k];
					a[k]=a[j-k];
					a[j-k]=c;
				}
				for(k=0;k<=j;k++)
				{
					if(a[k]=='+')
					a[k]='-';
					else a[k]='+';
				}
				p++;
			}
		}
		fprintf(ftp,"Case #%d: %d\n",i+1,p);
	}
	fclose(ftp);
}
