//Grzegorz Prusak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <queue>
#include <functional>
#include <cassert>

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

template<typename T> void checkmin(T &a, T b){ if(a>b) a = b; }

typedef long long LL;

enum { n_max = 3000 };

bool G[n_max][n_max];

void set(int i, int j)
{
	G[i][j] = 1;
}

void build(int A[], int n, bool rev)
{
	std::vector<int> S[n_max];
	if(!rev)
	{
		REP(i,n)
		{
			if(A[i]>1) set(S[A[i]-2].back(),i);
			if(S[A[i]-1].size()) set(i,S[A[i]-1].back());
			S[A[i]-1].push_back(i);
		}
	}
	else
	{
		FORD(i,n-1,0)
		{
			if(A[i]>1) set(S[A[i]-2].back(),i);
			if(S[A[i]-1].size()) set(i,S[A[i]-1].back());
			S[A[i]-1].push_back(i);
		}
	}
	//REP(i,n){ REP(j,S[i].size()) printf("%d ",S[i][j]); puts(""); }
	//puts("-------------");
}

int deg[n_max];
std::vector<int> topo(int n)
{
	memset(deg,0,sizeof deg);
	REP(i,n) REP(j,n) if(G[i][j]) deg[j]++;
	
	std::priority_queue<int,std::vector<int>,std::greater<int> > Q;
	REP(i,n) if(!deg[i]) Q.push(i);
	std::vector<int> res;
	while(Q.size())
	{
		int v = Q.top(); Q.pop();
		REP(i,n) if(G[v][i] && !--deg[i]) Q.push(i);
		res.push_back(v);
	}
	return res;
}

void printG(int n)
{
	REP(i,n){ REP(j,n) printf("%d ",G[i][j]); puts(""); }
}

int A[n_max];
int B[n_max];

int main()
{
	int t; scanf("%d",&t);
	FOR(_,1,t)
	{
		memset(G,0,sizeof G);
		int n; scanf("%d",&n);
		int A[n_max];
		REP(i,n) scanf("%d",A+i);	
		REP(i,n) scanf("%d",B+i);
		build(A,n,0);
		//printG(n);
		build(B,n,1);
		//printG(n);
		std::vector<int> res = topo(n), r2(n);
		//assert(res.size()==n);
		REP(i,res.size()) r2[res[i]] = i+1;
		printf("Case #%d: ",_);
		REP(i,n) printf("%d ",r2[i]); puts("");
	}

	return 0;
}

