#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <memory.h>
#include <iomanip>
#include <bitset>
#include <cassert>
#include <stack>
#include <deque>
#include <cassert>
#include <list>
#include <cstdio>
#include <numeric>
#define EPS 1e-7
#define INF (int)(1e+9)
#define LINF (long long)(1e+18)
#define PI acos(-1)
#define mp make_pair
#define MOD 1000000007
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define buli(x) __builtin_popcountll(x)
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define N 999999


using namespace std;

#define NAME "test"
typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

void solve(int test_number);


void pre() {
    cout.setf(ios::fixed);
    cout.precision(20);
    cerr.setf(ios::fixed);
    cerr.precision(3);
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
}

void post() {
    fprintf(stderr, "\n");
    fprintf(stderr, "Execution time: %Lf", (ld) clock());
}

const int MAXN = 100100;


int cnt[999];

inline void solve(int test_number) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n;
		scanf("%d", &n);
		m0(cnt);
		int ans = n, cur = 2;
		if (n == 0 ) {
			printf("Case #%d: ", i);
			puts("INSOMNIA");
			continue;
		}
		while (true) {
			string s;
			SS str;
			str << ans << ' ';
			str >> s;
			for (int j = 0; j < SZ(s); j++) {
				cnt[s[j] - '0']++;
			}
			int flag = 1;
			for (int j = 0; j <= 9; j++) if (!cnt[j]) flag = false;
			if (flag) break;
			ans = n * cur;
			//cout << ans<< endl;
			//if (cur == 90) break;
			cur++;
		}
		printf("Case #%d: %d\n", i, ans);
	}
	return;

}



int main()
{
#ifdef DEBUG
    freopen(NAME ".in", "r", stdin);
    freopen(NAME ".out", "w", stdout);
#endif
    freopen(NAME ".in", "r", stdin);
    freopen(NAME ".out", "w", stdout);
    pre();

    int n = 1;
    for (int i = 0; i < n; i++) {
            solve(i + 1);
    }

    post();
    return 0;
}
