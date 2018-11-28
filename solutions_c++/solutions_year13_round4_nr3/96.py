#include<functional>
#include<algorithm>
//#include<iostream>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
//#include<cmath>
#include<set>
#include<map>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b);i>=(e);--i)
#define FOReach(it,V) for(__typeof((V).begin()) it=(V).begin();it!=(V).end();++it)

#define PB push_back
#define ALL(V) (V).begin(),(V).end()
#define SIZE(V) ((int)(V).size())

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
	#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
	#define debug(...)
#endif

int stmp;
#define scanf stmp=scanf


const int MAX = 2000;
const int INF = 1000000001;

VI G[MAX];
int A[MAX], B[MAX];
int res[MAX];

int n;

void topsort() {
	priority_queue<int> Q;
	VI indeg(n, 0);
	REP(i,n)
		FOReach(u,G[i])
			++indeg[*u];
	REP(i,n)
		if(!indeg[i])
			Q.push(i);
	int k = n;
	while(!Q.empty())
	{
		int v = Q.top();
		Q.pop();
		res[v] = k--;
		FOReach(u,G[v])
		{
			--indeg[*u];
			if(!indeg[*u])
				Q.push(*u);
		}
	}
	assert(k == 0);
}

void solve() {
	REP(i,n)
	{
		int lastk = -1;
		REP(j,i)
			if(A[j] == A[i]) G[j].PB(i);
			else if(A[j]+1 == A[i]) lastk = j;
		assert(A[i] == 1 || lastk != -1);
		if(A[i] != 1)
			G[i].PB(lastk);
	}
	FORD(i,n-1,0)
	{
		int lastk = -1;
		FORD(j,n-1,i+1)
			if(B[j] == B[i]) G[j].PB(i);
			else if(B[j]+1 == B[i]) lastk = j;
		assert(B[i] == 1 || lastk != -1);
		if(B[i] != 1)
			G[i].PB(lastk);
	}
	topsort();
}

int main(int argc, char *argv[]) {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d", &n);
		REP(i,n) G[i].clear();
		REP(i,n) scanf("%d", A+i);
		REP(i,n) scanf("%d", B+i);
		solve();
		REP(i,n) printf("%d ", res[i]); printf("\n");
	}
	return 0;
}

