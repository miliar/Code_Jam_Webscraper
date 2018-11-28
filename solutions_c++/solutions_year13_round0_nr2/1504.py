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

int a[100][100];
int b[100][100];

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    int n, m;
    cin >> n >> m;
    FOR (i, n)
      FOR (j, m)
        cin >> a[i][j];

    FOR (i, n)
      FOR (j, m)
        b[i][j] = 100;
    bool change = true;
    FOR (i, n) {
      int mm = -1;
      FOR (j, m)
        mm >?= a[i][j];
      FOR (j, m)
        b[i][j] <?= mm;
    }

    FOR (j, m) {
      int mm = -1;
      FOR (i, n)
        mm >?= a[i][j];
      FOR (i, n)
        b[i][j] <?= mm;
    }

    bool good = true;
    FOR (i, n)
      FOR (j, m)
        if (a[i][j] != b[i][j])
          good = false;
    cout << "Case #" << (test + 1) << ": ";
    if (good)
      cout << "YES";
    else
      cout << "NO";
    cout << "\n";
  }
  return 0;
}
