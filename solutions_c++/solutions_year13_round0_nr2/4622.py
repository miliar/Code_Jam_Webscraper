#include<iostream>
using namespace std;
#define MAX_NM 200

int a[MAX_NM][MAX_NM],m[MAX_NM][MAX_NM];
bool solve()
{
	int N,M,mm,i,j;
	scanf("%d%d",&N,&M);
	for(i=0;i<N;i++)
		for(j=0;j<M;j++)
		{
			scanf("%d",&a[i][j]);
			m[i][j]=100;
		}
	for(i=0;i<N;i++)
	{
		mm=-1;
		for(j=0;j<M;j++) mm=max(mm,a[i][j]);
		for(j=0;j<M;j++) m[i][j]=min(mm,m[i][j]);
	}
	for(j=0;j<M;j++)
	{
		mm=-1;
		for(i=0;i<N;i++) mm=max(mm,a[i][j]);
		for(i=0;i<N;i++) m[i][j]=min(mm,m[i][j]);
	}
	for(i=0;i<N;i++)
	{
		for(j=0;j<M;j++)
			if(m[i][j]!=a[i][j]) return false;
	}
	return true;
}


int main()
{
	int T,i;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++) printf("Case #%d: %s\n",i,solve()?"YES":"NO");
	return 0;
}