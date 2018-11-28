#include<stdio.h>

char s[1005];

int main(void)
{
	
freopen("C:\\Users\\user\\Desktop\\input.in","r",stdin);
freopen("C:\\Users\\user\\Desktop\\out1.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n,ans=0,tot=0;
        scanf("%d",&n);
		scanf("%s",&s);
		for(int k=0;k<=n;k++)
		{
			s[k]=s[k]-'0';
	        if(k>tot)
			{
				ans=ans+k-tot;
				tot=k+s[k];
			}
			else
			tot=tot+s[k];
		}
		printf("Case #%d: %d\n",i,ans);
	}
    return 0;
}