#include<cstdio>
#include<set>

int sx[1002];
int sy[1002];
int ex[1002];
int ey[1002];
int d[1002];

struct vertex
{
	int v;
	int dist;
} tv;

inline bool operator <(const vertex &a,const vertex &b)
{
	if(a.dist!=b.dist)return a.dist<b.dist;
	return a.v<b.v;
}

int dist(int a,int b)
{
	int x,y;
	if(ex[a]>sx[b]&&ex[b]>sx[a])x=0;
	else x=sx[a]<sx[b]?sx[b]-ex[a]:sx[a]-ex[b];
	if(ey[a]>sy[b]&&ey[b]>sy[a])y=0;
	else y=sy[a]<sy[b]?sy[b]-ey[a]:sy[a]-ey[b];
	return x>y?x:y;
}

std::set<vertex> S;
std::set<vertex>::iterator it;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tc,tcn;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++)
	{
		int i,j,k,l,w,h,b;
		scanf("%d%d%d",&w,&h,&b);
		sx[0]=-1;
		sy[0]=0;
		ex[0]=0;
		ey[0]=h;
		sx[b+1]=w;
		sy[b+1]=0;
		ex[b+1]=w+1;
		ey[b+1]=h;
		for(i=0;i<=b+1;i++)d[i]=-1;
		for(i=1;i<=b;i++)
		{
			scanf("%d%d%d%d",&sx[i],&sy[i],&ex[i],&ey[i]);
			ex[i]++;
			ey[i]++;
		}
		tv.v=0;
		tv.dist=d[0]=0;
		S.insert(tv);
		while(!S.empty())
		{
			it=S.begin();
			for(i=0;i<=b+1;i++)
			{
				if(d[i]<0)
				{
					tv.v=i;
					tv.dist=d[i]=it->dist+dist(it->v,i);
					S.insert(tv);
				}
				else if(d[i]>it->dist+dist(it->v,i))
				{
					tv.v=i;
					tv.dist=d[i];
					S.erase(tv);
					tv.dist=d[i]=it->dist+dist(it->v,i);
					S.insert(tv);
				}
			}
			S.erase(it);
		}
		printf("Case #%d: %d\n",tc,d[b+1]);
	}
}