#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define MAXMO 100000
#define MAXN 50
#define MAXL 111

struct node
{
	int ch;
	node *link[26];
	void clear()
	{
		memset(link,0,sizeof link);
	}
}Mo[MAXMO],*Mo_head,*root;

int T,N,M;

char A[MAXN][MAXL];

int add(char *s)
{
	node *p = root;
	int ret = 0;
	for (int i=0;s[i];i++)
	{
		int ch = s[i] - 'A';
		if (!p->link[ch])
		{
			ret ++;
			p->link[ch] = Mo_head ++;
			p->link[ch]->clear();
		}
		p = p->link[ch];
	}
	return ret;
}

int S[MAXN],Ans,Count;

void dfs(int i)
{
	if ( i == N )
	{
		int ans = M;
		for (int j=0;j<M;j++)
		{
			root->clear();
			Mo_head = Mo;
			bool have = 0;
			for (int k=0;k<N;k++)
			{
				if (S[k] == j)
				{
					have = 1;
					ans += add(A[k]);
				}
			}
			if (!have)
			{
				return ;
			}
		}
		if (ans > Ans)
		{
			Ans = ans;
			Count = 1;
		}
		else if (ans == Ans)
		{
			Count ++;
		}
		return ;
	}
	
	for (int j=0;j<M;j++)
	{
		S[i] = j;
		dfs(i+1);
	}
}

int main()
{
	root = new node();
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int i;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&N,&M);
		for (i=0;i<N;i++)
		{
			scanf("%s",A[i]);
		}
		Ans = 0;
		dfs(0);
		printf("Case #%d: %d %d\n",cases,Ans,Count);
	}
	return 0;
}
