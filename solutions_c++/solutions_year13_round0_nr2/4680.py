/*
 * main.cpp
 *
 *  Created on: 2013-4-9
 *      Author: whd
 */
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#define pb push_back
#define mp make_pair
#define x first
#define y second
using namespace std;

typedef long long big;
int n,m;
int f[127][127][2],a[127][127];
const double eps=1e-9,PI=acos(-1.0);
int sgn(double x)
{
    if(fabs(x)<eps)return 0;
	return x>0?1:-1;
}
void check()
{
	int i,j,k,s;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
		{
			if(f[i][j][0]>a[i][j]&&f[i][j][1]>a[i][j])
			{
				puts("NO");
				return ;
			}
		}
	puts("YES");
}
bool ck1(int x,int y)
{
	int i;
	for(i=y-1;i;i--)
		if(a[x][i]>a[x][y])return true;
	return false;
}
bool ck2(int x,int y)
{
	int i;
	for(i=x-1;i;i--)
		if(a[i][y]>a[x][y])return true;
	return false;
}
bool ck3(int x,int y)
{
	int i;
	for(i=y+1;i<=m;i++)
		if(a[x][i]>a[x][y])return true;
	return false;
}
bool ck4(int x,int y)
{
	int i;
	for(i=x+1;i<=n;i++)
		if(a[i][y]>a[x][y])return true;
	return false;
}
void ck()
{
	int i,j;
	for(i=1;i<=n;i++)
		for(j=1;j<=m;j++)
			if((ck1(i,j)||ck3(i,j))&&(ck2(i,j)||ck4(i,j)))
			{
				printf("NO");
				return ;
			}
	printf("YES");
}
int main()
{
	int i,j,cass,cas,x,y,z;
	freopen("B-large.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&cas);
	for(cass=1;cass<=cas;cass++)
	{
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		printf("Case #%d: ",cass);
		ck();
		printf("\n");
	}
}
