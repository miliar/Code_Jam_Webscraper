#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
int main()
{
	int t,t1=1;
	scanf("%d",&t);
	while(t1<=t)
	{
		char s[1001];
		scanf("%s",s);
		char out[2002];
		int i=1000,j=1000,k=strlen(s),l=0;
		memset(out,'\0',sizeof(out));
		while(l<k)
		{
			if(l==0)
			{
				out[i]=s[l];
			}
			else
			{
				if(s[l]>=out[i])
				{
					i--;
					out[i]=s[l];
				}
				else
				{
					j++;
					out[j]=s[l];
				}
			}
			l++;
		}
		for(i=0;i<2002;i++)
		{
			if(out[i]!='\0')
				break;
		}
		printf("Case #%d: ",t1);
		for(;i<2002;i++)
		{
			if(out[i]=='\0')
				break;
			else
			{
				printf("%c",out[i]);
			}
		}
		printf("\n");
		t1++;
	}
	return 0;
}