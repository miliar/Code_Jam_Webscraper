#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<cstdlib>
#include<functional>
#include<utility>
#include<ctime>
#include<sstream>
#define pb push_back
#define mp make_pair
#define fr(i,n) for(int i=0;i<n;++i)
#define fn(i,n) for(int i=n-1;i>=0;--i)
#define fe(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();++i)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;
const int N = 110;
int test,ans,n,m,a[N],cnt;
char s[N][N];
int trie[N*10][26];

int calc()
{
	int tmp=0;
	for (int i=0;i<n;i++)
		tmp|=1<<a[i];
	if (tmp!=(1<<m)-1) return 0;
	int ret=0;
	for (int i=0;i<m;i++)
	{
		int tot=1;
		memset(trie[1],0,sizeof trie[1]);
		for (int j=0;j<n;j++)
			if (a[j]==i)
			{
				for (int k=0,now=1;s[j][k];k++)
				{
					if (!trie[now][s[j][k]-'A'])
					{
						trie[now][s[j][k]-'A']=++tot;
						memset(trie[tot],0,sizeof trie[tot]);
					}
					now=trie[now][s[j][k]-'A'];
				}
			}
		ret+=tot;
	}
	return ret;
}

void paint(int now)
{
	if (now==n) 
	{
		int tmp=calc();
		if (tmp==ans) cnt++;
		if (tmp>ans) cnt=1,ans=tmp;
		return;
	}
	for (int i=0;i<m;i++)
	{
		a[now]=i;
		paint(now+1);
	}
}

int main()
{
	scanf("%d",&test);
	for (int t=1;t<=test;t++)
	{
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) scanf("%s",s[i]);
		ans=0,cnt=0;
		paint(0);
		printf("Case #%d: %d %d\n",t,ans,cnt);
	}
	return 0;
}
