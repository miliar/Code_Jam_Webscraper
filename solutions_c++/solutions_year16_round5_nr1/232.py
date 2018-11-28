#include<cstdio>
#include<cstring>
char S[20050],s[20050];
int L;
int main()
{
	int i,T,_T,top,ans;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (_T=1;_T<=T;_T++)
	{
		scanf("%s",S+1);
		L=strlen(S+1); top=0; ans=0;
		for (i=1;i<=L;i++)
		{
			if ((top==0)||(S[i]!=s[top]))
			{
				top++; s[top]=S[i];
			}
			else
			{
				top--; ans+=10;
			}
		}
		for (i=1;i<=top/2;i++) ans+=5;
		printf("Case #%d: %d\n",_T,ans);
	}
	return 0;
}
