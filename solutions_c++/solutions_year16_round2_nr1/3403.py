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


string a[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
bool mark[9999];

vector <int> ans;
vector <int> cur;

inline void solve(int test_number) {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		m0(mark);
		ans.clear();
		//int ttt = 0;
		int cntZ = 0, cntH = 0, cntR = 0, cntG= 0 , cntT = 0, cntE = 0, cntI = 0, cntX = 0, cntU = 0, cntW = 0, cntS = 0, cntO = 0, cntV = 0, cntF = 0, cntN = 0;
		for (int j = 0; j < SZ(s); j++) {
			if (s[j] == 'Z') cntZ++;
			if (s[j] == 'E') cntE++;
			if (s[j] == 'X') cntX++;
			if (s[j] == 'N') cntN++;
			if (s[j] == 'F') cntF++;
			if (s[j] == 'R') cntR++;
			if (s[j] == 'W') cntW++;
			if (s[j] == 'O') cntO++;
			if (s[j] == 'T') cntT++;
			if (s[j] == 'I') cntI++;
			if (s[j] == 'S') cntS++;
			if (s[j] == 'V') cntV++;
			if (s[j] == 'G') cntG++;
			if (s[j] == 'H') cntH++;
			if (s[j] == 'U') cntU++;
		}
		for (int j = 0; j < cntX; j++) ans.pb(6), cntS--, cntI--;
		for (int j = 0; j < cntG; j++) ans.pb(8), cntI--, cntE--, cntH--, cntT++;
		for (int j = 0; j < cntW; j++) ans.pb(2), cntT--, cntO--;
		for (int j = 0; j < cntZ; j++) ans.pb(0), cntE--, cntO--, cntR--;
		for (int j = 0; j < cntU; j++) ans.pb(4), cntF--, cntO--, cntR--;
		if (cntF >= 0) for (int j = 0; j < cntF; j++) ans.pb(5), cntI--, cntV--, cntE--;
		if (cntV >= 0) for (int j = 0; j < cntV; j++) ans.pb(7), cntE -= 2, cntS--, cntN--;
		if (cntR >= 0)for (int j = 0; j < cntR; j++) ans.pb(3), cntT--, cntE -= 2, cntH--;
		if (cntI >= 0) for (int j = 0; j < cntI; j++) ans.pb(9), cntN -= 2, cntE--;
		//cout << cntN << endl;
		if (cntN >= 0) for (int j = 0; j < cntN; j++) ans.pb(1);
		sort(ALL(ans));
		cout << "Case #" << i << ": ";
		for (int j = 0; j < SZ(ans); j++) cout << ans[j];
		cout << endl;
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
