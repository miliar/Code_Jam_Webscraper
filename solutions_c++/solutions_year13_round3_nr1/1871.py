#include <stdio.h>
#include <string.h>
char s[1000009];

int main()
{
	int t,n,ans,jwb,min,max;
	scanf("%d",&t);
	for(int ctr=1;ctr<=t;ctr++)
	{
		scanf("%s%d",&s,&n);
		jwb=0;
		int len = strlen(s);
		for(int i=len;i>=n;i--)
		{
			for(int j=0;j<=len-i;j++)
			{
				ans = 0;
				min = max = -1;
				for(int k=j,h=0;h<i;k++,h++)
				{
					//printf("%c",s[k]);
					if(s[k]=='a' || s[k]=='i' || s[k]=='u' || s[k]=='e' || s[k]=='o') ans=0;
					else
					{
						ans++;
						if(ans>=n)
						{
							jwb++;
							break;
						}
						//printf("%d %d %d\n",i,j,k);
					}
				}
				//printf("\n");
				
			}
		}
		printf("Case #%d: %d\n",ctr,jwb);
	}

return 0;
}

