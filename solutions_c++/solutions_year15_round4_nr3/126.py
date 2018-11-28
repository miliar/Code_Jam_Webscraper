#include <cassert>
#include <cstring>

#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <iostream>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int inf = 1e9;
const int MID = 1e5;

namespace mf {
  struct Edge {
    int a, b, cap;
    int nx;
  };
 
  const int MAXV = 10000;
  const int MAXE = MAXV * 10 + 123;
 
  int ne = -1;
  Edge es[MAXE];
  int last_eidx[MAXV];
 
  void clear() { ne = 0; memset(last_eidx, -1, sizeof last_eidx); }
  void add_edge(int a, int b, int cap) {
    es[ne] = {a, b, cap, last_eidx[a]}; last_eidx[a] = ne; ++ne;
    es[ne] = {b, a, 0, last_eidx[b]}; last_eidx[b] = ne; ++ne; // pazi cap = 0
  }
 
  int solve(int source, int sink, int v) {
    assert(ne != -1);
    int ans = 0;
 
    while (true) {
      static int dad_eidx[MAXV]; REP(i, v) dad_eidx[i] = -1;
      static int acc[MAXV]; REP(i, v) acc[i] = 0;
      static queue<int> Q; while (!Q.empty()) Q.pop();
 
      for (Q.push(source), acc[source] = inf; !Q.empty(); Q.pop()) {
        int ex = Q.front();
 
        for (int eidx = last_eidx[ex]; eidx != -1; eidx = es[eidx].nx) {
          Edge& e = es[eidx];
          int val = min(acc[e.a], e.cap);
          if (val > 0 && acc[e.b] == 0) {
            acc[e.b] = val;
            dad_eidx[e.b] = eidx;
            Q.push(e.b);
          }
        }
      }
 
      if (acc[sink] == 0)  break;
      int f = acc[sink]; ans += f;
      // if (ans >= inf) ???
 
      for (int x = sink; x != source; ) {
        int eidx = dad_eidx[x];
        Edge& e = es[ eidx ];
        es[eidx].cap -= f;
        es[eidx^1].cap += f;
        x = e.a;
      }
    }
 
    return ans;
  }
 
}


int main(void) {
  int ntc; scanf("%d", &ntc);
  REP(tc, ntc) {
    int ns; scanf("%d ", &ns);
    vector<vector<string> > ss;
    vector<string> ws;

    REP(is, ns) {
      static char buff[123123]; fgets(buff, 123123, stdin);
      vector<string> row;
      istringstream in(buff);
      for (string x; in >> x; ) {
        row.push_back(x);
        ws.push_back(x);
      }
      ss.push_back(row);
    }

    sort(ws.begin(), ws.end());
    ws.resize(unique(ws.begin(), ws.end()) - ws.begin());

    vector<vector<int> > iss;
    REP(i, ns) {
      vector<int> row;
      for (string x : ss[i]) {
        row.push_back(lower_bound(ws.begin(), ws.end(), x) - ws.begin());
      }
      iss.push_back(row);
    }

    int ans = inf;
    mf::clear();

    int nw = (int)ws.size();
    int src = 2*nw, sink = src + 1;

    assert(nw < 9000);

    vector<int> A(nw, MID), B(nw, MID);
    for (int w : iss[0]) A[w] = inf;
    for (int w : iss[1]) B[w] = inf;

    REP(w, nw) {
      mf::add_edge(src, w, A[w]);
      mf::add_edge(w, nw+w, MID+1);
      mf::add_edge(nw+w, sink, B[w]);
    }
    
    REP(is, ns) {
      if (is >= 2) {
        int sz = iss[is].size();
        REP(ai, sz) REP(bi, sz) if (ai != bi) {
          int a = iss[is][ai];
          int b = iss[is][bi];
          mf::add_edge(nw+b, a, inf);
        }
      }
    }

    int ff = mf::solve(src, sink, sink+1);
    ans = ff - nw*MID;

    assert(ans < inf);
    printf("Case #%d: %d\n", tc+1, ans);
    fflush(stdout);
  }
  return 0;
}   
