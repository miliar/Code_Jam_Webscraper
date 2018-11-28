/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 * Date: 2015.04.12
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int N = 1e4;

// 1, i, j, k, -1, -i, -j, -k
int inv[] = {0, 5, 6, 7, 4, 1, 2, 3};
enum { O, I, J, K, O1, I1, J1, K1 };
int p[8][8] =
{
  {O, I, J, K, O1, I1, J1, K1}, 
  {I, O1, K, J1, I1, O, K1, J},
  {J, K1, O1, I, J1, K, O, I1},
  {K, J, I1, O1, K1, J1, I, O},
  {O1, I1, J1, K1, O, I, J, K},
  {I1, O, K1, J, I, O1, K, J1},
  {J1, K, O, I1, J, K1, O1, I},
  {K1, J1, I, O, K, J, I1, O1},
};

int n, k, sum[N + 1];
char s[N + 1];

int get( int l, int r ) {
  //printf("[%d..%d) = %d * %d\n", l, r, inv[sum[l]], sum[r]);
  return p[inv[sum[l]]][sum[r]];
}

void solve() {
  scanf("%d%d%s", &n, &k, s);
  forn(i, (k - 1) * n)
    s[i + n] = s[i];
  n *= k;
  sum[0] = 0;
  forn(i, n) 
    sum[i + 1] = p[sum[i]][s[i] - 'i' + 1];
  forn(i, n)
    forn(j, i) {
      //printf("i = %d, j = %d : %d %d %d\n", i, j, get(0, i), get(i, j), get(j, n));
      if (get(0, j) == 1 && get(j, i) == 2 && get(i, n) == 3) {
        puts("YES");
        return;
      }        
    }
  puts("NO");
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}
