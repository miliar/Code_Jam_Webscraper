#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int maxl = 605;

bool mp[maxl][maxl];

int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};

const int maxn = maxl*maxl*2;
const int inf = 1<<29;

int n,m,tot,start,end;
int head[maxn],cpyh[maxn],q[maxn],d[maxn];

struct edge
{
    int from,to,next,val;
} ji[maxn*20];

void add(int x,int y,int w)
{
    ji[tot].from = x;
    ji[tot].to = y;
    ji[tot].val = w;
    ji[tot].next = head[x];
    head[x] = tot++;
    ji[tot].from = y;
    ji[tot].to = x;
    ji[tot].val = 0;
    ji[tot].next = head[y];
    head[y] = tot++;
}

int dinic()
{
    int max_flow = 0;
    while(true)
    {
        memset(d,-1,sizeof(d));
        int front=0,tail=0;
        q[tail++] = start;
        d[start] = 0;
        while(front<tail)
        {
            int t = q[front++];
            for(int k = head[t];k;k=ji[k].next)
            {
                int toit = ji[k].to;
				int val = ji[k].val;
                if(val&&d[toit]==-1)
                {
                    d[toit] = d[t] + 1;
                    q[tail++] = toit;
                    if(toit==end)
                    {
                        front = tail;
                        break;
                    }
                }
            }
        }
        if(d[end]==-1)
            break;
        memcpy(cpyh,head,(end+1)*sizeof(int));
        for(int i=start,top=0;;)
        {
            if(i==end)
            {
                int flow,st;
                flow = inf;
                for(int k=0;k<top;k++)
                {
                    if(ji[q[k]].val<flow)
                    {
                        st = k;
                        flow = ji[q[st]].val;
                    }
                }
                for(int k=0;k<top;k++)
                {
                    ji[q[k]].val -= flow;
                    ji[q[k]^1].val +=flow;
                }
                max_flow += flow;
                top = st;
                i = ji[q[top]].from;
            }
            for(int j=cpyh[i];j;j=cpyh[i]=ji[j].next)
                if(ji[j].val>0&&d[i]+1==d[ji[j].to])
                    break;
            if(cpyh[i])
            {
                q[top++] = cpyh[i];
                i = ji[cpyh[i]].to;
            }
            else
            {
                if(top==0)
                    break;
                d[i] = -1;
                i = ji[q[--top]].from;
            }
        }
    }
    return max_flow;
}

int main()
{
	int t,w,h,bu,a,b,c,d,cas=0;
	scanf("%d",&t);
	while(t--)
	{
		memset(head,0,sizeof(head));tot = 2;
		memset(mp,0,sizeof(mp));
		scanf("%d%d%d",&w,&h,&bu);
		while(bu--)
		{
			scanf("%d%d%d%d",&a,&b,&c,&d);
			for(int i=a;i<=c;i++)
			{
				for(int j=b;j<=d;j++)
				{
					mp[i][j] = 1;
				}
			}
		}
		end = h*w*2 + 1;
		for(int i=0;i<w;i++)
		{
			for(int j=0;j<h;j++)
			{
				int p = i*h + j + 1;
				if(j==0)
				{
					add(0,p,1);
				}
				if(j==h-1)
				{
					add(p+h*w,end,1);
				}
				if(mp[i][j]==0)
				{
					add(p,p+h*w,1);
					int px = i,py = j;
					for(int k=0;k<4;k++)
					{
						int nx = px + dx[k],ny = py + dy[k];
						if(nx>=0&&nx<w&&ny>=0&&ny<h)
						{
							add(p+h*w,nx*h+ny+1,1);
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",++cas,dinic());
	}
}
