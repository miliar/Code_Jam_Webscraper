#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 1005
#define MODLL 1000002013LL
#define MOD 1000002013

using namespace std;

struct node
{
	int st, cnt;
};

int main ()
{
	int T, iT;
	scanf("%d",&T);
	static struct node a[MAXN];
	int ac;
	static pair <int, pair <char, int> > ev[MAXN];
	int evc;
	for (iT = 0; iT < T; iT++)
	{
		int st, N;
		scanf("%d %d",&st,&N);
		int i;
		evc = 0;
		int res2 = 0;
		for (i = 0; i < N; i++)
		{
			int o, e, p;
			scanf("%d %d %d",&o,&e,&p);
			int trav = e-o;
			res2 = (int)((long long)(res2) + (long long)(p) * ((((long long)(st) * (long long)(st-1) - (long long)(st-trav) * (long long)(st-trav-1)) / 2LL) % MODLL) % MODLL);
			ev[evc] = make_pair(o, make_pair('i', p));
			evc++;
			ev[evc] = make_pair(e, make_pair('o', p));
			evc++;
		}
		sort(ev,ev+evc);
		ac = 0;
		int res = 0;
		for (i = 0; i < evc; i++)
		{
			if (ev[i].second.first == 'i')
			{
				a[ac].st = ev[i].first;
				a[ac].cnt = ev[i].second.second;
				ac++;
			}
			else
			{
				int cnt = ev[i].second.second;
				int cur = ev[i].first;
				while (cnt)
				{
					int trav = cur - a[ac-1].st;
					if (a[ac-1].cnt > cnt)
					{
						res = (int)((long long)(res) + (long long)(cnt) * ((((long long)(st) * (long long)(st-1) - (long long)(st-trav) * (long long)(st-trav-1)) / 2LL) % MODLL) % MODLL);
						a[ac-1].cnt -= cnt;
						cnt = 0;
					}
					else
					{
						res = (int)((long long)(res) + (long long)(a[ac-1].cnt) * ((((long long)(st) * (long long)(st-1) - (long long)(st-trav) * (long long)(st-trav-1)) / 2LL) % MODLL) % MODLL);
						cnt -= a[ac-1].cnt;
						ac--;
					}
				}
			}
		}
		printf("Case #%d: %d\n",iT+1,(res2-res+MOD) % MOD);
	}
	return 0;
}