#include "cstdio"
#include "iostream"
#include "vector"
#include "algorithm"
#include "cstring"
#include "set"
#include "map"
#include "queue"
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
inline int getint(){
  char c = getchar();
  for(;c<'0'||c>'9';) c = getchar();
  int x = 0;
  for(;c>='0' && c<='9'; c = getchar()) x*=10, x+=c-'0';
  return x;
}
const int maxn = 2000;
int n, m, k;
struct node{
	int x[2], y[2];
}a[maxn];
int dis[maxn][maxn];
int d[maxn];

int get(int a, int b, int c, int d){
	if(a>c) swap(a,c), swap(b,d);
	return max(0, c-b-1);
}
int Q[maxn*30], l, r, inq[maxn];
int main(int argc, char const *argv[])
{
	int cass;cin>>cass;
	repp(cas, 1, cass){
		n = getint(), m = getint(), k = getint();
		rep(i, k){
			rep(j, 2)
			a[i].x[j] = getint(), a[i].y[j] = getint();
		}
		a[k].x[0] = -1, a[k].y[0] = 0, a[k].x[1] = -1, a[k].y[1] = m;k++;
		a[k].x[0] = n, a[k].y[0] = 0, a[k].x[1] = n, a[k].y[1] = m;k++;
		rep(i, k)rep(j, k) if(i!=j){
			dis[i][j] = max(get(a[i].x[0], a[i].x[1], a[j].x[0], a[j].x[1]), get(a[i].y[0], a[i].y[1], a[j].y[0], a[j].y[1]));
			//printf("%d %d %d\n", i,j,dis[i][j]);
		}
		rep(i, k) d[i] = 1000000000;
		d[k-1] = 0;
		l = 0, r = 1; Q[0] = k-1;
		memset(inq, 0, sizeof(inq));
		while(l<r){
			int u = Q[l++];
			rep(i, k) if(d[i] > d[u] + dis[u][i]){
				d[i] = d[u] + dis[u][i];
				if(!inq[i]) {
					Q[r++] = i;
					inq[i] = 1;
				}
			}
			inq[u] = 0;
		}
		printf("Case #%d: %d\n", cas, d[k-2]);
	}
	return 0;
}