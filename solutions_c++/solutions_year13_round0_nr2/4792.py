#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <list>
#include <ctime>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define mp(x,y) make_pair(x,y)
typedef short int sint;

const int N = 101;
int a[N][N];
int w[N], k[N];
int n, m;

bool solve() {
	scanf("%d %d", &n, &m);
	REP(i, n) {
		REP(j, m) {
			scanf("%d", &a[i][j]);
			w[i] = k[j] = a[i][j];
		}
	}
	REP(i, n) {
		REP(j, m) {
			w[i] = max(w[i], a[i][j]);
			k[j] = max(k[j], a[i][j]);
		}
	}
	REP(i, n) REP(j, m) {
		if (!(a[i][j] == w[i] || a[i][j] == k[j]))
			return false;
	}
	return true;
}

int main(){
	int t;
	scanf("%d", &t);
	REP(q, t) {
		printf("Case #%d: %s\n", q+1, solve() ? "YES" : "NO");
	}
}