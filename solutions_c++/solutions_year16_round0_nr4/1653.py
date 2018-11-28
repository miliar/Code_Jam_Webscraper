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

char S[105][10005];
int vis[105];

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		int k,c,s;
		scanf("%d %d %d",&k,&c,&s);
		for(int i = 0;i<k;i++){
			for(int j = 0;j<k;j++){
				if(j==i){
					for(int l = 0;l<k;l++) S[i][j*k+l] = 'G';
				}else{
					for(int l = 0;l<k;l++) S[i][j*k+l] = 'L';
					S[i][j*k+i] = 'G';
				}
			}
			S[i][k*k] = '\0';
		}
		vector<int> ans;
		int left = k;
		memset(vis,0,sizeof(vis));
		while(left>0){
			int mx = 0;
			int pos = -1;
			for(int i = 0;i<k*k;i++){
				int cnt = 0;
				for(int j = 0;j<k;j++){
					if(vis[j]) continue;
					else if(S[j][i]=='G') cnt++;
				}
				if(cnt>mx){
					mx = cnt;
					pos = i;
				}
			}
			left-=mx;
			ans.PB(pos+1);
			for(int j = 0;j<k;j++) if(vis[j]) continue;
			else if(S[j][pos]=='G') vis[j] = 1;
		}
		static int ca = 1;
		printf("Case #%d:",ca++);
		if(c==1){
			if(s!=k) puts(" IMPOSSIBLE");
			else{
				for(int i = 0;i<k;i++) printf(" %d",i+1);
				puts("");
			}
			continue;
		}
		if(s<(int)ans.size()){
			puts(" IMPOSSIBLE");
			continue;
		}
		for(int i = 0;i<(int)ans.size();i++) printf(" %d",ans[i]);
		puts("");
	}
	return 0;
}

