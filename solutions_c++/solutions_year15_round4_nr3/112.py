#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

class MaxFlow { public:
	int n,s,t;
	struct Edge {
		int end,next,cap;
		Edge(int e, int ca, int ne) : end(e), next(ne), cap(ca) {}
	};
	vector<int> first, prev;
	vector<bool> mark;
	vector<Edge> a;
	MaxFlow(int nn, int ss, int tt): n(nn), s(ss), t(tt) { first.assign(n,-1); }
	void add(int v, int u, int cap, int revcap=0) {
		a.pb(Edge(u,cap,first[v])); first[v] = SZ(a)-1;
		a.pb(Edge(v,revcap,first[u])); first[u] = SZ(a)-1;
	}
	bool findPath(int s, int t) {
		queue<int> q;
		mark.assign(n,false); mark[s]=true; q.push(s); prev.assign(n,-1);
		while (!q.empty()) {
			int v = q.front(); q.pop();
			for (int e = first[v]; e!=-1; e=a[e].next)
				if (a[e].cap && !mark[a[e].end]) { // add here e->cap>mnc for scaling!
					mark[a[e].end] = true;
					prev[a[e].end] = e;
					q.push(a[e].end);
				} }
		return mark[t];	}
	void augment(int s, int t, int &res, int cap=1000) {
		for (int v=t; v!=s; v=a[prev[v]^1].end) cap = min(cap, a[prev[v]].cap);
		res += cap;
		for (int v=t; v!=s; v=a[prev[v]^1].end) a[prev[v]].cap-=cap, a[prev[v]^1].cap+=cap;
	}
	int build() {
		int res=0;
/* scaling version: for (int mxc = 1<<30; mxc; mxc>>=1) // adjust for problem!!!  */
			while (findPath(s,t)) augment(s,t,res);
		return res; }
	VI mincut() // build should be called before!
	{	VI res;
		REP(i,n) if (mark[i]) for (int e=first[i]; e!=-1; e=a[e].next)
			if (!mark[a[e].end] && (e&1)==0) res.pb(e);
		return res; }
};

char buf[1024000];

int k;
//int p[N],r[N];
//int idrep[N],idk;

//int getset(int v) {	return p[v]==v ? v : (p[v]=getset(p[v])); }
//void mergeset(int v, int u) { if (r[v]<r[u]) p[v]=u; else {p[u]=v; r[v]+=r[u]==r[v]; } }

int main(int argc, char **argv)
{
	string FN = "C-large";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	gets(buf);
	sscanf(buf,"%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		gets(buf);
		int n;
		sscanf(buf,"%d",&n);
		map<string,int> dict;
		k=2;
		//REP(i,k) p[i]=i,r[i]=0;
		VVI w;
		REP(setn,n)
		{
			gets(buf);
			string bb(buf);
			istringstream stre(bb);
			string ww;
			w.push_back(VI());
			while (stre>>ww) {
				if (!dict.count(ww))
				{
					dict[ww] = k;
					k+=2;
				}
				w.back().push_back(dict[ww]);
			}
		}
		if (false) {
			k+=2000;
			REP(i,200)
			{
				w.push_back(VI());
				REP(j,10)
					w.back().push_back(rand()%(k/2-1)*2+2);
			}
		}

		fprintf(stderr,"? %d\n",k);
		MaxFlow mf(k,0,1);
		REP(setn,SZ(w))
		{
			const VI& ww = w[setn];
			if (setn==0)
			{
				REP(j,SZ(ww))
					mf.add(0,ww[j],1);
			}
			else if (setn==1)
			{
				REP(j,SZ(ww))
					mf.add(ww[j]+1,1,1);
			}
			else
				REP(j1,SZ(ww)) REP(j2,SZ(ww)) if (j1!=j2 && ww[j1] != ww[j2])
					mf.add(ww[j1]+1,ww[j2],1);
		}
		for (int i = 2; i < k; i+=2)
		{
			mf.add(i,i+1,1);
		}
		int res = mf.build();
		printf("%d\n",res);
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}