#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int n,ans;
int vis[15],a[15];
int ch[30];
char str[15][1010];
char s[10010];
void dfs(int k)
{
	int i,len,j;
	if (k == n)
	{
		len = 0;ans++;
		memset(s,EOF,sizeof(s));
		memset(ch,0,sizeof(ch));
		//for (i = 0;i < n;i++) printf("%d",a[i]);
		for (i = 0;i < n;i++)
		{
			for (j = 0;j < strlen(str[a[i] - 1]);j++) s[len++] = str[a[i] - 1][j];
		}
		//for (i = 0;i < len;i++) printf("%c",s[i]);
		//printf("\n");
		//printf("%c",s[0]);
		ch[s[0] - 'a'] = 1;
		//printf("%d\n",ch[s[0] - 'a']);
		for (i = 1;i < len;i++)
		{
			if (s[i] != s[i - 1])
			{
				if (ch[s[i] - 'a'] == 1)
				{
					ans--;
					break;
				}
				else ch[s[i] - 'a'] = 1;
			}
		}
		//printf("%d\n",ans);
	}
	else
	{
		for (i = 1;i <= n;i++)
		{
			if (vis[i] == 0)
			{
				vis[i] = 1;
				a[k] = i;
				dfs(k + 1);
				vis[i] = 0;
			}
		}
	}
	return;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,T;
	int i,j;
	int te;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		ans = 0;
		scanf("%d",&n);
		memset(vis,0,sizeof(vis));
		memset(str,EOF,sizeof(str));
		memset(ch,0,sizeof(ch));
		for (i = 0;i < n;i++)
		{
			scanf("%s",str[i]);
			te = 0;
			for (j = 1;j < strlen(str[i]);j++)
			{
				if (str[i][j] == str[i][j - 1]) te++;
				else str[i][j - te] = str[i][j];
			}
			str[i][j - te] = '\0';
			//printf("%s\n",str[i]);
		}
		dfs(0);
		printf("Case #%d: %d\n",t,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
