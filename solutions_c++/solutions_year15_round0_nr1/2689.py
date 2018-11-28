#include<cstdio>
#include<string.h>
using namespace std;

int main()
{
	int s_max,a,b,c,num,ans,k,i,j,test;
	char S[1005];
	scanf("%d",&test);
	for(j=1;j<=test;j++)
	{
		scanf("%d %s",&s_max,S);
		ans=0;
		num=0;
		for(i=0;i<=s_max;i++)
		{
			if(i > num && (S[i] - '0')>0)
			{
				ans += (i - num);
				num += (i - num);
			}
			num += S[i] - '0';
		}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}
