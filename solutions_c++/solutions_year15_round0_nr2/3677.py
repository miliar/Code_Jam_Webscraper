//
//  main.cpp
//  b
//
//  Created by Iago Almeida Neves on 4/11/15.
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
    int maxx = -INF;
    REP(i, n) {
      cin >> v[i];
      maxx = max(maxx, v[i]);
    }
    int ans = INF;
    REPI(i, maxx) {
      int time = i;
      REP(j, n) {
        time += (v[j]-i+(i-1))/i;
      }
      ans = min(ans, time);
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}