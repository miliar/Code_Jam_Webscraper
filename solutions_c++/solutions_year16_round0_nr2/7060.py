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

string S;

void parse() {
  cin >> S;
}

// greedy
int solve() {
  bool flip = false;
  int r = 0;
  for(int i = S.length()-1; i >= 0; i--) {
    if((S[i] == '-') != flip) {
      flip = !flip;
      r++;
    }
  }
  return r;
}

int main() {
  //ios::sync_with_stdio(false);
  int T;
  scanf("%d", &T);
  for(int i = 1; i <= T; i++) {
    parse();
    printf("Case #%d: %d\n", i, solve());
    #ifdef DEBUG
		  fprintf(stderr, "%d / %d = %.2fs | %.2fs\n", i, T, (double)clock () / CLOCKS_PER_SEC, ((double)clock () / i * T) / CLOCKS_PER_SEC);
    #endif
  }
  return 0;
}
