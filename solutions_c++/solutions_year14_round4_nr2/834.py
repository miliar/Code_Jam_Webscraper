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

const lint INF = 1ll<<55;
int N;
lint A[1011];

lint calc(vector<lint> v, int thr) {
    lint ret = 0;
    for(int i=0; i<thr; i++) {
        for(int j=thr-1; j>=i+1; j--) {
            if(v[j] < v[j-1]) {
                swap(v[j], v[j-1]);
                ret++;
            }
        }
    }

    for(int i=thr; i<N-1; i++) {
        for(int j=N-2; j>=thr+1; j--) {
            if(v[j] > v[j-1]) {
                swap(v[j], v[j-1]);
                ret++;
            }
        }
    }
    return ret;
}

void solve() {
    vector<pll> v;

    int le = 0;
    int ri = N-1;
    lint ans = 0;
    REP(i,N) {
        v.clear();
        for(int j=le; j<=ri; j++) v.push_back(pll(A[j], j));
        sort(ALL(v));

        int p = v[0].second;
        if(abs(p-le) < abs(ri-p)) {
            for(int j=p; j>le; j--) {
                swap(A[j], A[j-1]);
                ans++;
            }
            le++;
        } else {
            for(int j=p; j<ri; j++) {
                swap(A[j], A[j+1]);
                ans++;
            }
            ri--;
        }
    }
    cout << ans << endl;
}

void coding() {
    int T;
    cin>>T;
    REPP(t,1,T) {
        cin>>N;
        REP(i,N) cin>>A[i];
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST

int main() {
#ifdef _LOCAL_TEST
	clock_t startTime = clock();
	//freopen("b.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
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
