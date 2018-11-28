//#pragma comment(linker,"/STACK:102400000,102400000")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <ctime>
#include <numeric>
#include <vector>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <complex>
#include <deque>
#include <functional>
#include <list>
#include <map>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int, int> PII;
typedef pair<PII, int> PIII;
typedef pair<LL, LL> PLL;
typedef pair<LL, int> PLI;
typedef pair<LD, LD> PDD;
#define MP make_pair
#define PB push_back
#define sz(x) ((int)(x).size())
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define FOR(i,n) for(int i=0;i<(n);++i)
#define forIt(mp,it) for(__typeof(mp.begin()) it = mp.begin();it!=mp.end();it++)
const double EPS = 1e-6;
const int INF = 0x3fffffff;
const LL LINF = INF * 1ll * INF;
const double PI = acos(-1.0);

#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
#define lowbit(u) (u&(-u))

using namespace std;

char g[105][105];
int node[100005];
int idx[105][105];
int in[100005],out[100005];
int row[105],col[105];
int n,m;

bool valid(int x,int y){
	return x>=0&&x<n&&y>=0&&y<m;
}

bool check(int x,int y){
	for(int i = 0;i<n;i++) if(i==x) continue;
	else if(g[i][y]!='.') return true;
	for(int j = 0;j<m;j++) if(j==y) continue;
	else if(g[x][j]!='.') return true;
	return false;
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&n,&m);
		FOR(i,n) scanf("%s",g[i]);
		memset(row,0,sizeof(row));
		memset(col,0,sizeof(col));
		int cnt = 0;
		FOR(i,n) FOR(j,m) if(g[i][j]!='.') idx[i][j] = cnt++;
		memset(in,0,sizeof(in));
		memset(out,0,sizeof(out));
		FOR(i,n){
			FOR(j,m){
				if(g[i][j]=='.') continue;
				int dx,dy;
				if(g[i][j]=='>'){
					dx = 0,dy = 1;
				}else if(g[i][j]=='<') dx = 0,dy = -1;
				else if(g[i][j]=='^') dx = -1,dy = 0;
				else dx = 1,dy = 0;
				int nx = i+dx,ny = j+dy;
				while(valid(nx,ny)){
					if(g[nx][ny]!='.'){
						out[idx[i][j]]++;
						in[idx[nx][ny]]++;
						break;
					}
					nx+=dx,ny+=dy;
				}
			}
		}
		int ans = 0;
		FOR(i,n){
			FOR(j,m){
				if(g[i][j]!='.'){
					if(out[idx[i][j]]==0){
						if(check(i,j)) ans++;
						else ans = -INF;
					}
				}
			}
		}
		static int ca = 1;
		printf("Case #%d: ",ca++);
		if(ans<0) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}

