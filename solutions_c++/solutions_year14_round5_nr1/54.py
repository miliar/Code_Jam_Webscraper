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

int n,a[1000010],T,p,q,r,s;

bool calc(llint x)
{
	llint now=0,tot=1;
	for(int i=0;i<n;i++) 
	{
		if (now+a[i]<=x) now+=a[i];
		else
		{
			now=a[i],tot++;
			if (tot>3) return 0;
		}
	}
	return 1;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d%d%d",&n,&p,&q,&r,&s);
		for(int i=0;i<n;i++) a[i]=(1ll*i*p+q)%r+s;
		llint L=*max_element(a,a+n),R,t,ans,sum=0;
		for(int i=0;i<n;i++) sum+=a[i];
		R=sum;
		for(;L<=R;)
		{
			t=(L+R)>>1;
			if (calc(t)) R=t-1,ans=t; else L=t+1;
		}
		printf("Case #%d: %.12lf\n",tt,1-1.0*ans/sum);
	}
	
	return 0;
}
