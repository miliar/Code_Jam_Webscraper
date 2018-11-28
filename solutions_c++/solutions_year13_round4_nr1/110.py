#include<algorithm>
#include<cassert>
#include<cctype>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<complex>
using namespace std;

typedef long long LL;
typedef long double LD;

#define dprintf(...) fprintf(stderr, __VA_ARGS__)
// #define dprintf(...)

int cond = 1;
#define DB(X) {if(cond){cerr<<"Line:"<<__LINE__<<", "<<#X<<" = "<<X<<endl;}}
#define MAXT 1005

struct card{
	LL origin;
	LL count;
	card(LL org, LL cnt):origin(org),count(cnt){};
	card(){};
	bool operator<(const card & b) const {
		return origin < b.origin;
	};
};

struct event{
	int t;
	int type;
	int count;
	bool operator<(const event & a) const{
		return (t < a.t) || (a.t == t &&  type < a.type);
	};
};
#define START 1
#define END 2

event ev[MAXT];

priority_queue<card> cards;
LL dc;
LL ddc;
LL acost;

LL cost;

int n,m;

#define M 1000002013

LL sum(LL start, LL step, LL cnt){
	LL x = (2*start - (step)*(cnt-1))*cnt/2;
	return x%M;
}

void update_cost(int steps){
	acost = (acost + sum(dc, ddc, steps)) % M;
	dc -= ddc*steps;
};

int main2(int cn){
	while(!cards.empty()) cards.pop();
	cost = 0;
	acost = 0;
	scanf("%d %d", &n, &m);
	for(int i=0; i<m; ++i){
		int o, e, p;
		scanf("%d %d %d", &o, &e, &p);
		ev[2*i].t=o;
		ev[2*i].count = ev[2*i+1].count = p;
		ev[2*i+1].t = e;
		ev[2*i].type = START;
		ev[2*i+1].type = END;
		cost = (cost + (LL)p*sum(n, 1, e-o))%M;
	};
	sort(ev, ev+2*m);

	dc = 0; ddc = 0;
	for(int i=0; i<2*m; ++i){
		int t= ev[i].t;
		if(i>0 && ev[i].t > ev[i-1].t){
			update_cost(ev[i].t - ev[i-1].t);
		};
		if(ev[i].type == START){
			dc += n*ev[i].count;
			ddc += ev[i].count;
			cards.push(card(ev[i].t, ev[i].count));
		}
		else
		{	
			LL cnt=ev[i].count;
			card crd;
			while(cnt>0){
				crd = cards.top();
				cards.pop();
				LL q = min(crd.count, cnt);
				cnt -= q;
				crd.count -= q;
				dc -= (n - (t - crd.origin))*q;
			}
			if(crd.count > 0) cards.push(crd);
			ddc-=ev[i].count;
		}
	};
	printf("Case #%d: %lld\n", cn, (cost - acost + M)%M);
	return 0;
};

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; ++i) main2(i+1);
	return 0;
}

