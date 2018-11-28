//*
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <functional>
#define MOD 1000000007
#define MAX 0x3f3f3f3f
#define MAX2 0x3f3f3f3f3f3f3f3fll
#define ERR 1e-10
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#pragma warning(disable:4996)
using namespace std;

typedef long long ll;
typedef long double ldb;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;

int n, m;

int dat[200][200][4];

pair<pii, pii> pdat[200][200];
int ans[200][200];

int ui;

int u[200];

pii a[200];

int find(int x)
{
	return u[x]==x?x:u[x]=find(u[x]);
}

void dodo()
{
	int i, j, k;
	map<int, pii> mq;
	int xi=1;
	int tog=0;
	for(i=0;i<m;i++)
	{
		mq[xi++]=pii(dat[0][i][0], tog);
		tog^=1;
	}
	for(i=0;i<n;i++)
	{
		mq[xi++]=pii(dat[i][m-1][1], tog);
		tog^=1;
	}
	for(i=m-1;i>=0;i--)
	{
		mq[xi++]=pii(dat[n-1][i][2], tog);
		tog^=1;
	}
	for(i=n-1;i>=0;i--)
	{
		mq[xi++]=pii(dat[i][0][3], tog);
		tog^=1;
	}
	for(i=0;i<n+m;i++)
	{
		scanf("%d%d", &a[i].first, &a[i].second);
	}
	for(i=0;i<(1<<n*m);i++)
	{
		for(j=0;j<n*m;j++) ans[j/m][j%m]=!!(i&(1<<j));
		for(j=0;j<ui;j++) u[j]=j;
		for(j=0;j<n;j++) for(k=0;k<m;k++)
		{
			if(ans[j][k] == 0)
			{
				int x=dat[j][k][0], y=dat[j][k][3];
				u[find(x)]=find(y);
				x=dat[j][k][1], y=dat[j][k][2];
				u[find(x)]=find(y);
			}
			else
			{
				int x=dat[j][k][0], y=dat[j][k][1];
				u[find(x)]=find(y);
				x=dat[j][k][3], y=dat[j][k][2];
				u[find(x)]=find(y);
			}
		}
		int flag=0;
		for(j=0;j<n+m;j++)
		{
			int x=mq[a[j].first].first, y=mq[a[j].second].first;
			if(find(x) != find(y))
			{
				flag=1;
				break;
			}
		}
		if(flag) continue;
		for(j=0;j<n;j++)
		{
			for(k=0;k<m;k++)
			{
				if(ans[j][k] == 0) printf("/");
				else printf("\\");
			}
			printf("\n");
		}
		return;
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
	int i, j, k, l;
	int T, TT;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>TT;
	for(T=1;T<=TT;T++)
	{
		printf("Case #%d:\n", T);
		cin>>n>>m;
		ui=0;
		for(i=0;i<m;i++)
		{
			dat[0][i][0]=ui++;
		}
		for(i=0;i<n;i++)
		{
			dat[i][0][3]=ui++;
			for(j=0;j<m;j++)
			{
				dat[i][j][1]=ui;
				dat[i][j+1][3]=ui++;
			}
			for(j=0;j<m;j++)
			{
				dat[i][j][2]=ui;
				dat[i+1][j][0]=ui++;
			}
		}
		dodo();
	}
	return 0;
}
//*/