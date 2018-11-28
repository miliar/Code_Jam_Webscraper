#include"stdafx.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int n,m,ans,tot,fre;
char s[10][20];
char p[10][10][20];
char pn[10];
struct node
{
    int p[26];
    char c;
}trie[100];
void insert(int i,int i1)
{
    int np=0;
    char s[20];
    strcpy(s,p[i][i1]);
    int ls=strlen(s);
    int now=0;
    for (i=0;i<ls;i++)
    {
        int idx=(int)(s[i]-'A');
        if (trie[now].p[idx]==0)
        {
            tot++;
            trie[now].p[idx]=tot;
            now=tot;
            trie[now].c=s[i];
        }
        else now=trie[now].p[idx];
    }
}
int cal(int i)
{
    tot=0;
    memset(trie,0,sizeof(trie));
    for (int i1=0;i1<pn[i];i1++)
    {
        insert(i,i1);
    }
	//printf("%d\n",tot+1);
    return tot+1;
}
void dfs(int i)
{
    if (i==m)
    {
		for (int i1=0;i1<n;i1++)
			if (pn[i1]==0)
				return ;
        int res=0;
        for (int i1=0;i1<n;i1++)
		{
			int ww=cal(i1);
			if (ww==1)
				return ;
            res+=ww;;
		}
		if (res>ans)
		{
			ans=res;
			fre=1;
		}
		else if (res==ans)
		{
			fre++;
		}
        return ;
    }
    for (int i1=0;i1<n;i1++)
    {
        strcpy(p[i1][pn[i1]],s[i]);
        pn[i1]++;
        dfs(i+1);
        pn[i1]--;
    }
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int tk,tk1=0,i;
    scanf("%d",&tk);
    while (tk--)
    {
        tk1++;
        scanf("%d %d",&m,&n);
        for (i=0;i<m;i++)
        {
            scanf("%s",s[i]);
        }
        ans=0;
		fre=0;
        dfs(0);
        printf("Case #%d: %d %d\n",tk1,ans,fre);
    }
    return 0;
}

