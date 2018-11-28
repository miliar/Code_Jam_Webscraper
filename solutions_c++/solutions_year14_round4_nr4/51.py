/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int ans,cnt,T,n,m;
char s[1010][110];
int c[50000][26];
int ind,now,use[1010];
int exi[110];

void calc()
{
	memset(exi,0,sizeof exi);
	for(int i=0;i<n;i++) exi[use[i]]=1;
	for(int i=0;i<m;i++) if (!exi[i]) return;
	memset(c,0,(ind+10)*4*26);
	ind=m;
	for(int i=0;i<n;i++)
	{
		now=use[i]+1;
		int l=strlen(s[i]);
		for(int j=0;j<l;j++)
		{
			if (!c[now][s[i][j]-'A']) c[now][s[i][j]-'A']=++ind;
			now=c[now][s[i][j]-'A'];
		}
	}
	if (ind>ans) ans=ind,cnt=1; else if (ind==ans) cnt++;
}

void dfs(int x)
{
	if (x>=n)
	{
		calc();
		return;
	}
	for(int i=0;i<m;i++)
	{
		use[x]=i;
		dfs(x+1);
	}
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&m);
		ans=-1; cnt=0;
		for(int i=0;i<n;i++) scanf("%s",s[i]);
		dfs(0);
		printf("Case #%d: %d %d\n",tt,ans,cnt);
	}
	
	return 0;
}
