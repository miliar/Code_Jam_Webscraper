#include <stdio.h>
#include <string.h>
char a[200],b[200];
int n;

int isVol(char ch)
{
	if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
		return 1;
	else
		return 0;
}

int main(int argc, char const *argv[])
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.txt","w",stdout);
	int t,cass=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",a);
		scanf("%d",&n);
		int len = strlen(a);
		int num=0;
		if(!isVol(a[len-1]))
			a[len-1]=1;
		else
			a[len-1]=0;
		for(int i=len-2;i>=0;i--)
			if(!isVol(a[i]))
				a[i]=a[i+1]+1;
			else
				a[i]=0;


		//for(int i=0;i<len;i++)
			//printf("%d ",a[i]);
		//printf("\n");
		for(int i=0;i<len;i++)
		{
			if(a[i]>=n)
				num+=len-i-n+1;
			else
			{
				int j;
				for(j=i+1;j<len;j++)
				{
					if(a[j]>=n)
						break;
				}
				if(a[j]>=n)
				{
					num+=len-j-n+1;
				}
			}
		}
		printf("Case #%d: %d\n",cass++,num);
	}
	return 0;
}
