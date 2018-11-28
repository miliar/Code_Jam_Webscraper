#include <bits/stdc++.h>
using namespace std;

#define s(n)            scanf("%d",&n)
#define sl(n)           scanf("%lld",&n)
#define sf(n)           scanf("%lf",&n)
#define ss(n)           scanf("%s",n)
#define pls(x)          cout << x << " "
#define pln(x)          cout << x << "\n"
#define pis(x)          printf("%d ", x)
#define pin(x)          printf("%d\n", x)
#define pnl             printf("\n")
#define dbn             cout << "\n"
#define dbg(x)          cout << #x << " : " << x << " "
#define dbs(x)          cout << x << " "
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define rep(i,n)        FOR(i,0,n-1)
#define foreach(c,v)    for(__typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp              make_pair
#define FF              first
#define SS              second
#define pb              push_back
#define fill(a,v)       memset(a,v,sizeof(a))
#define all(x)          x.begin(),x.end()
#define sz(v)           ((int)(v.size()))
#define INF             (int)1e9
#define LINF            (long long)1e18
#define EPS             1e-9

typedef long long int lli;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

const int MAXN = 110;
const int MOD  =  (int)(1e9 + 7);

/*Main code begins now */
bool visit[MAXN][MAXN];
int m,n;
int cnT;
bool flag;
char G[MAXN][MAXN];
int dX[] = {0,0,-1,+1};
int dY[] = {-1,1,0,0};
bool valid(int x,int y)
{
	return x>=0 and y>=0 and x<m and y<n;
}
inline pii getNext(int x,int y,char dir){
	if(dir == '.') return mp(x,y);
	if(dir == '>') return mp(x,y+1);
	else if(dir == '<') return mp(x,y-1);
	else if(dir == '^') return mp(x-1,y);
	else if(dir == 'v') return mp(x+1,y);
}
bool go(int x,int y,char dir){
	int dx,dy;
	if(dir == '^') dx = -1,dy = 0;
	else if(dir == 'v') dx = 1,dy = 0;
	else if(dir == '>') dx = 0,dy = 1;
	else if(dir == '<') dx = 0,dy = -1;
	x+=dx,y+=dy;
	while(valid(x,y)){
		if(G[x][y]!='.') return true;
		x = x +dx,y = y+dy;
	}
	return false;
}
int main(){
	int t;
	s(t);
	string line;
	rep(q,t){
		cnT = 0;
		printf("Case #%d: ",q+1);
		s(m),s(n);
		rep(i,m){
			cin>>line;
			rep(j,n){
				G[i][j] = line[j];
			}
		}
		fill(visit,0);
		flag = true;
		rep(i,m){
			rep(j,n) {
				bool ok = false;
				if(G[i][j] == '.') continue;
				if(G[i][j] == '^'){
					if(!go(i,j,G[i][j])){
						if(go(i,j,'<') or go(i,j,'v') or go(i,j,'>')) ok = true;
					}else continue;
				}else if(G[i][j] == 'v'){
					if(!go(i,j,G[i][j])){
						if(go(i,j,'<') or go(i,j,'^') or go(i,j,'>')) ok = true;
					}else continue;
				}else if(G[i][j] == '<'){
					if(!go(i,j,G[i][j])){
						if(go(i,j,'^') or go(i,j,'v') or go(i,j,'>')) ok = true;
					}else continue;
				}else if(G[i][j] == '>'){
					if(!go(i,j,G[i][j])){
						if(go(i,j,'<') or go(i,j,'v') or go(i,j,'^')) ok = true;
					}else continue;
				}
				if(ok) cnT++;
				else {
					flag = false;
					break;
				}
			}
		}
		int ans = cnT;
		if(flag == false){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",ans);
		}
		flag = true;
		rep(i,m) rep(j,n) G[i][j] = '.';
	}
	return 0;
}