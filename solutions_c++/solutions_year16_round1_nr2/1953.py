#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <climits>
#include <cfloat>
#include <cmath>
#include <map>
#include <list>
#include <fstream>

using namespace std;
#ifdef BENCH
#define DBG 1

#if DBG
#define D(x) x;
#else
#define D(x)
#endif
#endif // BENCH

#define CLR(x) memset(x, 0, sizeof x);
#define CLRN(x, n) memset(x, 0, n*sizeof x[0]);
#define CLRVN(x, v, n) memset(x, v, n*sizeof x[0]);
#define REP(v,n) for(int v=0;v<n;v++)
#define FOR(v,a,b) for(int v=a;v<=b;v++)
#define every(iter, iterable) \
	typeof((iterable).begin()) iter = (iterable).begin(); iter != (iterable).end(); iter++

typedef int Num;
const int maxn=51;
const int maxm=2501;
int N;

Num data[2*maxn][maxn];
Num cnt[maxm];

void solve() {
    vector<Num> odds;
    FOR(i,1,2500) {
        if (cnt[i] & 1)
            odds.push_back(i);
    }
    sort(odds.begin(), odds.end());
    for (every(it, odds)) {
        cout << " " << *it;
    }
    cout<< endl;
}

int main() {
	// input
	string basename("B-large");
	string in(basename + ".in");
	string out(basename + ".out");
#if BENCH
	freopen(in.c_str(), "r", stdin);
	if (1) // write to file
		freopen(out.c_str(), "w", stdout);
#endif
	int TC, tc, i,j;
	cin >> TC;
	for (tc = 0; tc < TC; tc++) {
		cin >> N;
		CLR(cnt);
		for(i = 0; i < 2*N-1; i++)
		    for(j=0;j<N;j++) {
		        Num nn;
		        cin >> nn;
		        data[i][j] = nn;

		        cnt[nn]++;
		    }
		cout << "Case #" << (tc + 1) << ":";
		solve();
	}
	return 0;
}
