#include<stdio.h>
#include<string.h>
#include<math.h>
#include<ctype.h>
#include<assert.h>
#include<stdlib.h>
#include<time.h>
#include<assert.h>

#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

//#define DEBUG_MODE

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

#ifdef DEBUG_MODE
#define DBG(X) X
#else
#define DBG(X)
#endif

inline int ___INT(){int ret; scanf("%d",&ret); return ret;}
#define INT ___INT()

typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> VI;

const int INF = 1000000000;
int N;
int A[1005];
int B[1005];
int dp[1005];

int F(int k){
	if(k == N-1)
		return 0;
	int& ret = dp[k];
	if(ret>-1)return ret;

	ret = INF;
	int cost = 0;

	// left
	for(int i = 0; i < N; ++i)
		if(A[i] == B[k]) break;
		else if(A[i] > B[k]) ++cost;

	ret = min(ret, cost + F(k+1));
	// right
	cost = 0;

	for(int i = N-1; i >= 0; --i)
		if(A[i] == B[k]) break;
		else if(A[i] > B[k]) ++cost;

	ret = min(ret, cost + F(k+1));

	return ret;
}

int main() {
	freopen("B_large.in", "r", stdin);
	freopen("B_large_out.txt","w",stdout);

	int T=INT;
	REP(t,1,T){
		N=INT;
		FOR(i,N) A[i]=INT;
		FOR(i,N) B[i]=A[i];
		sort(B,B+N);
		CLR(dp,-1);
		printf("Case #%d: %d\n",t,F(0));
	}	
	return 0;
}

