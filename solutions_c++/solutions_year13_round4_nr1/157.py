#include <cstdio>
#include <algorithm>
#include <queue>
#include <utility>
#define mp make_pair
#define st first
#define nd second
#define FOREACH(i,c) for(__typeof(c.end()) i = c.begin();i!=c.end();++i)

using namespace std;
typedef pair<int,int> PII;
typedef pair<int, pair<int, int> > event;
priority_queue<PII> Q;
vector<event> E;
const long long mod = 1000002013;
long long normalResult;
int N,M;

void read()
{
	E.clear();
	normalResult = 0;
	while(!Q.empty()) Q.pop();
	scanf("%d%d", &N, &M);
	for(int i = 0;i<M;i++)
	{
		int o,e,p;
		scanf("%d%d%d", &o, &e, &p);
		long long tmp = (long long)(e-o)*(long long)N - (long long)(e-o)*(long long)(e-o-1)/2ll;
		tmp %= mod;
		tmp *= p;
		tmp %= mod;
		normalResult += tmp;
		normalResult %= mod;
		E.push_back(mp(o, mp(0,p)));
		E.push_back(mp(e, mp(1,p)));
	}
	sort(E.begin(), E.end());
}
void sweep(int tc)
{
	long long newResult = 0;
	FOREACH(i, E)
	{
		if(i->nd.st == 0)
			Q.push(mp(i->st, i->nd.nd));
		else
		{
			long long out = i->nd.nd;
			while(out > 0)
			{
				PII t = Q.top();
				Q.pop();
				long long used;
				if(t.nd > out)
				{
					used = out;
					Q.push(mp(t.st, t.nd-out));
				}
				else
					used = t.nd;
				out -= used;
				long long tmp = (long long)(i->st-t.st)*(long long)N - (long long)(i->st-t.st)*(long long)(i->st-t.st-1)/2ll;
				tmp %= mod;
				tmp *= used;
				tmp %= mod;
				newResult += tmp;
				newResult %= mod;
			}
		}
	}
	printf("Case #%d: %lld\n",tc,(((normalResult-newResult)%mod) + mod) % mod);
}
int main()
{
	int Z;
	scanf("%d", &Z);
	for(int i = 1;i<=Z;i++)
	{
		read();
		sweep(i);
	}
	return 0;
}

