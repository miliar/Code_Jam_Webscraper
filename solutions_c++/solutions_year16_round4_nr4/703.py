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
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

bool possible(int N, int pat) {
    vector<int> it(N);
    int M = (1 << N) - 1;
    rep(i,N) it[i] = i;
    // printf("N=%d, pat: %x\n", N, pat);
    do {
        // cout << "it:" << it << endl;
        queue<int> q;
        q.push(0);
        rep(i, N) {
            vector<int> v;
            while (!q.empty()) {
                v.pb(q.front()); q.pop();
            }
            // cout << v << endl;
            int wh = it[i];
            int mp = (pat >> (N*wh)) & M; // whさんの扱えるマシン
            rep(j, v.size()) {
                bool ok = false;
                int qi = v[j];
                for (int j=0,m=1; j<N; ++j,m<<=1) {
                    if (m & mp) {
                        if (!(m & qi)) {
//                            printf("%d san use %x|%x\n", wh, m,mp);
                            q.push(qi | m);
                            ok = true;
                        }
                    }
                }
                if (!ok) return false;
            }
        }
        if (q.empty()) return false;

    } while (next_permutation(all(it)));
    return true;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
      int N; cin >> N; // 1-4
      int NN = N * N; // 1-16
      int M = 1 << NN;
      vector<string> S(N);
      int L = 0;
      rep(i,N) {
          cin >> S[i];
          rep(j,N) {
              int of = i*N + j;
              if (S[i][j] == '1')
                L |= (1 << of);
          }
      }
//      printf("N=%d, L=%x\n", N, L);

      int pc_min = N*N;
      rep(p, M) {
          if (p & L) continue;
          // bool bad=false;
          int lp = L | p;
          if (possible(N, lp)) {
             int pc = __builtin_popcount(p);
//             printf("possible: %x | %x; || %d\n", L, p, pc);
             pc_min = min(pc_min, pc);
          }
      }

 answer:
    cout << "Case #" << (1+_t) << ": " << pc_min << endl;
  }
}
