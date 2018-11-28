#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

inline bool pal(long long n) {
  long long rev = 0, old_n = n;

  while (n > 0) {
    rev = rev * 10 + n % 10;
    n /= 10;
  }

  return rev == old_n;
}

inline long long fair(long long i) {
  long long sq = i * i;
  if (!pal(i) || !pal(sq))
    return -1;
  return sq;
}

int main(int argc, char *argv[])
{
  vector<long long> fairs;
  const long long MAX_N = pow(10, 8);

  for (long long i = 0; i < MAX_N; i++) {
    long long f = fair(i);
    if (f != -1)
      fairs.push_back(f);
  }

  int nt;
  scanf("%d", &nt);

  long long a, b;
  for (int t = 1; t <= nt; t++) {
    int posa = -1, posb = -1;
    cin >> a >> b;
    for ( int i = 0; i < fairs.size(); i++) {
      if ( posa == -1 && fairs[i] >= a ) posa = i;
      if ( posb == -1 && fairs[i] >= b ) posb = i;
    }
    if (fairs[posb] == b) posb++;
    printf("Case #%d: %d\n", t, posb - posa);
  }

  return 0;
}
