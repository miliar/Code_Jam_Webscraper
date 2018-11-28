//	Problem X

const bool debug=false;

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <functional>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <utility>
#include <cassert>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <deque>
#include <queue>
#include <stack>

#define TIMES(n) for (int i=0; i<(n); ++i)
#define REPE(i,s,t) for (int (i)=(s); (i)<=(t); ++(i))
#define RESET(a) memset((a), 0, sizeof((a)))
#define P(x, ...) printf((x), ##__VA_ARGS__)
#define D(x, ...) if (debug) printf((x), ##__VA_ARGS__)
#define MP(x, y) make_pair((x), (y))

const int INF = 0x3F3F3F3F; // or (unsigned)(-1)>>1
int caseI = 0, caseD = -1;

using namespace std;

//void P(char *f, ...) {va_list v; va_start(v, f); vprintf(f, v); va_end(v);}
//void D(char *f, ...) {if (!debug) return; va_list v; va_start(v, f); vprintf(f, v); va_end(v);}


/*

Sample Input:



Sample Output:


*/

typedef pair<int, int> ii;
typedef vector<vector<ii> > graph;

typedef long long int ll;

const ll maxN = (ll)1e14+5;
int maxM = sqrt(maxN) + 2;

set<ll> ans;

class Qs {
	ll a, b;
	//int e[maxN][maxN];
	//int e_n[maxN];

public:
	Qs() {
		
	}

	bool input() {

		if (scanf("%lld%lld", &a, &b) != 2)
			return false;
		
		

		return true;
	}

	void solve() {

		int count = 0;

		count = distance(ans.lower_bound(a), ans.upper_bound(b));

		P("Case #%d: %d\n", caseI, count);
	}
};

bool isPalindrome(ll n) {
	char s[50];
	sprintf(s, "%lld", n);
	int len = strlen(s);
	for (int i=0; i<len; ++i)
		if (s[i] != s[len-1-i])
			return false;
	return true;
}

void build_ans_set() {
	TIMES(maxM) {
		ll sqr_i = i*i;
		if (isPalindrome(i) && isPalindrome(sqr_i)) {
			ans.insert(sqr_i);
			D(">> %lld\n", sqr_i);
		}
	}
	D(">> build finish lo~!\n");
}

void pre_process() {
	// freopen("qC-sample.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	scanf("%d", &caseD);

	build_ans_set();
}

int main() {
	Qs *p = new Qs;
	pre_process();
	while ((++caseI|1) && caseD-- && p->input()) {
		p->solve();
		delete p;
		p = new Qs;
	}
	delete p;
	return 0;
}
