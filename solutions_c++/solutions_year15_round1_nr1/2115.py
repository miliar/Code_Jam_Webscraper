//
//  main.cpp
//  a
//
//  Created by Iago Almeida Neves on 4/17/15.
//  Copyright (c) 2015 Iago Almeida Neves. All rights reserved.
//

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define EPS 1e-9
#define _ ios_base::sync_with_stdio(false); cin.tie(NULL);
#define REP(i,n) for (int i = 0; i < n; i++)
#define REPI(i,n) for (int i = 1; i <= n; i++)
#define REPN(i,n) for (int i = n-1; i >= 0; i--)

#define MAXN 1010
int v[MAXN];

int main(int argc, const char * argv[]) { _
  int nt;
  cin >> nt;
  REPI(t, nt) {
    int n;
    cin >> n;
    REP(i, n) {
      cin >> v[i];
    }
    int maxx = -INF;
    int ans1 = 0;
    REP(i, n-1) {
      int a = v[i] - v[i+1];
      maxx = max(maxx, a);
      if (a > 0) {
        ans1 += a;
      }
    }
    int ans2 = 0;
    REP(i, n-1) {
      ans2 += min(maxx, v[i]);
    }
    cout << "Case #" << t << ": " << ans1 << " " << ans2 << "\n";
  }
  return 0;
}
