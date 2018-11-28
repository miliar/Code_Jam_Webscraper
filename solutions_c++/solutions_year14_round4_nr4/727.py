#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;
int T,n,m,len[10],que[5][10],tail[5],ans1,ans2,trie[85][26],top;
char s[10][11];
void add(int j)
{
    int now=0,i;
    for (i=1;i<=len[j];++i)
    {
        if (!trie[now][s[j][i]-'A'])
            trie[now][s[j][i]-'A']=++top;
        now=trie[now][s[j][i]-'A'];
    }
}
void pd()
{
	int i,tmp=0;
	for (i=1;i<=m;++i)
		if (!tail[i])
			return;
	for (i=1;i<=m;++i)
	{
		memset(trie,0,sizeof(trie));
		top=0;
		for (int j=1;j<=tail[i];++j)
			add(que[i][j]);
		tmp+=top+1;
	}
	if (tmp==ans1)
		++ans2;
	if (tmp>ans1)
		ans1=tmp,ans2=1;
}
void dfs(int now)
{
	if (now>n) {pd(); return;}
	for (int i=1;i<=m;++i)
	{
		que[i][++tail[i]]=now;
		dfs(now+1);
		--tail[i];
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int i;
	scanf("%d",&T);
	for (int ii=1;ii<=T;++ii)
	{
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;++i)
			scanf("%s",s[i]+1),len[i]=strlen(s[i]+1);
		ans1=0,ans2=1;
		dfs(1);
		printf("Case #%d: %d %d\n",ii,ans1,ans2);
	}
	
	//system("pause");
	return 0;
}
