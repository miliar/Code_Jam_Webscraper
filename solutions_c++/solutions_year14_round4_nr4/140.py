
#include <bits/stdc++.h>
using namespace std;

int T;

struct node
{
	int c[26];
};

char s[16][16];
int n,m,a1,a2;
int stk[16];
int cnt[5];

struct trie
{
	node tr[128];
	int gs;
	int cnt[26];
	void init() {
		memset(tr,0,sizeof(tr));
		gs=0;
	}
	trie()
	{
		init();
	}
	void insert(char s[])
	{
		int len=strlen(s);
		int now=0;
		for (int i=0;i<len;i++)
		{
			if (tr[now].c[s[i]-65]==0)
			{
				gs++;
				cnt[s[i]-97]++;
				tr[now].c[s[i]-65]=gs;
			}
			now=tr[now].c[s[i]-65];
		}
	}
}Tr[5];

void dfs(int dep) {
	if (dep>m) {
		for (int i=1;i<=n;i++) {
			if (cnt[i]==0) return;
			Tr[i].init();
		}
		for (int i=1;i<=m;i++)
			Tr[stk[i]].insert(s[i]);
		int ans=0;
		for (int i=1;i<=n;i++) ans+=Tr[i].gs+1;
		if (ans>a1) {
			a1=ans;
			a2=1;
		}
		else if (ans==a1) a2++;
		return;
	}
	for (int i=1;i<=n;i++) {
		cnt[i]++;
		stk[dep]=i;
		dfs(dep+1);
		cnt[i]--;
	}
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%d %d\n",&m,&n);
		for (int i=1;i<=m;i++) scanf("%s",s[i]);
		a1=-1;
		a2=0;
		dfs(1);
		printf("%d %d\n",a1,a2);
	}
	return 0;
}
