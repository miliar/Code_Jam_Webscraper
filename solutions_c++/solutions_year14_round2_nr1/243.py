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
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests) {
    int n;
    cin >> n;
    vector<string> strs;
    FOR (i, n) {
      string s;
      cin >> s;
      strs.pb(s);
    }
    
    vector<pair<char, int> > splits[n];
    FOR (i, n) {
      int idx = 0;
      splits[i].clear();
      string curr = strs[i];
      while (idx < curr.sz) {
        int j = idx;
        while (j < curr.sz && curr[idx] == curr[j])
          j++;
        splits[i].pb(make_pair(curr[idx], j - idx));
        idx = j;
      }
    }
    
    int cnt = splits[0].sz;
    bool lost = false;
    FOR (i, n)
      if (cnt != splits[i].sz)
        lost = true;
    
    if (!lost) {
      FOR (i, n)
        FOR (j, cnt)
          if (splits[0][j].first != splits[i][j].first)
            lost = true;      
    }
    
    int ret = 0;
    if (!lost) {
      FOR (j, cnt) {
        int m = 0;
        FOR (i, n)
          m >?= splits[i][j].second;
        int sum = 1 << 30;
        ffor (len, 1, m + 1) {
          int s = 0;
          FOR (i, n)
            s += abs(splits[i][j].second - len);
          sum <?= s;
        }
        ret += sum;
      }
    }
    cout << "Case #" << (test + 1) << ": ";
    if (lost)
      cout << "Fegla Won";
    else
      cout << ret;
    cout << "\n";
  }
  return 0;
}
