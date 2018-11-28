#include<stdio.h>
#include<string.h>
int main()
{
	int t,n;
	scanf("%d",&t);
	char a[101],b[101];
	for(int x=1;x<=t;x++)
	{
		scanf("%d",&n);
		scanf("%s",&a);
		scanf("%s",&b);
	
		//printf("%s %s\n",c,d);
		int i=0,j=0,opn=0;
		for(;i<strlen(a)&&j<strlen(b);)
		{
			
			if(a[i]==b[j])
			{
				i++;
				j++;
			}
			else if(j>0&&a[i]==b[j-1])
			{
				i++;
				opn++;
			}
			else if(i>0&&a[i-1]==b[j])
			{
				j++;
				opn++;
			}
			else if((j==0&&i==0)&&a[i]!=b[j])
			{
				opn=-1;
				break;
			}
			else if(!(a[i-1]==b[j])||(a[i]==b[j-1]))
			{
				opn=-1;
				break;
			}
		}
		while(j<strlen(b)&&opn!=-1)
					{
						if(b[j]==a[strlen(a)-1])
						{
							opn++;
							j++;
						}
						else
						{
							opn=-1;
							//printf("voila");
							break;
						}
					}
					while(i<strlen(a)&&opn!=-1)
					{
						if(a[i]==b[strlen(b)-1])
						{
							opn++;
							i++;
						}
						else
						{
							opn=-1;
							//printf("voila");
							break;
						}
					}
					
					
		if(opn==-1)
		{
				printf("Case #%d: Fegla Won\n",x);
		}
		else
		{
				printf("Case #%d: %d\n",x,opn);
		}
	}
}