#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T,R;
	char S[1000];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		R=0;
		int f=1;
		bool flag=true;
		scanf("%s",S);
		int len=strlen(S);
		for(int j=0;j<len;j++)
		{
			if(flag&&S[j]=='-')
			{
				R+=f;
				flag=false;
			}
			if(S[j]=='+')
			{
				f=2;
				flag=true;
			}
		}
		printf("Case #%d: %d\n",i+1,R);
	}
	return 0;
}