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

inline void solve(int test_number) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int cnt3 = s[SZ(s) - 1] == '+' ? 0 : 1;
		int ans = 0, ans1 = 0;
		int cnt = 0, cnt2 = s[SZ(s) - 1] == '+' ? 1 : 0;
		for (int j = SZ(s) - 1; j >= 0; j--) if (s[j] == '-') {
			if (cnt3 == 0 && ans != 0) ans1++;
			cnt++, cnt2 = 0, cnt3++;
		}
		else {
			if (cnt2 == 0) ans++; 
			cnt = 0;
			cnt2++;
			cnt3 = 0;
		}
		//cout << ans << endl;
		if (cnt != 0) ans++;
		if (cnt2 != 0 && ans != 0) ans1++;
		//cout << ans << ' ' << ans1<< endl;
		printf("Case #%d: %d\n", i, max(0, ans) + (ans == 0 ? 0 : ans1));
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
