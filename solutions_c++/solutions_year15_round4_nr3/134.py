#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int,int> pii;

const int MAXM = 10000000;
const int MAXN = 100000;
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
	//fprintf(stderr," %d -> %d (%d)\n",x,y,c);
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

map<string, int> wordidx;
int getidx(const string& x)
{
	auto it = wordidx.find(x);
	if(it == wordidx.end())
	{
		int t = wordidx.size();
		wordidx[x] = t;
		return t;
	}
	return it->second;
}

bool visen[233333];
bool visfr[233333];
char line[2333333];
vector<int> sentence[233];

int main(void)
{
	//freopen("C:\\Users\\Riatre\\Desktop\\GCJ2015\\R2\\C-small-attempt0.in","rt",stdin);
	int T = 0;
	int TK = 0;
	scanf("%d\n",&T);
	while(T--)
	{
		int N = 0;
		scanf("%d\n",&N);
		wordidx.clear();

		for(int i = 0;i < N;i++)
		{
			sentence[i].clear();
			gets(line);
			char* token = strtok(line, " ");
			do 
			{
				sentence[i].push_back(getidx(token));
			} while((token = strtok(NULL, " ")));
		}

		memset(visen,0,sizeof(visen));
		memset(visfr,0,sizeof(visfr));
		init_arc_ds();
		int s = wordidx.size() * 2;
		int t = s + 1;
		for(auto x: sentence[0])
		{
			if(!visen[x])
			{
				insert_arc(s, x*2, INF);
				visen[x] = true;
			}
		}
		for(auto x: sentence[1])
		{
			if(!visfr[x])
			{
				insert_arc(x*2+1, t, INF);
				visfr[x] = true;
			}
		}
		for(int i = 0;i < wordidx.size();i++)
		{
			insert_arc(i*2, i*2+1, 1);
		}

		for(int i = 0;i < N;i++)
		{
			for(int j = 0;j < sentence[i].size();j++)
			{
				for(int k = 0;k < sentence[i].size();k++)
				{
					//insert_arc(sentence[i][j]*2, sentence[i][k]*2+1, INF);
					insert_arc(sentence[i][j]*2+1, sentence[i][k]*2, INF);
				}
			}
		}

		printf("Case #%d: ",++TK);
		printf("%d\n",max_flow(s,t,t+1));
	}
	while(getchar() != EOF);
	return 0;
}
