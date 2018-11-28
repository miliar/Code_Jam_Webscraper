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
    double C, F, X;
    cin >> C >> F >> X;
    double ret = X / 2.0;
    double curr = 0.0;
    int cnt = 1;
    while (cnt) {
      double need = C / (2.0 + (cnt - 1) * F);
      curr += need;
      if (curr > ret - 1e-9)
        break;
      
      if (curr + X / (2.0 + cnt * F) < ret)
        ret = curr + X / (2.0 + cnt * F);
      cnt++;
    }
    cout << "Case #" << (test + 1) << ": ";
    printf("%.7lf", ret);
    cout << "\n";
  }
  return 0;
}
