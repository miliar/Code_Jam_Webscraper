#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define FOR(i,j,k) for(i=j;i<=k;++i)
#define REP(i,j) for(i=0;i<j;++i)
#define FORD(i,j,k) for(i=j;i>=k;i--)
#define inf 0x7fffffff

class trie
{
public:
	struct node
	{
		node *son[26];
		node()
		{
			int i;
			REP(i,26)son[i]=0;
		}
	};
	node *root;
	int tot;
	trie()
	{
		root=new node();
		tot=1;
	}
	void add(string s)
	{
		node *w=root;
		int i,tt;
		REP(i,(int)s.size())
		{
			tt=s[i]-'A';
			if(!w->son[tt])
			{
				tot++;
				w->son[tt]=new node();
			}
			w=w->son[tt];
		}
	}
	~trie()
	{
		clear(root);
	}
	void clear(node *w)
	{
		if(!w)return;
		int i;
		REP(i,26)clear(w->son[i]);
		delete w;
		w=0;
	}
};

int ans,num,n,m;
int belong[10];
string s[10];

void dfs(int ii)
{
	int i;
	if(ii>n)
	{

		trie tree[m];
		int res=0,bj,i,j;
		REP(i,m)
		{
			bj=0;
			FOR(j,1,n)if(belong[j]==i){bj=1;break;}
			if(!bj)return;
		}
		FOR(i,1,n)tree[belong[i]].add(s[i]);
		REP(i,m)res+=tree[i].tot;
		if(res>ans)
		{
			ans=res;
			num=1;
		}else if(res==ans)
		{
			num++;
		}
	}else
	{
		REP(i,m)
		{
			belong[ii]=i;
			dfs(ii+1);
		}
	}
}

void work()
{
	int i;
	scanf("%d%d",&n,&m);
	FOR(i,1,n)cin>>s[i];
	ans=0;num=0;
	dfs(1);
	printf("%d %d\n", ans,num);
}

int main()
{
	int i,T;
	scanf("%d",&T);
	FOR(i,1,T)
	{
		printf("Case #%d: ",i);
		work();
	}
}