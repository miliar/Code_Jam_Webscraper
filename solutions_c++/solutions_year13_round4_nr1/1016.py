#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<sstream>
#include<string>
#include<string.h>
#include<deque>
#include<vector>
#include<stack>
#include<queue>
#include<math.h>
#include<map>
#include<set>

using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

double PI = acos(-1);
double EPS = 1e-7;
int INF = 1000000000;
int MAXINT = 2147483647;
LL INFLL = 1000000000000000000LL;
LL MAXLL = 9223372036854775807LL;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

#define SIZE(a) (int)a.size()
#define ALL(a) a.begin(),a.end()
#define RESET(a,b) memset(a,b,sizeof(a))
#define FOR(a,b,c) for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a,b,c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a,b) for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); (a)++)
#define MIN(a, b) (a) = min((a), (b))
#define MAX(a, b) (a) = max((a), (b))
#define PAUSE system("pause")

#define input(in) freopen(in,"r",stdin)
#define output(out) freopen(out,"w",stdout)

pii M[8] = {mp(0,1),mp(1,0),mp(-1,0),mp(0,-1),mp(-1,1),mp(-1,-1),mp(1,-1),mp(1,1)};

/*\   \
\   \*/

typedef LL F;
typedef LL C;
#define F_INF 1e+18
#define C_INF 1e+18
#define NUM 10000000

LL mod = 1000002013;
int V;

vector<F> cap;
vector<C> cost;
vector<int> to,prev;

C dist[NUM],pot[NUM];
int last[NUM],path[NUM];


struct mincostflow{
    mincostflow(int n){
        cap.clear();
        cost.clear();
        to.clear();
        prev.clear();
        V = n;
        FOR(a,1,V)
        {
            last[a] = -1;
            pot[a] = 0;
        }
    }

    void addedge(int x, int y, F w, C c){
        cap.pb(w); cost.pb(c);  to.pb(y); prev.pb(last[x]); last[x] = SIZE(cap)-1;
        cap.pb(0); cost.pb(-c); to.pb(x); prev.pb(last[y]); last[y] = SIZE(cap)-1;
    }

    pair<F,C> dijkstra(int s, int t){
        F ansf=0; 
        C ansc=0;
        FOR(a,1,V) dist[a] = C_INF;
        FOR(a,1,V) path[a] = -1;
        priority_queue <pair <C,int>, vector<pair <C,int> >,greater< pair <C,int> > > pq;
        dist[s] = 0; 
        path[s] = -1; 
        pq.push(mp(0,s));
        while(!pq.empty())
        {
            double d = pq.top().fi;
            int p = pq.top().se;
            pq.pop();
            if (dist[p] == d)
            {
                int e = last[p];
                while(e != -1)
                {
                    if (cap[e] > 0)
                    {
                        C nd = dist[p] + cost[e] + pot[p] - pot[to[e]];
                        if (nd < dist[to[e]])
                        {
                            dist[to[e]] = nd;
                            path[to[e]] = e;
                            pq.push(mp(nd,to[e]));
                        }
                    }
                    e = prev[e];
                }
            }
        }
        FOR(a,1,V) pot[a] += dist[a];
        if(path[t] != -1)
        {
            ansf = F_INF;
            int e = path[t];
            while(e != -1)
            {
                MIN(ansf,cap[e]);
                e = path[to[e^1]];
            }
            e = path[t];
            while(e != -1)
            {
                ansc += cost[e] * ansf;
                cap[e^1] += ansf;
                cap[e] -= ansf;
                e = path[to[e^1]];
            }
        }

        return mp(ansf,ansc);
    }

    pair <F,C> calc(int s, int t){
        F ansf=0;
        C ansc=0;
        while(1)
        {
            pair <F, C> p = dijkstra(s,t);
            if(path[t] == -1) break;
            ansf += p.fi; ansc += p.se;
            ansf %= mod;
            ansc %= mod;
        }
        return mp(ansf,ansc);
    }
};

LL o[5000];
LL e[5000];
LL p[5000];
LL n,m;

LL val(LL d)
{
	if (d == 0) return 0;
	LL p = (2LL*n+1LL-d);
	LL q = d;
	if (p%2LL==0) p/= 2LL;
	else q /= 2LL;
	//cout << d << " " << p*q << endl;
	return p*q;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	FOR(t,1,tc)
	{
		LL ans = 0;
		scanf("%lld%lld",&n,&m);
		FOR(a,1,m)
		{
			scanf("%lld%lld%lld",&o[a],&e[a],&p[a]);
			ans += (p[a]*(val(e[a]-o[a])))%mod;
			ans %= mod;
		}
		//cout << ans << endl;
		int ss = 2*m+1;
		int st = 2*m+2;
		mincostflow lol(st);
		FOR(a,1,m)
		{
			lol.addedge(ss,a,p[a],0);
		}
		FOR(a,1,m)
		{
			FOR(b,1,m)
			{
				if (o[a] <= e[b])
				{
					//cout << "EDGE " << a << " " << m+b << " " << e[b]-o[a] << " " << val(e[b]-o[a]) << endl; 
					lol.addedge(a,m+b,INFLL,val(e[b]-o[a]));
				}
			}
		}
		FOR(a,1,m)
		{
			lol.addedge(m+a,st,p[a],0);
		}
		LL res = ans-lol.calc(ss,st).se;
		if (res < 0) res += mod;
		printf("Case #%d: %lld\n",t,res);
	}
}
