#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int MAXM = 2000000;
const int MAXN = 111111;
const int INF = 0x7FFFFFFF;

struct ARC
{
	int y;
	int c;
	ARC* Next;
	ARC* R;
};

ARC APool[MAXM*2];
ARC* APTop = APool;
ARC* Arc[MAXN];

int insert_arc(int x,int y,int c,int rc=0)
{
	ARC* fore = APTop++;
	fore->y = y; fore->c = c; fore->Next = Arc[x]; Arc[x] = fore;
	ARC* back = APTop++;
	back->y = x; back->c = rc; back->Next = Arc[y]; Arc[y] = back;

	fore->R = back; back->R = fore;
	return 0;
}

int init_arc_ds()
{
	memset(Arc,0,sizeof(Arc));
	APTop = APool;
	return 0;
}

int dis[MAXN];
ARC* curArc[MAXN];
int pre[MAXN];
int gap[MAXN];
// God damn SAP :D
int max_flow(int s,int t,int n)
{
	memset(dis,0,sizeof(dis));
	memset(curArc,0,sizeof(curArc));
	memset(gap,0,sizeof(gap));
	gap[0] = n;

	int maxflow = 0;
	int x = s;
	while(dis[s] < n)
	{
		if(x == t)
		{
			int tflow = INF;
			while(x != s)
			{
				tflow = min(tflow,curArc[pre[x]]->c);
				x = pre[x];
			}
			x = t;
			while(x != s)
			{
				curArc[pre[x]]->c -= tflow;
				curArc[pre[x]]->R->c += tflow;
				x = pre[x];
			}
			maxflow += tflow;
			continue;
		}
		if(!curArc[x]) curArc[x] = Arc[x];
		ARC* ar = curArc[x];
		for(;ar;ar = ar->Next)
		{
			int y = ar->y;
			int c = ar->c;
			if(!c) continue;
			if(dis[y]+1 == dis[x]) break;
		}
		curArc[x] = ar;
		if(!ar)
		{
			// relabel
			int mindis = n+1;
			for(ARC* a = Arc[x];a;a = a->Next) if(a->c) mindis = min(mindis,dis[a->y]+1);
			gap[dis[x]]--;
			if(!gap[dis[x]]) break;
			gap[dis[x] = mindis]++;
			if(x != s) x = pre[x];
		}
		else
		{
			pre[ar->y] = x;
			x = ar->y;
		}
	}
	return maxflow;
}

bool grid[111][555];
const int dx[4] = {1,-1,0,0};
const int dy[4] = {0,0,1,-1};

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		fprintf(stderr,"Running case %d..\n",TK);
		init_arc_ds();
		memset(grid,0,sizeof(grid));
		int W = 0;
		int H = 0;
		int B = 0;
		scanf("%d %d %d",&W,&H,&B);
		for(int i = 0;i < B;i++)
		{
			int x0 = 0;
			int y0 = 0;
			int x1 = 0;
			int y1 = 0;
			scanf("%d %d %d %d",&x0,&y0,&x1,&y1);
			for(int x = x0;x <= x1;x++) for(int y = y0;y <= y1;y++) grid[x][y] = true;
		}


		int s = W*H*2+1;
		int t = W*H*2+2;
		#define in(x,y) ((((x)*H)+(y))*2)
		#define out(x,y) ((((x)*H)+(y))*2+1)
		for(int i = 0;i < W;i++)
		{
			for(int j = 0;j < H;j++)
			{
				if(grid[i][j]) continue;
				if(j == 0) insert_arc(s,in(i,j),1);
				if(j == H-1) insert_arc(out(i,j),t,1);

				insert_arc(in(i,j),out(i,j),1);
				for(int k = 0;k < 4;k++)
				{
					int nx = i + dx[k];
					int ny = j + dy[k];
					if(nx >= 0 && nx < W && ny >= 0 && ny < H && !grid[nx][ny])
					{
						insert_arc(out(i,j),in(nx,ny),INF);
					}
				}
			}
		}
		printf("%d\n",max_flow(s,t,t+1));
	}
	while(getchar() != EOF);
	return 0;
}