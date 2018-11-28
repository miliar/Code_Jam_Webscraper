#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<cmath>
#include<string>
#include<set>
#include<vector>

using namespace std;

long long F(int N, long long P) {
  if (P == 0) return -1;
  long long res = 0;
  long long cnt = 1LL << N;
  long long cur = 2;
  while (P >= cur) {
    cur = cur << 1;
    cnt = cnt >> 1;
    res = res + cnt;
  }
  return res;
}


int main() {
  int T, n, i, j, cn, w;
  long long r1, r2, p;
  int X, Y;
  cin >> T;
  for(cn=0; cn<T; cn++){
    cin >> n >> p;
    r1 = F(n, p);
    r2 = (1LL << n) - 2 - F(n, (1LL << n) - p);
    cout << "Case #" << cn+1 << ": " << r2 << " " << r1 << "\n";
   }
  return 0;
}