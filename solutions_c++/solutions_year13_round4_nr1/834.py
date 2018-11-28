#include<cstdio>
#include<set>
using namespace std;
struct node{ int i,x,y,v; };
struct comp
{
	bool operator()(node x,node y)
	{
		if( x.x<y.x ) return true; if( x.x>y.x ) return false;
		if( x.y>y.y ) return true; if( x.y<y.y ) return false;
		if( x.i>y.i ) return true; if( x.i<y.i ) return false;
		return false;
	}
};
set<node,comp> h,h2;
set<node,comp>::iterator it;
int calc(int m,int d,int v)
{
	long long sm;
	sm=(long long)m*(m+1)/2-(long long)(m-d)*(m-d+1)/2;
	sm%=1000002013;
	return (int)((sm*v)%1000002013);
}
int main()
{
int N,T; scanf("%d",&N);
for(T=1;T<=N;T++)
{
	int a,sm,sm2,n,m;
	scanf("%d%d",&m,&n);
	h.clear();
	sm=0;
	for(a=0;a<n;a++)
	{
		node tn;
		int t;
		tn.i=a;
		scanf("%d%d%d",&tn.x,&tn.y,&tn.v);
		sm=(sm+calc(m,tn.y-tn.x,tn.v))%1000002013;
//printf("%d\n",sm);
		h.insert(tn);
		t=tn.x;
		tn.x=tn.y;
		tn.y=t;
		h.insert(tn);
	}
	sm2=0;
	h2.clear();
	for(it=h.begin();it!=h.end();it++)
	{
		if( it->x<it->y )
		{
			h2.insert(*it);
		}
		else
		{
			int v=it->v;
			while( v>0 )
			{
				node tn=*(h2.rbegin());
				if( tn.v<=v )
				{
					v-=tn.v;
					h2.erase(tn);
					sm2=(sm2+calc(m,it->x-tn.x,tn.v))%1000002013;
//printf("%d\n",sm2);
					continue;
				}
				h2.erase(tn);
				tn.v-=v;
				h2.insert(tn);
				sm2=(sm2+calc(m,it->x-tn.x,v))%1000002013;
//printf("%d\n",sm2);
				break;
			}
		}
	}
//printf("%d %d\n",sm,sm2);
	printf("Case #%d: %d",T,(sm-sm2+1000002013)%1000002013);
	printf("\n");
}
	return 0;
}
