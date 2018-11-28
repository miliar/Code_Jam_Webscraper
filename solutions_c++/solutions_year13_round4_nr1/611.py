//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI 3.1415926535897932384626433832795
#define eps 1e-9
#define MOD 1000002013
using namespace std;

typedef struct
{
	int s,e,p;
} data;

bool cf(data a, data b)
{
	if (a.e != b.e)
		return a.e < b.e;
	return a.s < b.s;
}

int main()
{
	int t;
	scanf("%d",&t);
	FORN(i,t)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		vector<data> dat;
		FORN(j,m)
		{
			int x,y,z;
			scanf("%d%d%d",&x,&y,&z);
			data tmp;
			tmp.s = x;
			tmp.e = y;
			tmp.p = z;
			dat.pb(tmp);
		}
		bool udah = false;
		LL ans = 0;
		while (!udah)
		{
			udah = true;
			sort(dat.begin(),dat.end(),cf);
			vector<data> tmp;
			FORN(j,dat.sz())
				FORD(k,dat.sz()-1,j+1)
					if ((dat[j].p > 0) && (dat[j].e != dat[k].e))
					{
						if ((dat[k].p > 0) && (dat[k].s <= dat[j].e) && (dat[j].s < dat[k].s))
						{
							// cout << dat[j].s << " " << dat[j].e << " " << dat[j].p << endl;
							// cout << dat[k].s << " " << dat[k].e << " " << dat[k].p << endl;
							int tot = min(dat[j].p,dat[k].p);
							LL tmp2 = ((LL)(dat[k].s-dat[j].s)*(LL)(dat[k].e-dat[j].e))%MOD;
							ans += ((LL)tot*tmp2)%MOD;
							ans %= MOD;
							dat[j].p -= tot;
							dat[k].p -= tot;
							data tmp3;
							tmp3.s = dat[j].s;
							tmp3.e = dat[k].e;
							tmp3.p = tot;
							tmp.pb(tmp3);
							tmp3.s = dat[k].s;
							tmp3.e = dat[j].e;
							tmp3.p = tot;
							tmp.pb(tmp3);
							udah = false;
						}
						else
							continue;
					}
					else
						break;
			FORN(j,dat.sz())
				if (dat[j].p > 0)
					tmp.pb(dat[j]);
			dat.clear();
			dat = tmp;
		}
		printf("Case #%d: %lld\n",i+1,ans);
	}
}
