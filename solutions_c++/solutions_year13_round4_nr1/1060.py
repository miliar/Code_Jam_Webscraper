#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define M 200001
#define Max(a, b) a > b ? a : b
#define Min(a, b) a < b ? a : b
#define inf 0xffffff
struct T
{
    int from, to, val;
    int next, cost;
}edge[M];
int len;
int visit[M], pre[M], dist[M], que[M], vis[M], pos[M];
void init()
{
    memset(vis,-1,sizeof(vis));
    len=0;
}
void add(int from, int to, int val, int cost)
{
    edge[len].from = from,edge[len].to = to, edge[len].val = val, edge[len].cost = cost;
    edge[len].next = vis[from], vis[from] = len++;
    edge[len].from = to, edge[len].to = from, edge[len].val = 0, edge[len].cost = -cost;
    edge[len].next = vis[to], vis[to] = len++;
}
int SPFA(int s, int t, int n)
{
    int i, to, k;
    for (i = 0; i <= n; i++)
    {
        pre[i] = -1, visit[i] = 0;
    }
    int head, tail;
    head = tail = 0;
    for (i = 0; i <= n; i++)
        dist[i] = -inf;//求最小费用时这里得改成正无穷
    que[tail++] = s, pre[s] = s, dist[s] = 0, visit[s] = 1;
    while (head != tail)
    {
        int from = que[head++];
        visit[from] = 0;
        for (k = vis[from]; k != -1; k = edge[k].next)
        {
            to = edge[k].to;
            if (edge[k].val > 0 && dist[from]+edge[k].cost > dist[to])//最大费用，求最小费用时这里的改符号
            {
                dist[to] = dist[from] + edge[k].cost;
                pre[to] = from;
                pos[to] = k;
                if (!visit[to])
                {
                    visit[to] = 1;
                    que[tail++] = to;
                }
            }
        }
    }
    if (pre[t] != -1 && dist[t] > -inf)//求最小费用时这里改成dit[t] < 正无穷 
        return 1;
    return 0;
}
int MinCostFlow(int s, int t, int n)
{
    if (s == t)
    {
        //这里具体情况具体分析，如果有附加s跟t就不用，如果用数据中的点作为s跟t就得考虑
        //直接返回某个值。否则SPFA里的队列会死循环。
		return 0;
    }
    int flow = 0, cost = 0;
    while (SPFA(s, t, n))
    {
        int from, min = inf;
        for (from = t; from != s; from = pre[from])
            min = Min(min, edge[pos[from]].val);
        flow += min;
        cost += dist[t] * min;
        for (from = t; from != s; from = pre[from])
        {
            edge[pos[from]].val -= min;
            edge[pos[from]^1].val += min;
        }
    }
    return cost;
}

int oo[M], ee[M];
int no[M], ne[M];
int lo, le;

void addo(int o, int p)
{
	for (int i = 1; i <= lo; ++i)
	{
		if (oo[i] == o)
		{
			no[i] += p;
			return;
		}
	}
	lo++;
	oo[lo] = o;
	no[lo] = p;
	
}

void adde(int e, int p)
{
	for (int i = 1; i <= le; ++i)
	{
		if (ee[i] == e)
		{
			ne[i] += p;
			return;
		}
	}
	le++;
	ee[le] = e;
	ne[le] = p;
	
}

int main()
{
	freopen("A-small-attempt0.in" , "r", stdin);
	freopen("A-small-attempt0.out" , "w", stdout);
    int n,m;
	long long ans;
	int T;
	scanf("%d", &T);
	int nt = 0;
    while (T--)
    {
		scanf("%d%d", &n, &m);
        init();
		lo = le = 0;
		int o, e, p;

		long long preAns = 0;
		for (int i = 0; i < m; ++i)
		{
			scanf("%d%d%d", &o, &e, &p);
			addo(o, p);
			adde(e, p);
			preAns += (e-o)*(e-o-1)/2*p;
		}
		int t = lo + le + 1;
		for (int i = 1; i <= lo; ++i)
		{
			for (int j = 1; j <= le; ++j)
			{
				if (oo[i] <= ee[j])
				{
					add(i, lo+j, inf, (ee[j]-oo[i])*(ee[j]-oo[i]-1)/2);
				}
			}
		}
		for (int i = 1; i <= lo; ++i)
		{
			add(0, i, no[i], 0);
		}
		for (int j = 1; j <= le; ++j)
		{
				add(lo+j, t, ne[j], 0);
		}
        ans = MinCostFlow(0, t, t + 1);
        printf("Case #%d: %lld\n", ++nt, (ans-preAns) % 1000002013);
    }
    return 0;
}