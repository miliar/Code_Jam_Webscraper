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
const int N=5, INF=1e9;
const LD EPS=1e-7;
int T;

int n;
char able[N][N];
vector<PII> zlist;
bool f;

int lst[N];
int visit[N];
int V;

bool gdfs(int i){
	if(i == n) return true;
	bool w = false;
	FOR(j, n){
		if(visit[j] != V && able[lst[i]][j] == '1'){
			w = true;
			visit[j] = V;
			bool res = gdfs(i+1);
			if(!res) return false;
			visit[j] = V-1;
		}
	}
	return w;
}

bool go(){
	V ++;
	return gdfs(0);
}

bool test(){/*
	puts("--");
	FOR(i, n){
		printf("%s\n",able[i]);
	}puts("");*/
	sort(lst, lst+n);
	do{
		bool res = go();	
		if(!res) {
			//FOR(i,n) printf("%d ",lst[i]); puts("");
			return res;
		}
	} while(next_permutation(lst, lst+n));
	return true;
}
void dfs(int i,int cn, int gl){
	if(cn > gl) return;
	if(f) return;
	if(cn == gl){
		f = f || test();
		return;
	} else if(i == (int)zlist.size()){
		return;
	} else{
		dfs(i+1, cn, gl);
		int x = zlist[i].X;
		int y = zlist[i].Y;
		able[x][y] = '1';
		dfs(i+1, cn+1, gl);
		able[x][y] = '0';
	}
}


int main(){
	int t = 0;
	scanf("%d",&T);
	while(t++ < T){
		f = false;
		zlist.clear();
		memset(visit,0,sizeof(visit));
		V = 0;
		RI(n);
		FOR(i, n) lst[i] = i;
		FOR(i, n){
			scanf("%s",able[i]);
			FOR(j, n){
				if(able[i][j] == '0'){
					zlist.pb(mpr(i,j));	
				}
			}
		}
		printf("Case #%d: ",t);	
		for(int tt = 0; tt <= (int)zlist.size(); tt++){
			dfs(0,0,tt);
			if(f){
				//puts("yo!!");
				printf("%d\n",tt);
				break;
			} else{
				//puts("GG");
			}
		}	
	}
}
