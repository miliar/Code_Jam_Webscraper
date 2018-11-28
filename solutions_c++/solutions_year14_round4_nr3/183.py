#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,n,m,w,h,S,T;
struct node
{
	int x[5],y[5];
}a[10010];
int dis[1010][1010];
int b[1010],d[1010];


int calc(int i, int j)
{
	int r = 10000;
	for (int p=1;p<=4;p++) for (int q=1;q<=4;q++)
	{
		int dd = max(abs(a[i].x[p]-a[j].x[q]), abs(a[i].y[p]-a[j].y[q]))-1;
		r = min(r, dd);
	}
	for (int p=1;p<=4;p++)
	{
		if (a[i].y[p] >= a[j].y[1] && a[i].y[p] <= a[j].y[3])
			r = min(r, min(abs(a[j].x[1]-a[i].x[p]), abs(a[j].x[3]-a[i].x[p]))-1);
		if (a[i].x[p] >= a[j].x[1] && a[i].x[p] <= a[j].x[3])
			r = min(r, min(abs(a[j].y[1]-a[i].y[p]), abs(a[j].y[3]-a[i].y[p]))-1);
	}
	for (int p=1;p<=4;p++)
	{
		if (a[j].y[p] >= a[i].y[1] && a[j].y[p] <= a[i].y[3])
			r = min(r, min(abs(a[i].x[1]-a[j].x[p]), abs(a[i].x[3]-a[j].x[p]))-1);
		if (a[j].x[p] >= a[i].x[1] && a[j].x[p] <= a[i].x[3])
			r = min(r, min(abs(a[i].y[1]-a[j].y[p]), abs(a[i].y[3]-a[j].y[p]))-1);
	}
	if (r<0) return 0;
	return r;
}

int main()
{
	freopen("c2.in","r",stdin);
	freopen("c2.out","w",stdout);

	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d%d%d",&w,&h,&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d%d%d%d",&a[i].x[1],&a[i].y[1],&a[i].x[3],&a[i].y[3]);
			a[i].x[2] = a[i].x[3],   a[i].y[2] = a[i].y[1];
			a[i].x[4] = a[i].x[1],   a[i].y[4] = a[i].y[3];
		}
		S = n+1;
		T = n+2;
		for (int i=1;i<=T;i++) for (int j=1;j<=T;j++) dis[i][j] = 10000;
		for (int i=1;i<=n;i++) dis[S][i] = dis[i][S] = a[i].x[1], dis[T][i] = dis[i][T] = w-1-a[i].x[2];
		for (int i=1;i<=n;i++) for (int j=1;j<=n;j++)
			dis[i][j] = dis[j][i] = calc(i,j);
		dis[S][T] = w;
		/*
		for (int i=1;i<=T;i++)
		{
			for (int j=1;j<=T;j++) printf("%3d ",dis[i][j]);
			printf("\n");
		}
		*/
		for (int i=1;i<=T;i++) b[i] = 0, d[i] = 10000;
		b[S] = 1; d[S] = 0;
		for (int i=1;i<=T;i++) d[i] = min(d[i], d[S] + dis[S][i]);
		for (int c=1;c<T;c++)
		{
			int k = 0;
			for (int i=1;i<=T;i++) if (b[i]==0) if (k==0 || d[i]<d[k]) k = i;
			//printf("k=%d\n",k);
			b[k] = 1;
			for (int i=1;i<=T;i++) d[i] = min(d[i], d[k] + dis[k][i]);
		}
		
		
		
		printf("Case #%d: %d\n", test, d[T]);
	}
	
	return 0;
}
