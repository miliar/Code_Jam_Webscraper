#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cout << "Case #" << (test + 1) << ": ";
    int n, a;
    cin >> n;
    vector<int> vals;
    FOR (i, n) {
      cin >> a;
      vals.pb(a);
    }
    int ret = 1 << 20;
    ffor (m, 1, 1001) {
      int cnt = m;
      FOR (i, vals.sz)
        cnt += (vals[i] + m - 1) / m - 1;
      ret = min(ret, cnt);
    }
    cout << ret;
    cout << "\n";
  }
  return 0;
}
