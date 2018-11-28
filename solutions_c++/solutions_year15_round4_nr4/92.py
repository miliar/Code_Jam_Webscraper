#include <bits/stdc++.h>
using namespace std;

const int D[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
int ans,S,N,M,a[10][10],A[105][10][10];

void init()
{
	ans=0;
	scanf("%d%d",&N,&M);
}

int get(int x,int y,int t)
{
	int s=0;
	for (int i=0; i<4; i++)
	{
		int xx=x+D[i][0],yy=y+D[i][1];
		if (xx<1||xx>N) continue;
		if (yy<1) yy=M;
		if (yy>M) yy=1;
		if (a[xx][yy]==t) s++;
	}
	return s;
}

bool cmp(int a[10][10],int b[10][10])
{
/*	for (int i=1; i<=N; i++){
		for (int j=1; j<=M; j++) cout<<" "<<a[i][j];cout<<endl;}
		for (int i=1; i<=N; i++){
		for (int j=1; j<=M; j++) cout<<"  "<<b[i][j];cout<<endl;}*/
	for (int t=0; t<M; t++)
	{
		bool ok=1;
		for (int i=1; i<=N; i++)
			for (int j=1; j<=M; j++) if (a[i][j]!=b[i][(j+t-1)%M+1]) ok=0;
		if (ok) {return 1;}
	}
	return 0;
}

void dfs(int x,int y)
{
	if (x>N) {dfs(1,y+1); return;}
	if (y>M)
	{
		for (int i=1; i<=N; i++)
			for (int j=1; j<=M; j++) if (get(i,j,a[i][j])!=a[i][j]) return;
		for (int i=1; i<=S; i++) if (cmp(A[i],a)) return;
		S++;
		memcpy(A[S],a,sizeof(a));
	/*	for (int i=1; i<=N; i++){
			for (int j=1; j<=M; j++) cout<<a[i][j];cout<<endl;}
			cout<<endl;*/
		
		return;
	}
	for (int i=1; i<=3; i++) if (get(x,y,i)<=i)
	{
		a[x][y]=i;
		if (y>1&&get(x,y-1,a[x][y-1])>a[x][y-1]) {a[x][y]=0; continue;}
		if (y>2&&get(x,y-1,a[x][y-1])!=a[x][y-1]) {a[x][y]=0; continue;}
	//	if (x>1&&get(x-1,y,a[x-1][y])>a[x-1][y]) continue;
		dfs(x+1,y);
		a[x][y]=0;
	}
}

void doit()
{
	S=0;
	dfs(1,1);
	cout<<S<<endl;
	//cout<<ans/M<<endl;
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
2 1 1 3
2 3 2 2
3 1 1 5
5 3 1 5
4 3 2 19
*/
