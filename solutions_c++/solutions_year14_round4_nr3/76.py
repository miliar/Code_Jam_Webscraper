#include <cstdio>
#include <cstring>

int w,h,test,b,ans;
int d[1005];
int x0[1005],y0[1005],x1[1005],y1[1005];
bool bo[1005];

int Max(int a,int b) { return a > b ? a : b; }

int dist(int a,int b)
{
	int res = 0;
	res = Max(res,x0[b] - x1[a] - 1);
	res = Max(res,x0[a] - x1[b] - 1);
	res = Max(res,y0[b] - y1[a] - 1);
	res = Max(res,y0[a] - y1[b] - 1);
	return res;
}

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&test);
	for (int T = 1; T <= test; T++)
	{
		scanf("%d%d%d",&w,&h,&b);
		for (int i = 1; i <= b; i++) scanf("%d%d%d%d",x0 + i,y0 + i,x1 + i,y1 + i);
		memset(d,-1,sizeof d);
		memset(bo,false,sizeof bo);
		b++;
		x0[0] = -1; y0[0] = 0;
		x1[0] = -1; y1[0] = h - 1;
		x0[b] = w; y0[b] = 0;
		x1[b] = w; y1[b] = h - 1;
		d[0] = 0;
		bo[0] = true;
		for (int i = 1; i <= b; i++) d[i] = dist(0,i);
		while (!bo[b])
		{
			int k = -1;
			for (int i = 1; i <= b; i++) if (!bo[i] && (k == -1 || d[i] < d[k]))
				k = i;
			bo[k] = true;
			for (int i = 1; i <= b; i++) if (d[i] > d[k] + dist(i,k))
				d[i] = d[k] + dist(i,k);
		}
		printf("Case #%d: %d\n",T,d[b]);
	}
}
