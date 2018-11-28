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

vector<int> v[205];
char s[100005];
char str[100005];
map<string,int> mp;
int tot = 0;
int eng[100005],fre[100005];

void solve(int i){
	string now = "";
	for(int j = 0;s[j];j++){
		if(s[j]==' '){
			if(now!=""){
				if(mp.find(now)==mp.end()){
					mp[now] = tot++;
				}
				v[i].PB(mp[now]);
			}
			now = "";
		}else now+=s[j];
	}
	if(now!=" "){
		if(mp.find(now)==mp.end()){
			mp[now] = tot++;
		}
		v[i].PB(mp[now]);
	}
}

int ans;

void dfs(int u,int ret){
	if(u<0){
		ans = min(ans,ret);
		return;
	}
	int sz = v[u].size();
	int tmp = ret;
	FOR(i,sz){
		int id = v[u][i];
		eng[id]++;
		if(eng[id]==1&&fre[id]) tmp++;
	}
	dfs(u-1,tmp);
	FOR(i,sz) eng[v[u][i]]--;
	tmp = ret;
	FOR(i,sz){
		int id = v[u][i];
		fre[id]++;
		if(eng[id]&&fre[id]==1) tmp++;
	}
	dfs(u-1,tmp);
	FOR(i,sz) fre[v[u][i]]--;
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		mp.clear();
		tot = 0;
		int n;
		scanf("%d",&n);
		n-=2;
		gets(s);
		FOR(i,n+10) v[i].clear();
		gets(s);
		solve(n);
		gets(s);
		solve(n+1);
		FOR(i,n){
			gets(s);
			solve(i);
		}
		memset(eng,0,sizeof(eng));
		memset(fre,0,sizeof(fre));
		int sz = v[n].size();
		FOR(i,sz) eng[v[n][i]]++;
		sz = v[n+1].size();
		FOR(i,sz) fre[v[n+1][i]]++;
		int res = 0;
		FOR(i,tot) if(eng[i]&&fre[i]) res++;
		ans = INF;
		dfs(n-1,res);
		static int ca = 1;
		printf("Case #%d: %d\n",ca++,ans);
	}
	return 0;
}

