#include <stdio.h>
int abs(int x)
{
	if(x>0)
		return x;
	return -x;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int flag=1,ans=0,N,p[100]={0};
		char str[100][101];
		
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			scanf("%s",str[i]);
		while(flag&&str[0][p[0]]!='\0')
		{
			int cnt[100],sum=0,target;
			char ch=str[0][p[0]];
			for(int i=0;i<N;i++)
			{
				if(str[i][p[i]]!=ch)
				{
					flag=0;
					break;
				}

				int j;
				for(j=p[i]+1;;j++)
					if(str[i][j]!=ch)
						break;
				cnt[i]=j-p[i]-1;
				sum+=cnt[i];
				p[i]=j;
			}
			target=sum/N;
			if(sum-target*N>(target+1)*N-sum)
				target++;
			for(int i=0;i<N;i++)
				ans+=abs(cnt[i]-target);
		}
		for(int i=0;i<N;i++)
			if(str[i][p[i]]!='\0')
			{
				flag=0;
				break;
			}
		if(flag)
			printf("Case #%d: %d\n",t,ans);
		else
			printf("Case #%d: Fegla Won\n",t);
	}
	return 0;
}
