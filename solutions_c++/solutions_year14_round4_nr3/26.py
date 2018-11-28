#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<string.h>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<map>
#include<set>
#include<iostream>
#include<sstream>
#include<sys/time.h>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; i++)
#define rrep(i,n) for(int i = 1; i <= n; i++)
#define drep(i,n) for(int i = n-1; i >= 0; i--)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL))
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;

const int MX = 1005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;

int d[MX][4];
int a[MX][MX];
int ad[2];

int s[MX][MX];

int main(){
	int ts;
	scanf("%d",&ts);
	rrep(ti,ts){
		int w, h, n;
		scanf("%d%d%d",&w,&h,&n);
		rep(i,n)rep(j,4) scanf("%d",&d[i][j]);
		priority_queue<P,vector<P>,greater<P>> q;
		vi dist(n,w);
		rep(i,n)rep(j,n){
			ad[0] = ad[1] = w;
			if(d[i][0] > d[j][2]){
				ad[0] = d[i][0] - d[j][2] - 1;
			} else if(d[j][0] > d[i][2]){
				ad[0] = d[j][0] - d[i][2] - 1;
			} else ad[0] = 0;
			if(d[i][1] > d[j][3]){
				ad[1] = d[i][1] - d[j][3] - 1;
			} else if(d[j][1] > d[i][3]){
				ad[1] = d[j][1] - d[i][3] - 1;
			} else ad[1] = 0;
			a[i][j] = max(ad[0],ad[1]);
		}
		rep(i,n){
			dist[i] = d[i][0];
			q.push(P(d[i][0],i));
		}
		while(!q.empty()){
			int v = q.top().se, ds = q.top().fi; q.pop();
			if(dist[v] != ds) continue;
			rep(i,n){
				int nd = ds+a[v][i];
				if(dist[i] > nd){
					dist[i] = nd;
					q.push(P(nd,i));
				}
			}
		}
		int ans = w;
		rep(i,n){
			ans = min(ans,dist[i]+(w-1-d[i][2]));
		}
		//rep(i,n){rep(j,n) printf("%d ",a[i][j]);puts("");}
		printf("Case #%d: %d\n",ti,ans);
		
		//rep(i,w)rep(j,h) s[i][j] = 0;
		//rep(i,n)for(int j = d[i][0]; j <= d[i][2]; ++j)
			//for(int k = d[i][1]; k <= d[i][3]; ++k) s[j][k] = 1;
		//if(ti==9){ rep(i,w){rep(j,h)printf("%c",s[i][j]?'#':'.');puts("");}}
	}
	
	return 0;
}





