//shjj-rps

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int N=5000;

int A[3][N],now[3],s[3],Now,n,m;
char Ans[N];
bool P[3];

bool check(int x,int y)
{
	if (y==-1) return 1;
	for (int i=1;i<=(1<<n);i++)
	{
		if (A[x][i]<A[y][i]) return 1;
		if (A[x][i]<A[y][i]) return 0;
	}
	return 1;
}

int getfail(int x)
{
	if (!x) return 1;
	if (x==1) return 2;
	if (x==2) return 0;
	return -1;
}

bool Check(int l,int mid,int r)
{
	int ll=mid-l+1;
	for (int i=1;i<=ll;i++)
	{
		if (A[Now][l+i-1]>A[Now][mid+i]) return 1;
		if (A[Now][l+i-1]<A[Now][mid+i]) return 0;
	}
	return 0;
}

void build(int l,int r,int x,int dep)
{
	if (!dep)
	{
		A[Now][l]=x;
		return;
	}
	int y=getfail(x);
	int mid=(l+r)>>1;
	build(l,mid,x,dep-1);
	build(mid+1,r,y,dep-1);
	if (Check(l,mid,r))
		for (int i=l;i<=mid;i++)
			swap(A[Now][i],A[Now][i+(1<<(dep-1))]);
}

bool sum()
{
	for (int i=1;i<=m;i++) now[A[Now][i]]++;
	for (int i=0;i<3;i++)
		if (now[i]!=s[i]) return 0;
	return 1;
}

int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	int T,Tt=0;
	scanf("%d",&T);
	for (;T--;)
	{
		scanf("%d%d%d%d",&n,&s[1],&s[0],&s[2]);
		m=1<<n;
		for (int i=0;i<3;i++)
		{
			P[i]=0;
			now[0]=now[1]=now[2]=0;
			Now=i;
			build(1,m,i,n);
			if (sum()) P[i]=1;
		}
		int w=-1;
		for (int i=0;i<3;i++)
			if (P[i]&&check(i,w)) w=i;
		if (w==-1) printf("Case #%d: IMPOSSIBLE\n",++Tt);
			else 	{
						memset(Ans,0,sizeof(Ans));
						for (int i=1;i<=(1<<n);i++)
						{
							if (A[w][i]==0) Ans[i]='P';
							if (A[w][i]==1) Ans[i]='R';
							if (A[w][i]==2) Ans[i]='S';
						}
						
						printf("Case #%d: %s\n",++Tt,Ans+1);
					}
	}
}