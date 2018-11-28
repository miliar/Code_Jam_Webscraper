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

char grid[111][111];
int R, C;

	//		v,>,^,<
int dr[] = {1,0,-1,0};
int dc[] = {0,1,0,-1};

bool inside(int r, int c){
	return (0 <= r && r < R && 0 <= c && c < C);
}

bool check(int r, int c, int d){
	r+=dr[d]; c+=dc[d];
	while(inside(r,c)){
		if(grid[r][c]!='.') return false;	
		r+=dr[d];c+=dc[d];
	}
	return true;
}

int getD(int r, int c){
	char ch = grid[r][c];
	if (ch=='v')return 0;
	if (ch=='>')return 1;
	if (ch=='^')return 2;
	if (ch=='<')return 3;
}

int solve(){
	FOR(r,R)FOR(c,C)if(grid[r][c]!='.'){
		bool flag=true;
		FOR(d,4){
			flag = flag && check(r,c,d);
		}
		if(flag) return -1;
	}

	int ans=0;
	FOR(r,R)FOR(c,C)if(grid[r][c]!='.' && check(r,c,getD(r,c))) ++ans;
	return ans;
}

int main(){
	int T=INT;
	REP(t,1,T){
		R=INT;
		C=INT;
			
		FOR(r,R)scanf("%s",grid[r]);
		
		printf("Case #%d: ", t);
		int ans=solve();
		if (ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}	
	return 0;
}
