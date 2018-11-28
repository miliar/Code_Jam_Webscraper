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
  freopen("Dl.out","wt", stdout);
  freopen("Dl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  int N;
  vector<double> Naomi, Ken;
  
  FOR (test, tests){
    cin >> N;
    Naomi.clear();
    Ken.clear();
    int ret1 = 0, ret2 = 0;
    FOR (i, N) {
      double a;
      cin >> a;
      Naomi.pb(a);
    }
    FOR (i, N) {
      double a;
      cin >> a;
      Ken.pb(a);
    }
    sort(all(Naomi));
    sort(all(Ken));
    
    bool used[N];
    SET(used, 0);
    FOR (i, N) {
      bool found = false;
      FOR (j, N)
        if (!used[j] && Ken[j] > Naomi[i]) {
          used[j] = true;
          found = true;
          break;
        }
      
      ret2 += !found;
    }
    SET(used, 0);
    int st = 0;
    if (fabs(Ken[N - 1] - 1) < 1e-9) {
      used[N - 1] = true;
      st = 1;
      Naomi[0] = -1;
    }
    ffor (i, st, N) {
      bool found = false;
      int idxl = -1, idxr = -1;
      FOR (j, N)
        if (!used[j]) {
          idxl = j;
          break;
        }

      FOR (j, N)
        if (!used[j])
          idxr = j;

      double val = Naomi[i];
      if (val < Ken[idxl])
        val = Ken[idxr] - 1e-9;
      else
        val = 1.01;
      FOR (j, N)
        if (!used[j] && Ken[j] > val) {
          used[j] = true;
          found = true;
          break;
        }
      
      if (!found) {
        FOR (j, N)
          if (!used[j]) {
            used[j] = true;
            break;
          }
      }
      
      ret1 += !found;
    }
    cout << "Case #" << (test + 1) << ": ";
    cout << ret1 << " " << ret2;
    cout << "\n";
  }
  return 0;
}
