//Google Code Jam
//Round 2
//1 Jun 2013

//start of jonathanirvings' template v2.0.0 (BETA)

#define jonathan using
#define ganteng namespace
#define banget std
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <deque>
#include <string>
#include <string.h>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <time.h>
#include <bitset>
#include <list>
jonathan ganteng banget;

typedef long long LL;
typedef pair<int,int> pii;
typedef pair<pii,pii> ppi;
typedef pair<LL,LL> pll;
typedef pair<string,string> pss;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vii;
typedef vector<LL> vl;
typedef vector<vl> vvl;
typedef vector<string> vstr;
typedef vector<char> vc;

double EPS = 1e-9;
int INF = 2000000000;
long long INFF = 8000000000000000000LL;
double PI = acos(-1);
int dirx[8] = {-1,0,0,1,-1,-1,1,1};
int diry[8] = {0,1,-1,0,-1,1,-1,1};

#ifdef TESTING
	#define DEBUG fprintf(stderr,"====TESTING====\n")
	#define VALUE(x) cerr << "The value of " << #x << " is " << x << endl
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define DEBUG 
	#define VALUE(x)
	#define debug(...)
#endif

#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORN(a,b,c) for (int (a)=(b);(a)<=(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>=(c);--(a))
#define FORSQ(a,b,c) for (int (a)=(b);(a)*(a)<=(c);++(a))
#define FORL(a,b,c) for (LL (a)=(b);(a)<=(c);++(a))
#define FORLSQ(a,b,c) for (int (a)=(b);(LL)(a)*(LL)(a)<=(c);++(a))
#define FORC(a,b,c) for (char (a)=(b);(a)<=(c);++(a))
#define REP(i,n) FOR(i,0,n)
#define REPN(i,n) FORN(i,1,n)
#define REPD(i,n) FORD(i,n,1)
#define MAX(a,b) a = max(a,b)
#define MIN(a,b) a = min(a,b)
#define SQR(x) ((x) * (x))
#define RESET(a,b) memset(a,b,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define ALL(v) v.begin(),v.end()
#define ALLA(arr,sz) arr,arr+sz
#define SIZE(v) (int)v.size()
#define SORT(v) sort(ALL(v))
#define REVERSE(v) reverse(ALL(v))
#define SORTA(arr,sz) sort(ALLA(arr,sz))
#define REVERSEA(arr,sz) reverse(ALLA(arr,sz))
#define PERMUTE next_permutation
#define TC(t) while(t--)
#define READ(n,data) {scanf("%d",&n); REPN(i,n) scanf("%d",&data[i]);}

inline string IntToString(int a){
    char x[100];
    sprintf(x,"%d",a); string s = x;
    return s;
}

inline int StringToInt(string a){
    char x[100]; int res;
    strcpy(x,a.c_str()); sscanf(x,"%d",&res);
    return res;
}

inline string GetString(void){
	char x[1000005];
	scanf("%s",x); string s = x;
	return s;
}

inline string uppercase(string s){
	int n = SIZE(s); 
	REP(i,n) if (s[i] >= 'a' && s[i] <= 'z') s[i] = s[i] - 'a' + 'A';
	return s;
}

inline string lowercase(string s){
	int n = SIZE(s); 
	REP(i,n) if (s[i] >= 'A' && s[i] <= 'Z') s[i] = s[i] - 'A' + 'a';
	return s;
}

inline void OPEN (string s) {
    freopen ((s + ".in").c_str (), "r", stdin);
    freopen ((s + ".out").c_str (), "w", stdout);
}

//end of jonathanirvings' template v2.0.0 (BETA)

int T,ada[505][505],R,C,B,a,b,c,d;
int sudah[505][505];
int nomor[505][505];
int done;

class MaxFlow
{
	public:
	int n,start,end;
	map<int,int> cap[100005];
	vi adj[100005];
	void reset(int _n)
	{
		n = _n;
		start = 0;
		end = n - 1;
		REP(i,n) cap[i].clear();
		REP(i,n) adj[i].clear();
	}
	void addEdge(int a,int b,int c)
	{
		adj[a].pb(b);
		adj[b].pb(a);
		if (cap[a].count(b) > 0) cap[a][b] += c;
		else cap[a][b] = c;
	}
	int bisa(void)
	{
		queue<pii> q;
		int parent[n+5];
		bool sudah[n+5];
		RESET(parent,-1); RESET(sudah,0);
		q.push(mp(start,INF));
		parent[start] = -1;
		sudah[start] = 1;
		while (!q.empty())
		{
			pii now = q.front();
			q.pop();
			if (now.fi == end)
			{
				int ix = now.fi;
				while (ix != start)
				{
					cap[parent[ix]][ix] -= now.se;
					cap[ix][parent[ix]] += now.se;
					ix = parent[ix];
				}
				return now.se;
			}
			REP(i,SIZE(adj[now.fi])) 
			{
				int dest = adj[now.fi][i];
				if(cap[now.fi][dest] > 0)
				{
					int jalan = min(cap[now.fi][dest],now.se);
					if (!sudah[dest])
					{
						parent[dest] = now.fi;
						sudah[dest] = 1;
						q.push(mp(dest,jalan));
					}
				}
			}
		}
		return 0;
	}
	int countMaxFlow(void)
	{
		int res = 0;
		while (1)
		{
			int x = bisa();
			if (x == 0) break;
			res += x;
		}
		return res;
	}
};

MaxFlow M;

int main()
{
	scanf("%d",&T);
	REPN(cases,T)
	{
		fprintf(stderr,"%d\n",cases);
		printf("Case #%d: ",cases);
		scanf("%d %d %d",&C,&R,&B);
		RESET(ada,0);
		TC(B)
		{
			scanf("%d %d %d %d",&a,&b,&c,&d);
			FORN(i,a,c) FORN(j,b,d) ada[i][j] = 1;
		}
		//printf("%d\n",C*R*2+2);
		M.reset(C*R*2+2);
		//return 0;
		int now = 0;
		//printf("%d %d\n",now,C*R*2+2);
		REP(i,C) REP(j,R)
		{
			++now;
			nomor[i][j] = now;
			++now;
			if (ada[i][j] == 0) 
				M.addEdge(nomor[i][j],nomor[i][j]+1,1);
		}
		//printf("%d %d\n",now,C*R*2+2);
		REP(i,C) REP(j,R)
		{
			if (i > 0) M.addEdge(nomor[i][j]+1,nomor[i-1][j],100);
			if (i < C-1) M.addEdge(nomor[i][j]+1,nomor[i+1][j],100);
			if (j > 0) M.addEdge(nomor[i][j]+1,nomor[i][j-1],100);
			if (j < R-1) M.addEdge(nomor[i][j]+1,nomor[i][j+1],100);
		}
		REP(i,C)
		{
			if (ada[i][0] == 0) 
				M.addEdge(M.start,nomor[i][0],1);
			if (ada[i][R-1] == 0)
				M.addEdge(nomor[i][R-1]+1,M.end,1);
		}
		printf("%d\n",M.countMaxFlow());
	}
	return 0;
}










