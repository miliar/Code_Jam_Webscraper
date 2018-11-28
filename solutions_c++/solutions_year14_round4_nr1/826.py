#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <climits>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
using namespace std;

#define REP(i,n) for(int i=0; i<n; i++)
#define REPP(i,s,e) for(int i=s; i<=e; i++)
#define PB(a) push_back(a)
#define MP(i,s) make_pair(i,s)
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(), (a).end()
#define PRT(a) cerr << #a << " = " << (a) << endl
#define PRT2(a,b) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << endl
#define PRT3(a,b,c) cerr << (a) << ", " << (b) << ", " << (c) << endl

typedef long long lint;
typedef pair<lint,lint> pll;

int N,X;
int S[10011];

void solve() {
    sort(S, S+N);
    int lo = 0;
    int hi = N-1;
    int ans = 0;
    while(lo < hi) {
        if(S[lo] + S[hi] <= X) {
            ans++;
            lo++;
            hi--;
        } else {
            ans++;
            hi--;
        }
    }
    if(lo == hi) ans++;
    printf("%d\n", ans);
}

void coding() {
    int T;
    cin>>T;
    REPP(t,1,T) {
        cin>>N>>X;
        REP(i,N) cin>>S[i];
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST

int main() {
#ifdef _LOCAL_TEST
	clock_t startTime = clock();
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

	coding();

#ifdef _LOCAL_TEST
	clock_t elapsedTime = clock() - startTime;
	cerr << endl;
	cerr << (elapsedTime / 1000.0) << " sec elapsed." << endl;
	cerr << "This is local test" << endl;
	cerr << "Do not forget to comment out _LOCAL_TEST" << endl << endl;
#endif
}
