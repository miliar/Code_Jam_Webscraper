#include <bits/stdc++.h>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define lgll(x) (63-__builtin_clzll(x))
#define __count __builtin_popcount
#define __countll __builtin_popcountll
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
const int N=1e6, INF=1e9;
const LD EPS=1e-7;
int T;

int n, R, P, S;

int stop = 0;
int rc,pc,sc;
char s[N];

char lst[4] = "RPS";

void dfs(char now, int dep){
	if(dep == 0) {
		s[stop ++] = now;
		if(now == 'P') pc ++;
		else if(now == 'S') sc++ ;
		else if(now == 'R') rc++;
		return;
	} else{
		char loss = 0;
		if(now == 'P') {
			dfs(now, dep-1);
			loss = 'R';
			dfs(loss, dep-1);
		}
		else if(now == 'S'){
			loss = 'P';
			dfs(loss, dep-1);
			dfs(now, dep-1);
		}
		else if(now == 'R'){
			dfs(now, dep-1);
			loss = 'S';
			dfs(loss, dep-1);
		}
	}
	return;
}
string best_str[13][3];

void init(){
	FOR(i, 3){
		best_str[0][i] = lst[i];
	}
	FOR1(l, 12){
		FOR(i, 3){
			int loss = (i+2) %3;
			if(best_str[l-1][i] > best_str[l-1][loss]){
				best_str[l][i] = best_str[l-1][loss] + best_str[l-1][i];
			} else{
				best_str[l][i] = best_str[l-1][i]+best_str[l-1][loss] ;
			}
		}
	}
}


int main(){
	int t = 0;
	scanf("%d",&T);
	init();
	while(t++ < T){

		RI(n);
		RI(R); RI(P); RI(S);
		bool w = false;
		int idx = -1;
		FOR(i ,3){
			stop = 0;
			rc = pc = sc = stop = 0;
			dfs(lst[i], n);
			s[stop] = 0;
			if(rc == R && pc == P && sc == S){
				w = true;
				idx = i;
				break;
			}
		}
		printf("Case #%d: ",t);	
		if(w) printf("%s\n", best_str[n][idx].c_str());
		else puts("IMPOSSIBLE");
	}
}
