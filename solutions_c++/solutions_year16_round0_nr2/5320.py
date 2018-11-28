#include<stdio.h>
#include<string.h>
int main()
{
	int t,k=0;
	scanf("%d",&t);
	char s[100];
	while(k!=t)
	{
		int i=0,n,l=0,cnt=0;
		scanf("%s",s);
		n = strlen(s);
		while(s[i]=='-' && i!=n)
		{
			l++;
			i++;
		}
		if(l>0)
		{
			cnt = 1;
			l=0;
		}	
		while(true)
		{
			if(i==n)
			    break;
			l=0;
                	while(s[i]=='-' && i!=n)
			{
				l++;
				i++;
			}
			if(i==n)
			{
				cnt = cnt + 2;
				break;
			}
			if(l>0)
			{
				cnt=cnt+2;
				l=0;
			}
			while(s[i]=='+' && i!=n)
				i++;
			if(i==n)
			    break;
			
		}
		printf("Case #%d: %d \n",(k+1),cnt);
		k++;
        }
	return 0;
}
