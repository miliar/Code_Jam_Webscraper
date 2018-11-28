#include <iostream>
#include <cstdio>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;


const int mod=1000002013;
struct ss{ int t,ty,p; } a[1010],tmp;
priority_queue <ss> q;
int n,m,x,y,p,T,cnt;

bool cmp(ss a,ss b)
{
	return a.t<b.t || a.t==b.t && a.ty;
}

bool operator <(ss a,ss b){ return a.t<b.t; }

long long cost(int st,int en,int p)
{
	long long dis=en-st;
	return (((n+n+1-dis)*dis)%(mod+mod)*p)%(mod+mod);
}

int main()
{
	freopen("a.in","r",stdin);
	int TT=0;
	scanf("%d",&T);
	while (T--)
	{
		long long ans=0;
		scanf("%d%d",&n,&m);
		cnt=0;
		for (int i=1;i<=m;i++)
		{
			scanf("%d%d%d",&x,&y,&p);
			(ans+=cost(x,y,p))%=(mod+mod);
			a[++cnt].t=x;a[cnt].ty=1;a[cnt].p=p;
			a[++cnt].t=y;a[cnt].ty=0;a[cnt].p=p;
		}
		sort(&a[1],&a[cnt+1],cmp);
		while (!q.empty()) q.pop();
		for (int i=1;i<=cnt;i++)
		{
			if (!a[i].ty)
			{
				while (a[i].p)
				{
					tmp=q.top();
					q.pop();
					if (tmp.p<=a[i].p)
					{
						a[i].p-=tmp.p;
						(ans-=cost(tmp.t,a[i].t,tmp.p))%=(mod+mod);
					}else
					{
						tmp.p-=a[i].p;
						(ans-=cost(tmp.t,a[i].t,a[i].p))%=(mod+mod);
						q.push(tmp);
						break;
					}
				}
			}else
			{
				q.push(a[i]);
			}
		}
		cout<<"Case #"<<++TT<<": "<<ans/2<<endl;
	}
	
	return 0;
}