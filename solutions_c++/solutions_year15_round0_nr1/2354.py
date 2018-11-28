#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int main() {
  int T;
  cin >> T;
  REP(cas,T) {
    int N; cin >> N;
    vector<int> v;
    string str; cin >> str;
    REP(i,N+1) {
      REP(j,str[i]-'0') v.push_back(i);
    }
    int res = 0;
    REP(i,v.size()) res = max(res, v[i] - i);
    printf("Case #%d: %d\n", cas+1, res);
  }
  return 0;
}
