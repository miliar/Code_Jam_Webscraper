#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>

#define TEST_NUM "c1"
//#define DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
char inname[100];
char outname[100];

int arr[1000][6];
double tim[1000][1000][2];
double can[1000][1000][2];
bool val[1000][1000];
bool vit[1000];
bool chk[1000][1000];
bool pre[1000];
const double INF = 10000000000000.0;
int n;

struct str
{
	int h, f;
	double x, y;
	str(int ah = 0, int af = 0, double ax = 0, double ay = 0) : h(ah), f(af), x(ax), y(ay) {}
	bool operator <(const str &a) const
	{
		return y > a.y;
	}
};

std::priority_queue<str> que;

void dfs(int x)
{
	pre[x] = 1;
	int i;
	for(i = 0; i<n; i++)
		if(chk[x][i] && !pre[i])
			dfs(i);
}

void process()
{
	bool ex;
	int s, h, f, bi, i, j, k;
	double a, b, x, y, m, u, v, p, q, r, d;
	scanf("%d%d", &n, &s);
	for(i = 0; i<n; i++)
		for(j = 0; j<6; j++)
			scanf("%d", &arr[i][j]);

	a = 0;
	b = 2000;
	for(bi = 0; a<b && bi<100; bi++)
	{
		m = (a+b)/2;
		memset(chk, 0, sizeof(chk));
		memset(val, 0, sizeof(val));
		memset(pre, 0, sizeof(pre));
		while(!que.empty())
			que.pop();

		for(i = 0; i<n; i++)
		{
			for(j = i+1; j<n; j++)
			{
				r = 0;
				for(k = 0; k<3; k++)
					r += (arr[i][k]-arr[j][k])*(arr[i][k]-arr[j][k]);

				if(sqrt(r)<=m)
					chk[i][j] = chk[j][i] = 1;

				/*p = q = r = 0;
				for(k = 0; k<3; k++)
				{
				p += (arr[i][k+3]-arr[j][k+3])*(arr[i][k+3]-arr[j][k+3]);
				q += 2*(arr[i][k+3]-arr[j][k+3])*(arr[i][k]-arr[j][k]);
				r += (arr[i][k]-arr[j][k])*(arr[i][k]-arr[j][k]);
				}
				r -= m*m;

				if(p==0)
				{
				if(q==0)
				{
				if(r<=0)
				{
				chk[i][j] = chk[j][i] = 1;
				tim[i][j][0] = tim[j][i][0] = -INF;
				tim[i][j][1] = tim[j][i][1] = INF;
				}
				}
				else
				{
				chk[i][j] = chk[j][i] = 1;
				if(b<0)
				{
				tim[i][j][0] = tim[j][i][0] = -r/q;
				tim[i][j][1] = tim[j][i][1] = INF;
				}
				else
				{
				tim[i][j][0] = tim[j][i][0] = -INF;
				tim[i][j][1] = tim[j][i][1] = -r/q;
				}
				}
				}
				else
				{
				d = q*q - 4*p*r;
				if(d<0)
				continue;

				chk[i][j] = chk[j][i] = 1;
				tim[i][j][0] = tim[j][i][0] = (-q - sqrt(d))/(2.0*p);
				tim[i][j][1] = tim[j][i][1] = (-q + sqrt(d))/(2.0*p);
				}
				*/
			}
		}

		dfs(0);
		if(!pre[1])
		{
			a = m;
			continue;
		}
		else
		{
			b = m;
			continue;
		}
		/*

		can[0][0][0] = can[0][0][1] = 0;
		val[0][0] = 1;
		que.push(str(0, 0, 0, 0));
		ex = 0;
		while(!que.empty())
		{
		h = que.top().h;
		f = que.top().f;
		x = que.top().x;
		y = que.top().y;
		que.pop();
		fprintf(stderr, "vit %d %d %lf %lf\n", h, f, x, y);

		if(val[h][f] && can[h][f][0]<x && y<can[h][f][1])
		continue;

		y += s;
		for(i = 0; i<n; i++)
		{
		if(!chk[h][i])
		continue;

		u = std::max(x, tim[h][i][0]);
		v = std::min(y, tim[h][i][1]);

		if(v<u)
		continue;
		if(val[i][h] && can[i][h][0]<=u && v<=can[i][h][1])
		continue;

		if(i==1)
		{
		ex = 1;
		break;
		}

		if(!val[i][h])
		{
		val[i][h] = 1;
		can[i][h][0] = u;
		can[i][h][1] = v;
		}
		else
		{
		can[i][h][0] = std::min(can[i][h][0], u);
		can[i][h][1] = std::max(can[i][h][1], v);
		}
		que.push(str(i, h, u, v));
		}
		if(ex)
		break;
		}
		if(ex)
		b = m;
		else
		a = m;*/
	}
	printf("%.10lf", (a+b)/2);
}

void pre_process()
{

}

int main()
{
#ifndef DEBUGGGGGGGGGGGGGGGGGGGGGGGGGG
	sprintf(inname, "%s.in", TEST_NUM);
	sprintf(outname, "%s.out", TEST_NUM);
#endif
	freopen(inname, "r", stdin);
	freopen(outname, "w", stdout);
	int tn, ti;
	scanf("%d", &tn);
	pre_process();
	for(ti = 1; ti<=tn; ti++)
	{
		fprintf(stderr, "\n%d\n", ti);
		printf("Case #%d: ", ti);
		process();
		printf("\n");
	}
	return 0;
}