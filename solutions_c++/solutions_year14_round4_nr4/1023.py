#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

struct trie
{
	int x[26];
} t[105];
int S,N,M,ans,bg,s[105],b[105];
char a[1005][105];

void init()
{
	scanf("%d%d",&M,&N);
	for (int i=1; i<=M; i++) scanf("%s",a[i]);
}

void ins(char*s)
{
	for (int i=0,p=1,c; c=s[i]-65,s[i]; i++,p=t[p].x[c]) if (!t[p].x[c]) t[p].x[c]=++S;
}

int calc()
{
	int ss=0;
//	for (int i=1; i<=M; i++) cout<<b[i]<<' ';cout<<endl;
	for (int i=1; i<=N; i++) if (!s[i]) return -1e9;
	for (int i=1; i<=N; i++)
	{
		S=1,memset(t,0,sizeof(t));
		for (int j=1; j<=M; j++) if (b[j]==i) ins(a[j]);
	//	cout<<i<<' '<<S<<endl;
		ss+=S;
	}
//	cout<<ss<<endl;
	return ss;
}

void dfs(int t)
{
	if (t>M)
	{
		int w=calc();
		if (w>ans) ans=w,bg=1; else if (w==ans) bg++;
		return;
	}
	for (int i=1; i<=N; i++) b[t]=i,s[i]++,dfs(t+1),s[i]--;
}

void doit()
{
	ans=0,dfs(1);
	cout<<ans<<' '<<bg<<endl;
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1; i<=T; i++)
	{
		init();
		printf("Case #%d: ",i);
		doit();
	}
	return 0;
}
/*
1
4 2
AAA
AAB
AB
B


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
