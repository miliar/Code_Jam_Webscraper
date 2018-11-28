#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

///////////////// macros and typedefs ////////////////////
#define DEB(k) cerr << "debug: " #k << "=" << k << endl;
#define rep(i, n) for (int i = 0, _n = (n); i < _n; ++i)
#define repd(i, n) for (int i = (n)-1; i >= 0; --i)
#define _fill(MAP, x) memset((MAP), (x), sizeof((MAP)))
#define all(c) (c).begin(), (c).end()
#define mp(MAP, b) make_pair(MAP, b)
#define l(c) (int)((c).size())
#define sqr(MAP) ((MAP)*(MAP))
#define inf 0x7f7f7f7f
#define pb push_back
#define ppb pop_back
#define x first
#define y second
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> pi;

#define PROBLEM_NAME "A-large"

int N, M;
ll AA[2222];
vector< pair<pi, int> > v, v1;
ll CNT1 = 0, CNT2 = 0;
set<int> SET;
map<int,int> MAP;
vi tmp;

void solveCase(int tc) {
    scanf("%d %d", &N, &M);
    v.clear();
    v1.clear();
    CNT1 = CNT2 = 0;
    SET.clear();
    MAP.clear();
    tmp.clear();
    _fill(AA, 0);
    rep(i, M) {
        pair<pi, int> T;
        cin >> T.x.x >> T.x.y >> T.y;
        SET.insert(T.x.x);
        SET.insert(T.x.y);
        v.pb(T);
        ll cur = T.x.y - T.x.x;
        cur *= (N+N-cur+1);
        cur /= 2;
        cur %= 1000002013;
        cur *= T.y;
        cur %= 1000002013;
        CNT1 += cur;
    }
    CNT1 %= 1000002013;
    int cnt=1;
    for (set<int>::iterator i = SET.begin(); i != SET.end(); i++) {
        MAP[*i] = cnt++;
        tmp.pb(*i);
    }
    rep(i, M) {
        int l = MAP[v[i].x.x];
        int r = MAP[v[i].x.y];
        for (int j = l; j < r; j++)
            AA[j] += v[i].second;
    }
    int cur = 0;
    while (true) {
        while(cur<2005 && AA[cur]==0) cur++;
        if (cur > 2004) break;
        int cur1 = cur;
        ll Min=AA[cur];
        while (cur1 < 2005 && AA[cur1] != 0) {
            Min=min(Min, AA[cur1]);
            cur1++;
        }
        ll answer=tmp[cur1-1]-tmp[cur-1];
        answer *= (2*N-answer+1);
        answer /= 2;
        answer %= 1000002013;
        answer *= Min;
        answer %= 1000002013;
        CNT2 += answer;
        for (int i = cur; i < cur1; i++)
            AA[i] -= Min;
    }
    CNT2%=1000002013;
    int ret=(CNT1+1000002013-CNT2)%1000002013;
    cout << "Case #" << (tc+1) << ": " << ret << endl;
}

void solution()
{
    int tc;
    scanf("%d\n", &tc);
    rep(i, tc)
        solveCase(i);
}

int main()
{
#ifndef ONLINE_JUDGE
   freopen(PROBLEM_NAME".in", "rt", stdin);
   freopen(PROBLEM_NAME".out", "wt", stdout);
#endif
   solution();
#ifndef ONLINE_JUDGE
   //fprintf(stderr, "Time: %.2lf sec\n", (clock()*1./CLOCKS_PER_SEC));
#endif
   return 0;
}
