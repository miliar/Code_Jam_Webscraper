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

int N,c[55];
llint P;

bool calc1(llint x)
{
	llint g=x;
	for(int i=0;i<N;i++)
	{
		if (g)
		{
			if (!c[i])
				return 0;
			else
				g--;
		}
		g/=2;
	}
	return 1;
}

bool calc2(llint x)
{
	llint g=(1ll<<N)-x-1;
	for(int i=0;i<N;i++)
	{
		if (!c[i])
		{
			if (!g)
				return 0;
			else
				g--;
		} else
			if (g)
				return 1;
		g/=2;
	}
	return 1;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cin>>N>>P; P--;
		memset(c,0,sizeof c);
		int len=0;
		while(P)
		{
			c[len++]=P%2;
			P/=2;
		}
		reverse(c,c+N);
		llint L=0,R=(1ll<<N)-1,t,ans;
		printf("Case #%d: ",tt);
		for(;L<=R;)
		{
			t=(L+R)>>1;
			if (calc1(t)) L=t+1,ans=t; else R=t-1;
		}
		printf("%I64d ",ans);
		for(L=0,R=(1ll<<N)-1;L<=R;)
		{
			t=(L+R)>>1;
			if (calc2(t)) L=t+1,ans=t; else R=t-1;
		}
		printf("%I64d\n",ans);
	}
	
	return 0;
}
