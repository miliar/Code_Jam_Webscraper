//Grzegorz Prusak
#include <cstdio>
#include <algorithm>
#include <vector>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

template<typename T> void checkmin(T &a, T b){ if(a>b) a = b; }

typedef long long LL;

enum { M = 1000002013 };
enum { m_max = 3000 };

struct Event
{
	Event(){}
	Event(int _station, int _count) : station(_station), count(_count) {}
	int station;
	int count;
	bool operator<(const Event &b) const { return station!=b.station ? station<b.station : count>b.count; }
};

LL cost(int a, int b, int n)
{
	b -= a;
	return b*LL(n+(n-b+1))/2;
}

int main()
{
	int t; scanf("%d",&t);
	FOR(_,1,t)
	{
		int n,m; scanf("%d%d",&n,&m);
		std::vector<Event> E;
		LL T = 0;
		REP(i,m)
		{
			int a,b,c; scanf("%d%d%d",&a,&b,&c);
			E.push_back(Event(a,c));
			E.push_back(Event(b,-c));
			T = (T+cost(a,b,n)%M*c)%M;
		}
		std::sort(E.begin(),E.end());
		Event S[m_max]; int ss=0;
		LL T2 = 0;
		REP(i,E.size())
		{
			if(E[i].count>0) S[ss++] = E[i];
			else while(E[i].count)
			{
				int v = std::min(-E[i].count,S[ss-1].count);
				//printf("v = %d\n",v);
				E[i].count += v;
				S[ss-1].count -= v;
				T2 = (T2+cost(S[ss-1].station,E[i].station,n)%M*v)%M;
				//printf("T2 = %d\n",(int)T2);
				if(!S[ss-1].count) ss--;
			}
		}
		printf("Case #%d: %d\n",_,(int)((T-T2+M)%M));
	}

	return 0;
}

