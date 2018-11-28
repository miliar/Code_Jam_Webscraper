#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<map>
#include<set>
#include<string>
#include<vector>
using namespace std;
typedef long long lld;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
struct Trie
{
    int next[26];
    int fail;
}node[100010];
int pos;
void add()
{
    memset(node[pos].next,-1,sizeof(node[pos].next));
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
        int id=str[i]-'A';
        if(node[at].next[id] == -1)
        {
            node[at].next[id]=pos;
            add();
        }
        at=node[at].next[id];
    }
}
char str[110][110];
int n,need;
int ans,way;
int belong[110];
int val[110];
void solve()
{
	for(int i=0;i<need;i++)
		val[i]=0;
	for(int i=0;i<n;i++)
		val[belong[i]]+=1<<i;
	for(int i=0;i<need;i++)
		if(val[i] == 0)
			return;
	int tmp=0;
	for(int t=0;t<need;t++)
	{
		int sss=val[t];
		init();
		for(int i=0;i<n;i++)
			if(sss&(1<<i))
				insert(str[i]);
		tmp+=pos;
	}
	if(tmp > ans)
	{
		ans=tmp;
		way=1;
	}
	else if(tmp == ans)
		way++;
}
void dfs(int dep)
{
	if(dep == n)
	{
		solve();
		return;
	}
	for(int i=0;i<need;i++)
	{
		belong[dep]=i;
		dfs(dep+1);
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%d %d",&n,&need);
		for(int i=0;i<n;i++)
			scanf("%s",str[i]);
		ans=-1;
		way=0;
		dfs(0);
		printf("Case #%d: %d %d\n",cc,ans,way);
	}
	return 0;
}
/*
2
4 2
AAA
AAB
AB
B
5 2
A
B
C
D
E

 */
