#pragma comment(linker,"/STACK:100000000000,100000000000")

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <stack>
#include <set>
#include <iomanip>
#include <queue>
#include <map>
#include <functional>
#include <list>
#include <sstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <list>
#include <cassert>
#include <complex>

using namespace std;

/* Constants begin */
const long long inf = 1e18+7;
const long long mod = 1e9+9;
const double eps = 1e-9;
const double PI = 2*acos(0.0);
const double E = 2.71828;
/* Constants end */

/* Defines begin */
#define pb push_back
#define mp make_pair
#define ll long long
//#define double long double
#define F first
#define S second
#define all(a) (a).begin(),(a).end()
#define forn(i,n) for (int (i)=0;(i)<(n);(i)++)
#define random (rand()<<16|rand())
#define sqr(x) (x)*(x)
#define base complex<double>
/* Defines end */

char s[55][55];

int res = 0;

int a[55];

bool u[55][55];

bool nxt(int a[], int n, int k){
  for(int i = k - 1; i >= 0; --i){
    if(a[i] < n - k + i){
      ++a[i];
      for(int j = i + 1; j < k; ++j){
        a[j] = a[j - 1] + 1;
      }
      return true;
    }
  }
  return false;
}

int sx[100005], sy[100005], sz;

int dx[] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[] = {1, -1, 0, 0, 1, -1, 1, -1};

void Solve(){
  int n, m, w; scanf("%d %d %d", &n, &m, &w);
  forn(i, w){
    a[i] = i;
  }
  do{
    forn(i, n) forn(j, m) s[i][j] = '.', u[i][j] = 0;
    forn(i, w) s[a[i] / m][a[i] % m] = '*';
    forn(i, n){
      forn(j, m) if(s[i][j] == '.'){
        sz = 0;
        sx[sz] = i;
        sy[sz++] = j;
        u[i][j] = true;
        int qt = 0;
        int cnt = 0;
        while(qt != sz){
          int x = sx[qt], y = sy[qt++];
          ++cnt;
          int nc = 0;
          forn(j, 8){
            int nx = x + dx[j], ny = y + dy[j];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m){
              continue;
            }
            if(s[nx][ny] == '*'){
              ++nc;
            }
          }
          if(nc) continue;

          forn(j, 8){
            int nx = x + dx[j], ny = y + dy[j];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m){
              continue;
            }
            if(!u[nx][ny]){
              u[nx][ny] = true;
              sx[sz] = nx;
              sy[sz] = ny;
              ++sz;
            }
          }

        }
        if(cnt == n * m - w){
          s[i][j] = 'c';
          forn(i, n){
            forn(j, m){
              printf("%c", s[i][j]);
            }
            printf("\n");
          }
          return;
        }
      }
    }
  }while(nxt(a, n * m, w));
  puts("Impossible");
}

int main(void){
  #ifdef nobik
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
  #endif
  int t; scanf("%d", &t);
  forn(i, t){
    printf("Case #%d:\n", i + 1);
    cerr << i + 1 << endl;
    Solve();
  }
  return 0;
}
