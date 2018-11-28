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

vector<long long> m;

long long count(long long t) {
  if (t < 0)
    return 0;
  long long ret = m.sz;
  FOR (i, m.sz)
    ret += t / m[i];
  return ret;
}

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int b, n;
    cin >> b >> n;
    m.clear();
    FOR (i, b) {
      int t;
      cin >> t;
      m.pb(t);
    }
    
    long long s = 0, e = 1000000000000001LL, mid;
    long long best = -1;
    while (s <= e) {
      mid = (s + e) >> 1;
      long long cnt = count(mid);
      if (cnt < n)
        s = mid + 1;
      else {
        e = mid - 1;
        best = mid;
      }
    }
    
    if (best < 0)
      cout << "Something is wrong!!!" << endl;
    int ret = -1;
    long long cc = count(best - 1);
    FOR (i, m.sz)
      if (best % m[i] == 0) {
        cc++;
        if (cc == n) {
          ret = i + 1;
          break;
        }
      }

    if (ret == -1)
      cout << "Something else is wrong!!! " << best << endl;
    
    cout << "Case #" << (test + 1) << ": ";
    cout << ret;
    cout << "\n";
  }
  return 0;
}
