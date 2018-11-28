#include <stdio.h>

int n;
char str[1020];

int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int Ti=1;Ti<=T;++Ti)
	{
		scanf("%d%s",&n,str);
		int ans=0,sum=0;
		for(int i=0; i<=n; ++i)		
			if(str[i]-'0'!=0)
			{
				if(sum<i)
				{
					ans+=i-sum;
					sum=i;
				}
				sum+=str[i]-'0';
			}
		printf("Case #%d: %d\n",Ti,ans);
	}
	return 0;
}