#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
#define LL long long

const LL mod = 1000002013;

const int MaxN = 10000;

struct event
{
	int x, t, p;
	inline event(int x=0,int t=0,int p=0):x(x),t(t),p(p){};
}stack[MaxN];
int top;

bool operator < (const event &a, const event& b)
{
	return a.x != b.x ? a.x < b.x : a.t > b.t;
}

int N, M;

LL CalcCost(LL s, LL t, LL p)
{
	
//	cerr << ">> Match < "<<s<<" , "<<t<<" > p = "<<p<<" : cost = ";
	
	LL l = t - s;
	LL ret = (N + N - l + 1ll) * l / 2;
	ret = ret % mod;
	ret = ret * p;
	ret %= mod;
//	cerr << ret << endl;
	return ret;
}

int run()
{
	scanf("%d %d", &N, &M);
	vector<event> E;
	
	LL expect = 0;
	
	for(int i=0;i<M;++i)
	{
		int s,t,p;
		scanf("%d %d %d", &s, &t, &p);
		expect = (expect + CalcCost(s,t,p)) % mod;
		E.push_back(event(s,1,p));
		E.push_back(event(t,-1,p));
	}
	
	sort(E.begin(), E.end());
	
	top = 0;
	
	LL res = 0;
	
	for(int i=0;i<E.size();++i)
	{
		event &e = E[i];
		if(e.t > 0)
		{
			stack[++ top] = e;
			continue;
		}
		while(e.p > 0)
		{
			LL det = min(e.p, stack[top].p);
			res = ( res + CalcCost(stack[top].x, e.x, det)) % mod;
			e.p -= det;
			if(!(stack[top].p -= det)) -- top;
		}
	}
	
	
	
	LL ret = (expect - res) % mod;
	if(ret < 0) ret += mod;
	
//	cerr << "expect = "<<expect<<"  res = "<<res<<endl;
	
	return ret;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int test;
	scanf("%d", &test);
	for(int no=1;no<=test;++no)
		printf("Case #%d: %d\n", no, run());
}
