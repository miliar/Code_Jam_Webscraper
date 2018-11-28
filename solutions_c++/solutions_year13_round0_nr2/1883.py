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

int n,m,xma[110],yma[110],a[110][110],b[110][110],T;

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&m);
		memset(xma,0,sizeof xma);
		memset(yma,0,sizeof yma);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++) b[i][j]=100;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				xma[i]=max(a[i][j],xma[i]);
				yma[j]=max(a[i][j],yma[j]);
			}
		int flag=1;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				b[i][j]=min(xma[i],yma[j]);
				if (b[i][j]!=a[i][j]) flag=0;
			}
		printf("Case #%d: ",tt);
		if (flag) puts("YES"); else puts("NO");
	}
	return 0;
}
