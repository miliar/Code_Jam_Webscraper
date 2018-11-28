#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int T,N,M,R;
long long Fee1,Fee2;
struct travel
{	
	int isb,pos,p;
}ts[2009];
inline int cmp(const travel &a ,const travel &b)
{
	return a.pos<b.pos || (a.pos==b.pos && a.isb<b.isb);
}
inline long long fee(int i)
{	
	return ((long long)(N+N-i+1)*i)>>1;
}
int main()
{
	scanf("%d",&T);
	int TT;
	for (TT=1;TT<=T;TT++)
	{
		scanf("%d%d",&N,&M);
		int i,j;
		Fee1=Fee2=0;
		R=0;
		for (i=1;i<=M;i++)
		{
			int b,e,p;
			scanf("%d%d%d",&b,&e,&p);
			Fee1+=fee(e-b)*p;
			ts[++R].isb=0;ts[R].pos=b;ts[R].p=p;
			ts[++R].isb=1;ts[R].pos=e;ts[R].p=p;
		}
		sort(ts+1,ts+2*M+1,cmp);
		for (i=1;i<=2*M;i++)
		{
			if (ts[i].isb==1)//end
			{
				for (j=i-1;j>=1 && ts[i].p>0;j--)
					if (ts[j].isb==0 && ts[j].p>0)//begin
					{
						if (ts[i].p>ts[j].p)
						{
							Fee2+=ts[j].p*fee(ts[i].pos-ts[j].pos);
							ts[i].p-=ts[j].p;
							ts[j].p=0;
						}
						else
						{
							Fee2+=ts[i].p*fee(ts[i].pos-ts[j].pos);
							ts[j].p-=ts[i].p;
							ts[i].p=0;
						}
					}
			}
		}
		//
		printf("Case #%d: %lld\n",TT,Fee1-Fee2);
	}
}