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

const int N = 2001;
int x[N], y[N];
int cx[N], cy[N];
bool juz[N];
int a[N];
int n;

bool exists(int xx) {
	if (xx == n+1) return true;
	//printf("bede szukal dla: %d\n", xx);
		set<PII> inc, dec;
		REP(i, n) if (juz[i]) dec.insert(mp(-y[i], i));
		REP(i, n) {
			if (!juz[i]) {
				//printf("   potencjalnie na pozycji: %d\n", i);
				int incShouldbe;
				if (inc.empty()) incShouldbe = 1;
				else incShouldbe = (-(inc.begin()->ST)) + 1;
				int decShouldbe;
				if (dec.empty()) decShouldbe = 1;
				else decShouldbe = (-(dec.begin()->ST)) + 1;
				//printf("   incs: %d, decs: %d\n", incShouldbe, decShouldbe);
				if (x[i] == incShouldbe && y[i] == decShouldbe) {
					juz[i] = true;
					a[i] = xx;
					if (exists(xx+1)) return true;
					juz[i] = false;
				}
			} else {
				inc.insert(mp(-x[i], i));
				dec.erase(dec.find(mp(-y[i], i)));
			}
		}
		return false;
}

void solve() {
	scanf("%d", &n);
	REP(i, n)
		scanf("%d", &x[i]);
	REP(i, n)
		scanf("%d", &y[i]);
	REP(i,n) juz[i] = false;
	REP(i, n) if (x[i] == 1 && y[i] == 1) {
		juz[i] = true;
		a[i] = 1;
		cx[i] = cy[i] = 1;
		//printf(" znalazlem 1 na poz: %d\n", i);
		break;
	}
	exists(2);
	REP(i, n) printf("%d ", a[i]);
	printf("\n");
}

int main(){
	int t;
	scanf("%d", &t);
	REP(i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
}