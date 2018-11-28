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
const int dx[] = {-1,0,1,0}, dy[] = {0,-1,0,1}; //<^>v

int a[MX];

int main(){
	int ts;
	scanf("%d",&ts);
	rrep(ti,ts){
		int n, l = 0, r = 0;
		scanf("%d",&n);
		rep(i,n) scanf("%d",&a[i]);
		int ans = 0;
		rep(i,n){
			P s = P(INF,0);
			rep(j,n) if(a[j] != -1) s = min(s,P(a[j],j));
			int y = s.se;
			int now = 0;
			if(y-l < n-r-y-1){
				now = y-l;
				rep(j,now){
					swap(a[y],a[y-1]);
					--y;
				}
				l++;
				a[y] = -1;
			} else {
				now = n-r-1-y;
				rep(j,now){
					swap(a[y],a[y+1]);
					++y;
				}
				r++;
				a[y] = -1;
			}
			ans += now;
		}
		printf("Case #%d: %d\n",ti,ans);
	}
	
	return 0;
}





