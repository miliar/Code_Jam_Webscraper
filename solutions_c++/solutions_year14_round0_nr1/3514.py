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
  freopen("As.out","wt", stdout);
  freopen("As.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int r, c[4][4];
    int cnt[16];
    SET(cnt, 0);
    FOR (s, 2) {
      cin >> r;
      r--;
      FOR (i, 4)
        FOR (j, 4) {
          cin >> c[i][j];
          c[i][j]--;
        }
      FOR (j, 4)
        cnt[c[r][j]]++;
    }
    
    int cc = 0, val = -1;
    FOR (i, 16) {
      cc += cnt[i] == 2;
      if (cnt[i] == 2)
        val = i + 1;
    }
    cout << "Case #" << (test + 1) << ": ";
    if (cc == 0)
      cout << "Volunteer cheated!";
    else if (cc > 1)
      cout << "Bad magician!";
    else
      cout << val;
    cout << "\n";
  }
  return 0;
}
