#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

struct TNODE
{
	TNODE* ch[26];
};

TNODE TPool[2333333];
TNODE* TPTop = TPool;

struct TRIE
{
	TNODE* Root;
	int ncnt;
	bool virgin;
	TRIE(){ Root = TPTop++; memset(Root,0,sizeof(TNODE)); ncnt = 0; virgin = true; } 
	int insert(char* str)
	{
		if(virgin) virgin = false;
		TNODE* now = Root;
		while(*str)
		{
			int ch = *str - 'A';
			if(!now->ch[ch])
			{
				now->ch[ch] = TPTop++;
				memset(now->ch[ch],0,sizeof(TNODE));
				ncnt++;
			}
			now = now->ch[ch];
			str++;
		}
		return 0;
	}
};

char imstr[23][33];
int which[23];

int M = 0;
int N = 0;
int ans = -1;
int nans = 0;
int dfs(int x)
{
	if(x == M)
	{
		TPTop = TPool;
		TRIE trie[4];
		for(int i = 0;i < M;i++) trie[which[i]].insert(imstr[i]);
		int tans = 0;
		for(int i = 0;i < N;i++) tans += trie[i].ncnt + !trie[i].virgin;
		if(tans > ans)
		{
			ans = tans;
			nans = 1;
		}
		else if(tans == ans) nans++;
		return 0;
	}
	for(int i = 0;i < N;i++)
	{
		which[x] = i;
		dfs(x+1);
	}
	return 0;
}

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		scanf("%d %d",&M,&N);
		for(int i = 0;i < M;i++) scanf("%s",imstr[i]);
		ans = -1;
		nans = 0;
		dfs(0);
		printf("%d %d\n",ans,nans);
	}
	while(getchar() != EOF);
	return 0;
}