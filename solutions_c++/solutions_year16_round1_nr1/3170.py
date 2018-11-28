#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	int t,test,i,k,j;
	char s[1001],c[1001];
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%s",s);
		k=0;
		for(i=0;i<strlen(s);i++)
		{
			char ch=s[i];
			if(k==0)
			{
				c[k++]=ch;
			}
			else
			{
				if(ch>=c[0])
				{
					for(j=k;j>0;j--)
					{
						c[j]=c[j-1];
					}
					c[0]=ch;
					k++;
				}
				else
				{
					c[k++]=ch;
				}
			}
		}
		printf("Case #%d: ",t);
		for(j=0;j<k;j++)
		{
			printf("%c",c[j]);
		}
		printf("\n");
	}
	return 0;
}
