//
//  main.cpp
//  a
//
//  Created by Iago Almeida Neves on 5/10/15.
//  Copyright (c) 2015 Iago Almeida Neves. All rights reserved.
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define EPS 1e-9
#define _ ios_base::sync_with_stdio(false); cin.tie(NULL);
#define REP(i,n) for (auto i = 0; i < n; ++i)
#define REPI(i,n) for (auto i = 1; i <= n; ++i)
#define REPN(i,n) for (int i = n-1; i >= 0; --i)
#define ITER(it, g) for (auto it = g.begin(); it != g.end(); ++it)
#define ITERN(it, g) for (auto it = g.rbegin(); it != g.rend(); ++it)

#define MAXN 110

//KMP
int fail[MAXN];
int num;
void buildFail(string s) {
  int j = fail[0] = -1;
  REPI(i, s.size()) {
    while (j >= 0 && s[j] != s[i-1]) {
      j = fail[j];
    }
    fail[i] = ++j;
  }
}
void kmp(string s, string t) {
  num = 0;
  buildFail(s);
  int k = 0;
  REP(i, t.size()) {
    while (k >= 0 && s[k] != t[i]) {
      k = fail[k];
    }
    if (++k >= s.size()) {  // found in t[i-s.size()+1] to t[i]
      k = fail[k];
      num++;
      //      found[i] = 1;
    }
  }
}

int total;
int good;
int nn;
typedef struct probs {
  string c[MAXN];
  bool vis;
}
probs;

probs dp[MAXN][MAXN];
string alpha, target;

probs solve(int n, int let) {
  probs &ans = dp[n][let];
  if (ans.vis) {
    return ans;
  }
  if (n == 1) {
    REP(i, alpha.size()) {
      ans.c[i] = alpha[i];
    }
  }
  else {
    REP(i, alpha.size()) {
      probs a = solve(n-1, i);
      ans.c[i] += alpha[let] + a.c[i];
    }
  }
  ans.vis = true;
  return ans;
}

vector<string> v;


int main(int argc, const char * argv[]) { _
  int nt;
  cin >> nt;
  REPI(t, nt) {
    int bla1, bla2;
    cin >> bla1 >> bla2 >> nn;
    cin >> alpha >> target;
    total = good = 0;
    REP(i, MAXN) {
      REP(j, MAXN) {
        REP(k, MAXN) {
          dp[i][j].c[k] = "";
        }
        dp[i][j].vis = false;
      }
    }
    buildFail(target);
    string s;
    int good = 0;
    int maxx = 0;
    int total = 0;
    REP(i, alpha.size()) {
      s.push_back(alpha[i]);
      if (nn == 1) {
        kmp(target, s);
        total++;
        good += num;
        maxx = max(maxx, num);
      }
      REP(j, alpha.size()) {
        s.push_back(alpha[j]);
        if (nn == 2) {
          kmp(target, s);
          total++;
          good += num;
          maxx = max(maxx, num);
        }
        REP(k, alpha.size()) {
          s.push_back(alpha[k]);
          if (nn == 3) {
            kmp(target, s);
            total++;
            good += num;
            maxx = max(maxx, num);
          }
          REP(l, alpha.size()) {
            s.push_back(alpha[l]);
            if (nn == 4) {
              kmp(target, s);
              total++;
              good += num;
              maxx = max(maxx, num);
            }
            REP(m, alpha.size()) {
              s.push_back(alpha[m]);
              if (nn == 5) {
                kmp(target, s);
                total++;
                good += num;
                maxx = max(maxx, num);
              }
              REP(n, alpha.size()) {
                s.push_back(alpha[n]);
                if (nn == 6) {
                  kmp(target, s);
                  total++;
                  good += num;
                  maxx = max(maxx, num);
                }
                REP(o, alpha.size()) {
                  s.push_back(alpha[o]);
                  if (nn == 7) {
                    kmp(target, s);
                    total++;
                    good += num;
                    maxx = max(maxx, num);
                  }
//                  REP(p, alpha.size()) {
//                    s.push_back(alpha[o]);
//                    if (nn == 7) {
//                      kmp(target, s);
//                      total++;
//                      good += num;
//                      maxx = max(maxx, num);
//                    }
//                    s.pop_back();
//                  }
                  s.pop_back();
                }
                s.pop_back();
              }
              s.pop_back();
            }
            s.pop_back();
          }
          s.pop_back();
        }
        s.pop_back();
      }
      s.pop_back();
    }
//    int good = 0;
//    int maxx = 0;
//    int total = 0;
//    REP(i, alpha.size()) {
//      REP(j, alpha.size()) {
//        cout << dp[nn][i].c[j] << endl;
//        kmp(target, dp[nn][i].c[j]);
//        good += num;
//        total++;
//      }
//      cout << endl;
//    }
    printf("Case #%d: %.8lf\n", t, maxx - (good/(1.0*total)));
  }
  return 0;
}