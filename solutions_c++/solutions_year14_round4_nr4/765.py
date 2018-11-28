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

int M, N;
string S[1011];
int sev[1011];

pll ans;

int cnt(vector<string>& v) {
    set<string> st;
    for(int i=0; i<v.size(); i++) {
        for(int c=0; c<=v[i].size(); c++) {
            st.insert(v[i].substr(0, c));
        }
    }
    return (int)st.size();
}

void calc() {
    vector<string> v;
    int ret = 0;
    REP(i,N) {
        v.clear();
        REP(j,M) {
            if(sev[j] == i) v.push_back(S[j]);
        }

        if(v.empty()) return;
        ret += cnt(v);
    }

    if(ans.first < ret) {
        ans = pll(ret, 1);
    }
    else if(ans.first == ret) {
        ans.second++;
    }
}

void dfs(int d) {
    if(d == M) {
        calc();
        return;
    }

    for(int i=0; i<N; i++) {
        sev[d] = i;
        dfs(d+1);
    }
}

void solve() {
    ans = pll(0, 0);
    dfs(0);
    printf("%lld %lld\n", ans.first, ans.second);
}

void coding() {
    int T;
    cin>>T;
    REPP(t,1,T) {
        cin>>M>>N;
        REP(i,M) cin>>S[i];
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST

int main() {
#ifdef _LOCAL_TEST
	clock_t startTime = clock();
	//freopen("d.in",  "r", stdin);
	freopen("D-small-attempt3.in",  "r", stdin);
    freopen("D-small.out", "w", stdout);
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
