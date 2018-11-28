#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
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
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests) {
    int n, x;
    cin >> n >> x;
    int S;
    int cnt[x + 1];
    SET(cnt, 0);
    set<int> has;
    FOR (i, n) {
      cin >> S;
      cnt[S]++;
      has.insert(-S);
    }
    
    int ret = 0;
    int val = x;
    while (val) {
      if (!cnt[val]) {
        val--;
        continue;
      }
      ret++;
      
      cnt[val]--;
      if (!cnt[val])
        has.erase(-val);
      
      int tmp = x - val;
      set<int>::iterator it = has.lower_bound(-tmp);
      if (it != has.end()) {
        tmp = -(*it);
        cnt[tmp]--;
        if (!cnt[tmp])
          has.erase(-tmp);
      }
    }

    cout << "Case #" << (test + 1) << ": ";
    cout << ret;
    cout << "\n";
  }
  return 0;
}
