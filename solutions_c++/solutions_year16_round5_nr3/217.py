#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
struct Point
{
	double x,y,z;
	double l;
	void in()
	{
		scanf("%lf %lf %lf",&x,&y,&z);
		for(int i=0;i<3;i++)
			scanf("%lf",&l);
	}
};
double ddd(Point a,Point b)
{
	double x=a.x-b.x;
	double y=a.y-b.y;
	double z=a.z-b.z;
	return sqrt(x*x+y*y+z*z);
}
struct E
{
	double s;
	int x,y;
	E(){}
	E(double s0,int x0,int y0):s(s0),x(x0),y(y0){}
};
bool cmp(E a,E b)
{
	return a.s < b.s;
}
E pp[1000010];
int qq;
Point p[100010];
int fa[100010];
int find(int x)
{
	if(fa[x] != x)
		fa[x]=find(fa[x]);
	return fa[x];
}
void uunion(int x,int y)
{
	int fx=find(x);
	int fy=find(y);
	fa[fx]=fy;
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
//	freopen("A.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,dummy;
		scanf("%d %d",&n,&dummy);
		for(int i=0;i<n;i++)
			p[i].in();
		qq=0;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				pp[qq++]=E(ddd(p[i],p[j]),i,j);
		sort(pp,pp+qq,cmp);
		for(int i=0;i<n;i++)
			fa[i]=i;
		for(int i=0;i<qq;i++)
		{
			uunion(pp[i].x,pp[i].y);
			if(find(0) == find(1))
			{
				printf("Case #%d: %.12f\n",cc,pp[i].s);
				break;
			}
		}
	}
	return 0;
}
/*
3
3 7
0 0 0 0 0 0
1 2 2 0 0 0
1 1 1 0 0 0
5 10
0 0 0 0 0 0
35 0 0 -1 0 0
1 54 0 0 -2 0
2 -150 0 0 10 0
4 0 0 -1 0 0
3 1
-10 2 0 1 0 0
0 0 10 0 0 -1
-10 -2 0 1 0 0

 */
