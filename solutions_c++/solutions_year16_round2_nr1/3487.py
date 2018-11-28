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

int cnt[26];
char s[2005];
const char* NUM[] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
bool flag;
int use[10];

void dfs(int cur){
	if(flag) return;
	bool all = true;
	for(int i = 0;i<26;i++){
		if(cnt[i]>0) all = false;
	}
	if(all){
		flag = true;
		for(int i = 0;i<10;i++)
			for(int j = 0;j<use[i];j++) printf("%d",i);
		puts("");
		return;
	}
	if(cur==10) return;
	for(int i = 0;i<1000;i++){
		bool ok = true;
		for(int j = 0;NUM[cur][j];j++) if(cnt[NUM[cur][j]-'A']<i) ok = false;
		if(!ok) break;
		for(int j = 0;NUM[cur][j];j++) cnt[NUM[cur][j]-'A']-=i;
		use[cur] = i;
		dfs(cur+1);
		for(int j = 0;NUM[cur][j];j++) cnt[NUM[cur][j]-'A']+=i;
	}
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/data.in","r",stdin);
	freopen("/Users/mac/Desktop/data.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		memset(cnt,0,sizeof(cnt));
		scanf("%s",s);
		for(int i = 0;i<s[i];i++) cnt[s[i]-'A']++;
		flag = false;
		static int ca = 1;
		printf("Case #%d: ",ca++);
		dfs(0);
	}
	return 0;
}

