#include <cstdio>
#include <cstring>
#include <algorithm>
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn1(i,n) for(int i = 1; i <= n; i++)
#define forall(it, vec) for(typeof(vec.begin()) it = vec.begin(); it != vec.end(); it++)
#define ON(mask,i) (mask | (1L << (i)))
#define OFF(mask,i) (mask &  (-1 ^ (1L<<(i))) )
#define TOGGLE(mask,i) (mask ^ (1L << (i)))
#define isON(mask, i) (mask & (1L<<(i)))
#define mp make_pair
#define INF 100000000
using namespace std;
typedef pair<int, int> pii;

char str[128][128];
int memo[101][101][101][101];
int solve(int a, int b, int s1, int s2){
	
	int res  = INF;
	if(str[s1][a] != str[s2][b]) return INF;
	if(memo[a][b][s1][s2] != -1) return memo[a][b][s1][s2];
	if(!str[s1][a]) return 0;
	res = min(res, solve(a+1,b,s1,s2) + 1);
	res = min(res, solve(a,b+1,s1,s2) + 1);
	res = min(res, solve(a+1,b+1,s1,s2));
	return memo[a][b][s1][s2] = res;
}

int main(){
	int T,N;
	scanf("%d",&T);
	forn1(t,T){
		memset(memo,-1,sizeof(memo));
		scanf("%d",&N);
		forn(i,N) scanf("%s", str[i]);
		int res =  solve(0,0,0,1);
		if(res == INF) printf("Case #%d: Fegla Won\n",t);
		else printf("Case #%d: %d\n",t, res);		
	}
	return 0;
}
