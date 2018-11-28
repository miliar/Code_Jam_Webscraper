#include<cstdio>
#include<cstring>
#define N 1000
char s[N];
int test,ii,i,j,flag,ans,len;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&test);
	while (test--)
	{
		scanf("%s",&s);
		ans=0;
		ii++;
		printf("Case #%d: ",ii);
		len=strlen(s);
		while (1)
		{
			flag=0;
			for (i=0;i<len;i++)
				if (s[i]=='-') flag=1;
			if (!flag) break;
			ans++;
			if (s[0]=='-')
			{
				for (i=len-1;i>=0;i--)
				if (s[i]=='-') break;
			} 
			else
			{
				for (i=0;i<len;i++)
				if (s[i]=='-') break;i--;
			}
			
			for (j=0;j<=i-j;j++)
			{
				char t=s[j];s[j]=s[i-j];s[i-j]=t; 
			}
			for (j=0;j<=i;j++)
			if (s[j]=='-') s[j]='+';else s[j]='-';
		}
		printf("%d\n",ans);
	}
}
