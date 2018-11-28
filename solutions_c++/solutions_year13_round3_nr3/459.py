#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

//#define DEBUG
#ifdef DEBUG
//#include "cout.h"
#endif

main(){
  int _T; cin>>_T;
  rep(_t,_T){
    int N; cin>>N; // # of tribes. 1-10 1-1000
    // vector<int> d(N), n(N), w(N), e(N), s(N), dd(N), dp(N), ds(N);

    priority_queue<vector<int> > pq;
    // set<pair<int, pair<int,int> > > walls; // w, e, h
    // (day, w, e, strength)
    int wmin = INT_MAX, emax = INT_MIN;
    int dmin = INT_MAX, dmax = 0;
    rep(i,N) {
      int d,n,w,e,s,Dd,Dp,Ds; cin>>d>>n>>w>>e>>s>>Dd>>Dp>>Ds;
      // cin >> d[i] >> n[i] >> w[i] >> e[i] >> s[i] >> dd[i] >> dp[i] >> ds[i];
      vector<int> v(4);
      rep(j,n) {
        int day = (d + Dd*j);
        dmin = min(dmin, day); dmax = max(dmax, day);
        v[0] = -(day*2); // <= 676060
        v[1] = w + Dp*j;
        v[2] = e + Dp*j;
        v[3] = s + Ds*j; // >= 1

        wmin = min(wmin, v[1]);
        emax = max(emax, v[2]);
        // cout << i << " " << v << endl;
        pq.push(v);
      }
    }
    for (int day=dmin; day<=dmax; ++day) {
      vector<int> v(4, -1);
      v[0] = -(day*2 + 1);
      pq.push(v);
    }

#ifdef DEBUG
    // cout << wmin << " " << emax << endl;
#endif

    vector<int> wh(emax - wmin + 1, 0);
    vector<int> ch(emax - wmin + 1, 0);

    int ans = 0;
    while (!pq.empty()) {
      vector<int> v = pq.top(); pq.pop();
      int d = -v[0], w = v[1], e = v[2], s = v[3];
#ifdef DEBUG
      printf("attack [%d-%d] w/%d\n", w,e,s);
#endif
      if (d & 1) {
        for (int x=0; x<emax-wmin+1; ++x) {
          if (ch[x] > 0) { wh[x] = max(wh[x], ch[x]); }
        }
        ch.assign(emax - wmin + 1, 0);
      } else {
        bool fails = false;
        for (int x=w; x<e; ++x) {
          if (wh[x-wmin] < s) { fails = true; ch[x-wmin] = max(ch[x-wmin],s); }
        }
        if (fails) ++ans;
      }
    }

    printf("Case #%d: %d\n", 1+_t, ans);
  }
}
