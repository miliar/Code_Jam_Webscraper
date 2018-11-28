#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define pi acos(-1.0)
#define eps 1e-8
struct Trie
{
    int next[26];
    bool isend;
}node[10000010];
int pos;
void add()
{
    memset(node[pos].next,-1,sizeof(node[pos].next));
    node[pos].isend=false;
    pos++;
}
void init()
{
    pos=0;
    add();
}
void insert(char str[])
{
    int len=strlen(str);
    int at=0;
    for(int i=0;i<len;i++)
    {
        int id=str[i]-'a';
        if(node[at].next[id] == -1)
        {
            node[at].next[id]=pos;
            add();
        }
        at=node[at].next[id];
    }
    node[at].isend=true;
}
char str[10010];
int dp[2][1200010][5];
int len;
int main()
{
	freopen("garbled_email_dictionary.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	init();
	while(scanf("%s",str) != EOF)
		insert(str);
//	printf("%d\n",pos);
	freopen("input.txt","r",stdin);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%s",str);
		len=strlen(str);
		int now=0;
		int pre=1;
		for(int i=0;i<pos;i++)
			for(int j=0;j<=4;j++)
				dp[now][i][j]=inf;
		dp[now][0][0]=0;
		for(int k=0;k<len;k++)
		{
			int x=str[k]-'a';
			now^=1;
			pre^=1;
			for(int i=0;i<pos;i++)
				for(int j=0;j<=4;j++)
					dp[now][i][j]=inf;
			for(int i=0;i<pos;i++)
				for(int j=0;j<=4;j++)
				{
					if(dp[pre][i][j] == inf)
						continue;
					if(j == 0)
					{
						for(int t=0;t<26;t++)
						{
							int next=node[i].next[t];
							if(next != -1)
							{
								dp[now][next][4]=min(dp[now][next][4],dp[pre][i][j]+1);
								if(node[next].isend)
									dp[now][0][4]=min(dp[now][0][4],dp[now][next][4]);
							}
						}
						int next=node[i].next[x];
						if(next != -1)
						{
							dp[now][next][0]=min(dp[now][next][0],dp[pre][i][j]);
							if(node[next].isend)
								dp[now][0][0]=min(dp[now][0][0],dp[now][next][0]);
						}
					}
					else
					{
						int next=node[i].next[x];
						if(next != -1)
						{
							dp[now][next][j-1]=min(dp[now][next][j-1],dp[pre][i][j]);
							if(node[next].isend)
								dp[now][0][j-1]=min(dp[now][0][j-1],dp[now][next][j-1]);
						}
					}
				}
		}
		int ans=inf;
		for(int i=0;i<=4;i++)
			ans=min(ans,dp[now][0][i]);
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
