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

vector<int> a;

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int n;
    cin >> n;
    a.clear();
    FOR (i, n) {
      int b;
      cin >> b;
      a.pb(b);
    }
    int x = 0;
    ffor (i, 1, a.sz)
      x += max(a[i - 1] - a[i], 0);
    int rate = 0;
    ffor (i, 1, a.sz)
      rate = max(rate, a[i - 1] - a[i]);
    int y = 0;
    FOR (i, a.sz - 1)
      y += min(rate, a[i]);
    cout << "Case #" << (test + 1) << ": ";
    cout << x << " " << y;
    cout << "\n";
  }
  return 0;
}
