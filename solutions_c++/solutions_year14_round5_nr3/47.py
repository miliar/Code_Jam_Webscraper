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

int T,n,a[20],b[20],type[20],now[1<<15],nxt[1<<15];
char s[20];

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		int len=0;
		for(int i=0;i<n;i++)
		{
			scanf("%s%d",s,&a[i]);
			type[i]=(s[0]=='E');
			if (a[i]!=0) b[len++]=a[i];
		}
		sort(b,b+len);
		len=unique(b,b+len)-b;
		for(int i=0;i<n;i++)
			if (a[i]!=0) a[i]=lower_bound(b,b+len,a[i])-b+1;
		int o=1<<n;
		for(int i=0;i<o;i++) now[i]=1;
		for(int i=0;i<n;i++)
		{
			memset(nxt,0,sizeof nxt);
			for(int j=0;j<o;j++) if (now[j])
			{
				if (type[i]==0)
				{
					if (a[i]==0)
					{
						for(int k=0;k<n;k++) if ((j>>k)&1)
							nxt[j^(1<<k)]=1;
					} else if ((j>>a[i])&1)
						nxt[j^(1<<a[i])]=1;
				} else
				{
					if (a[i]==0)
					{
						for(int k=0;k<n;k++) if (!((j>>k)&1))
							nxt[j^(1<<k)]=1;
					} else if (!((j>>a[i])&1))
						nxt[j^(1<<a[i])]=1;
				}
			}
			memcpy(now,nxt,sizeof now);
		}
		int ans=n+1;
		for(int i=0;i<o;i++) if (now[i]) ans=min(ans,__builtin_popcount(i));
		
		printf("Case #%d: ",tt);
		if (ans>n) puts("CRIME TIME"); else printf("%d\n",ans);
	}
	
	return 0;
}
