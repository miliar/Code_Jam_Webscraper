#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

typedef double dbl;
typedef float flt;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

#define eps 1e-9
#define inf 1000000000
#define infll 1000000000000000000LL
#define abs(x) ((x)<0?-(x):(x))
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define sz(x) ((int)(x).size())
#define intclz(x) __builtin_clz(x)
#define intctz(x) __builtin_ctz(x)
#define intln(x) (32-intclz(x))
#define intbc(x) __builtin_popcount(x)
#define llclz(x) __builtin_clzll(x)
#define llctz(x) __builtin_ctzll(x)
#define llln(x) (64-llclz(x))
#define llbc(x) __builtin_popcountll(x)
#define atbit(x,i) (((x)>>(i))&1)
#define tof(x) __typeof(x)
#define FORab(i,a,b) for (int i=(a); i<=(b); ++i)
#define RFORab(i,a,b) for (int i=(a); i>=(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define allstl(i,x,t) for (t::iterator i = (x).begin(); i!=(x).end(); ++i)
#define rallstl(i,x,t) for (t::reverse_iterator i = (x).rbegin(); i!=(x).rend(); ++i)
#define begend(x) (x).begin(),(x).end()
#define ms(a,v) memset(a,v,sizeof(a))
#define msn(a,v,n) memset(a,v,n*sizeof(a[0]))
#define mcp(d,s,n) memcpy(d,s,n*sizeof(s[0]))
#define clamp(x,a,b) min(max(x,a),b)

int k, n;
int keys[205];
vector<pair<int,vi> > chests;
int open;
vi O;

bool dp[1<<20];
bool dfs() {
	if (sz(O)==n) return true;
	if (dp[open]) return false;
	int oz = (~open) & ((1<<n)-1);
	while (oz) {
		int i = intctz(oz);
		oz ^= 1<<i;
		if (open & (1<<i)) continue;
		int needkey = chests[i].px;
		if (!keys[needkey]) continue;
		open |= 1<<i;
		--keys[needkey];
		FOR(j,sz(chests[i].py)) {
			++keys[chests[i].py[j]];
		}
		O.pb(i);

		if (dfs()) return true;

		O.pop_back();
		FOR(j,sz(chests[i].py)) {
			--keys[chests[i].py[j]];
		}
		++keys[needkey];
		open ^= 1<<i;
	}
	dp[open] = true;
	return false;
}

int main() {
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T;
    cin>>T;
    FOR1(cas,T) {
		cout<<"Case #"<<cas<<":";
		cin>>k>>n;
		ms(dp, false);
		ms(keys, 0);
		chests.assign(n, pair<int,vi>());
		open = 0;
		O.clear();
		FOR(i,k) {
			int key;
			cin>>key;
			++keys[key];
		}
		FOR(i,n) {
			cin>>chests[i].px;
			int ki;
			cin>>ki;
			chests[i].py.resize(ki);
			FOR(j,ki) {
				cin>>chests[i].py[j];
			}
		}
		bool ok = dfs();
		if (ok) {
			FOR(i,n) cout<<' '<<O[i]+1;
			cout<<endl;
		} else {
			cout<<" IMPOSSIBLE"<<endl;
		}
	}
    return 0;
}
