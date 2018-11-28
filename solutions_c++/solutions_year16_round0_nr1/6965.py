// solution by Olivier Marty

//#define ONLINE_JUDGE
#include <bits/stdc++.h>
#define fin(i, n) for(int i = 0; i < n; i++)
#define fin2(i, a, b) for(int i = a; i < b; i++)
#define pb push_back
#define mp make_pair
using namespace std;

#ifndef ONLINE_JUDGE
  #define debug(a) cerr << #a << " = " << (a) << endl
#else
  #define debug(a)
#endif

int N;

void parse() {
  scanf("%d", &N);
}

int solve_naive() {
  if(!N)
    return -1;
  else
  {
    bool d[10] = {false, false, false, false, false, false, false, false, false, false};
    long long x = 0;
    while(!d[0] || !d[1] || !d[2] || !d[3] || !d[4] || !d[5] || !d[6] || !d[7] || !d[8] || !d[9]) {
      x += N;
      long long y = x;
      while(y) {
        d[y%10] = true;
        y/=10;
      }
    }
    return x;
  }
}

int solve() {
  return solve_naive();
}

int main() {
  //ios::sync_with_stdio(false);
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++) {
    parse();
    printf("Case #%d: ", i);
    int x = solve();
    if(x < 0)
      printf("INSOMNIA\n");
    else
      cout << x << endl;
    #ifdef DEBUG
		  fprintf(stderr, "%d / %d = %.2fs | %.2fs\n", i, T, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * T) / CLOCKS_PER_SEC);
    #endif
  }
  return 0;
}
