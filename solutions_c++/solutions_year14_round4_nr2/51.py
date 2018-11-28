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

int T,a[1010],p[1010],ans,n;

bool cmp(int x,int y)
{
	return a[x]>a[y];
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		for(int i=0;i<n;i++) p[i]=i;
		sort(p,p+n,cmp);
		ans=0;
		for(int i=0;i<n;i++)
		{
			int L=0,R=0;
			for(int j=0;j<p[i];j++) if (a[j]>a[p[i]]) L++;
			for(int j=p[i]+1;j<n;j++) if (a[j]>a[p[i]]) R++;
			ans+=min(L,R);
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	
	return 0;
}
