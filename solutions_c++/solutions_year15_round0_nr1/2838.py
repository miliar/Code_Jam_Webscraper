#include<cstdio>

using namespace std;

int S,s[1100],pre[1100];
void work()
{
	scanf("%d",&S);
	getchar();
	for(int i=0;i<=S;i++)
	{
		char c; scanf("%c",&c);
		s[i]=c-48;
		pre[i]=s[i]; if(i>0) pre[i]+=pre[i-1];
	}
	int ans=0;
	for(int i=1;i<=S;i++)
		if(pre[i-1]+ans<i) ans=i-pre[i-1];
	printf("%d\n",ans);
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T; scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		work();
	}
}
