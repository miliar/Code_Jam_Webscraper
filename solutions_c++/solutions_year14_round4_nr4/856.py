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
const int INF = 0x3fffffff;
const LL LINF = INF * 1ll * INF;
const double PI = acos(-1.0);

#define lson l,mid,rt<<1
#define rson mid+1,r,rt<<1|1
#define lowbit(u) (u&(-u))

using namespace std;

class Trie{
public:
	int cnt;
	struct Node{
		Node *ch[26];
		void init(){
			memset(ch,0,sizeof(ch));
		}
	} nd[1005],*root;
	Trie(){
		cnt = 0;
		root = newNode();
	}

	Node *newNode(){
		nd[cnt].init();
		return &nd[cnt++];
	}
	void insert(char *s){
		Node *x = root;
		for(int i = 0;s[i];i++){
			int pos = s[i]-'A';
			if(x->ch[pos]==NULL) x->ch[pos] = newNode();
			x = x->ch[pos];
		}
	}
};

int mx,num;
int m,n;
char s[15][15];

void dfs(int now,int st,int tot){
	if(now==n&&st==(1<<m)-1){
		if(tot>mx){
			mx = tot;
			num = 1;
		}else if(tot==mx){
			num++;
		}
		return;
	}else if(now==n){
		return;
	}
	int all = (1<<m)-1;
	all^=st;
//	dfs(now+1,st,tot+1);
	for(int i = all;i;i = all&(i-1)){
		Trie trie;
		for(int j = 0;j<m;j++){
			if(i&(1<<j)){
				trie.insert(s[j]);
			}
		}
		dfs(now+1,st|i,tot+trie.cnt);
	}
}

int main(void){
#ifndef ONLINE_JUDGE
	freopen("/Users/mac/Desktop/D.in","r",stdin);
	freopen("/Users/mac/Desktop/D.out","w",stdout);
#endif
	int t;
	scanf("%d",&t);
	while(t--){
		scanf("%d %d",&m,&n);
		for(int i = 0;i<m;i++) scanf("%s",s[i]);
		mx = -INF,num = 1;
		dfs(0,0,0);
		static int ca = 1;
		printf("Case #%d: %d %d\n",ca++,mx,num);
	}
	return 0;
}

