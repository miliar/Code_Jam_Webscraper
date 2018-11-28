#include<cstdio>
#include<algorithm>
#include<stack>

#define MAX 1000
#define FI 1000002013

template<typename T>
T min(T a, T b)
{
	return (a<b)?a:b;
}

struct ev
{
	bool beg;
	int from;
	int to;
	int count;
} event[MAX*2+10];

bool comp1(ev a, ev b)
{
	int _a = (a.beg)?a.from:a.to;
	int _b = (b.beg)?b.from:b.to;
	if(_a == _b)
		return (a.beg)?(!b.beg):0;
	else
		return _a<_b;
}
struct ticket
{
	int count;
	int from;
	ticket(int _c, int _f):count(_c),from(_f){}
	ticket(){}
};
ticket ticks[MAX+10];
int tick_c = 0;

int main()
{
	int T; scanf("%d",&T);
	for(int ii = 0; ii < T; ii++)
	{
		long long cost = 0;
		long long c_fi = 0;
		tick_c = 0;
		int N, M;
		scanf("%d%d",&N,&M);
		for(int i = 0; i < M; i++)
		{
			int o, e, p; scanf("%d%d%d",&o,&e,&p);
			event[i*2].beg = 1;
			event[i*2+1].beg = 0;
			event[i*2].from = event[i*2+1].from = o;
			event[i*2].to = event[i*2+1].to = e;
			event[i*2].count = event[i*2+1].count = p;
		}
		std::sort(event,event+(M*2),comp1);
		for(int i = 0; i < M*2; i++)
		{
			if(event[i].beg)
				ticks[tick_c++] = ticket(event[i].count,event[i].from);
			else
				while(event[i].count)
				{
					int pass = min(event[i].count,ticks[tick_c-1].count);
					int n1 = event[i].to-event[i].from;
					int n2 = event[i].to-ticks[tick_c-1].from;
					int awaited = N*n1-((n1-1)*n1)/2;
					int real = N*n2-((n2-1)*n2)/2;
					cost += (long long)(awaited-real)*pass;
					while(cost>FI) {cost -= FI; c_fi++;}
					while(cost<0 && c_fi) {cost += FI; c_fi--;}
					event[i].count -= pass;
					ticks[tick_c-1].count -= pass;
					if(!ticks[tick_c-1].count) tick_c--;
				}
		}
		printf("Case #%d: %lld\n",ii+1,cost);
	}
	return 0;
}
