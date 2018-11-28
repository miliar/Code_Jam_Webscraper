#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SGN(x) (x < 0 ? -1 : ( x > 0 ? 1 : 0 ) )

using namespace std;

int T, L, X;

char Q[4][4] = { {1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1} };

vector<int> prefix;
vector<int> suffix;

int main(void) {
  cin >> T;
  REP(t,T) {
    cout << "Case #" << t+1 << ": ";
    string S, s;
    cin >> L >> X;
    cin >> s;
    REP(x, X) S += s;

    prefix.resize(SIZE(S));
    suffix.resize(SIZE(S));

    prefix[0] = S[0] - 'i' + 2;
    for(int i = 1; i < SIZE(S); ++i)
      prefix[i] = SGN(prefix[i-1]) * Q[abs(prefix[i-1]) - 1][S[i] - 'i' + 1];
    suffix[SIZE(S)-1] = S[SIZE(S)-1] - 'i' + 2;
    for(int i = SIZE(S) - 2; i >= 0; --i)
      suffix[i] = SGN(suffix[i+1]) * Q[S[i] - 'i' + 1][abs(suffix[i+1]) - 1];

    bool found = false;
    for(int i=0; i < SIZE(S) - 2; ++i)
      for(int j=i+2; j < SIZE(S); ++j) {
        if (prefix[i]   != 2) continue;
        if (suffix[j]   != 4) continue;
        if (suffix[i+1] != 2) continue;
        found = true;
        break;
      }
    if (found) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
