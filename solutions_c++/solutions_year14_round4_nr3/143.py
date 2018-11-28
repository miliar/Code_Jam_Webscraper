#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
#define MAXB 1110

const int inf = (int)2e8;

struct point
{
	int x,y;
};

struct rect
{
	point P[4];
}A[MAXB];

int T,B;

int D[MAXB],N;
bool Vis[MAXB];
int G[MAXB][MAXB];

int dis(const point &a, const point &b)
{
	return max(abs(a.x - b.x),abs(a.y - b.y)) - 1;
}

int dis(const point &a, const point &b, const point &c)
{
	if (b.y == c.y)
	{
		int xmin = min(b.x,c.x);
		int xmax = max(b.x,c.x);
		if (xmin <= a.x && a.x <= xmax)
		{
			return abs(a.y - b.y) - 1;
		}
	}
	else
	{
		int ymin = min(b.y,c.y);
		int ymax = max(b.y,c.y);
		if (ymin <= a.y && a.y <= ymax)
		{
			return abs(a.x - b.x) - 1;
		}
	}
	return min(dis(a,b), dis(a,c));
}

int calc0(const rect &a, const rect &b)
{
	int i,j;
	int ret = inf;
	for (i=0;i<4;i++)
	{
		for (j=0;j<3;j++)
		{
			ret = min(ret, dis(a.P[i],b.P[j],b.P[j+1]));
		}
		ret = min(ret, dis(a.P[i], b.P[3], b.P[0]));
	}
	return ret;
}

int calc(const rect &a, const rect &b)
{
	return min(calc0(a,b), calc0(b,a));
}



int W;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int i,j;
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%*d%d",&W,&B);
		for (i=0;i<B;i++)
		{
			point *P = A[i].P;
			scanf("%d%d%d%d",&P[0].x,&P[0].y,&P[2].x,&P[2].y);
			P[1].x = P[2].x;
			P[1].y = P[0].y;
			P[3].x = P[0].x;
			P[3].y = P[2].y;
		}
		N = B + 2;
		for (i=0;i<B;i++)
		{
			G[i][i] = 0;
			for (j=i+1;j<B;j++)
			{
				G[i][j] = G[j][i] = calc(A[i],A[j]);
			}
		}
		G[B][B+1] = G[B+1][B] = W;
		for (i=0;i<B;i++)
		{
			G[B][i] = A[i].P[0].x;
			G[i][B+1] = W - A[i].P[2].x - 1;
		}
		memset(Vis,0,sizeof Vis);
		memset(D,0x20,sizeof D);
		D[B] = 0;
		i = B;
		Vis[B] = 1;
		while (1)
		{
			for (j=0;j<N;j++)
				D[j] = min(D[j],D[i] + G[i][j]);
			i = B+2;
			for (j=0;j<N;j++)
				if (D[j] < D[i] && !Vis[j])
				{
					i = j;
				}
			if (i == B+2)
			{
				break;
			}
			Vis[i] = 1;
		}
		printf("Case #%d: %d\n",cases,D[B+1]);
	}
    return 0;
}
