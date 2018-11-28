#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

typedef long long lol;

const lol MOD = 1000002013;

lol N;
int M;

struct TEvent {
	lol t; // origin
	lol d; // difference (+ are arrivals, - are leavers)
	TEvent(lol _t, lol _d) : t(_t), d(_d) {}
};
bool operator < (TEvent x, TEvent y)
{
  return (x.t < y.t) || (x.t == y.t && x.d > y.d);
}
vector<TEvent> events;

struct TTicket {
	lol o; // origin
	lol c; // count
	TTicket(lol _o, lol _c) : o(_o), c(_c) {}
};
bool operator < (TTicket x, TTicket y)
{
  return x.o < y.o;
}
priority_queue<TTicket> heap;

lol priceForStations(lol stations) {
	return (N * stations - stations * (stations - 1) / 2) % MOD;	
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		// init
		events.clear();
		while (!heap.empty()) { printf("BUG\n"); heap.pop(); }

		// input and fair price
		scanf("%lld %d", &N, &M);
		lol fairPrice = 0;
		for (int i = 0; i < M; ++i) {
			lol o, e, p;
			scanf("%lld %lld %lld", &o, &e, &p);
			events.push_back( TEvent(o, +p) );
			events.push_back( TEvent(e, -p) );

			fairPrice = (fairPrice + p * priceForStations(e - o)) % MOD;
		}
		sort(events.begin(), events.end());

		//for (int i = 0; i < M * 2; ++i) printf("%lld %lld \n", events[i].t, events[i].d);
		
		// calculate unfair price
		lol unfairPrice = 0;
		for (int i = 0; i < M * 2; ++i)
			if (events[i].d > 0) // arrival
			{
				// add tickets to pool
				heap.push( TTicket(events[i].t, events[i].d) );
			}
			else // departure
			{
				// get enough tickets from pool
				lol p = -events[i].d;
				while (p > 0) {
					TTicket ticket = heap.top();
					heap.pop();
					lol use = min(p, ticket.c);
					lol stations = events[i].t - ticket.o;
					unfairPrice = (unfairPrice + use * priceForStations(stations)) % MOD;

					ticket.c -= use;
					if (ticket.c > 0)
						heap.push(ticket);
					p -= use;
				}
			}

		printf("Case #%d: %lld\n", Ti, (MOD + fairPrice - unfairPrice) % MOD);
	}
	return 0;
}