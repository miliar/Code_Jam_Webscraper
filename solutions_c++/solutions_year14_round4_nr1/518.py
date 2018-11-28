#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <functional>
#include <complex>
#include <iomanip>

using namespace std;

typedef long long ll;

int s[10000];

int main(void){
  int T;
  cin >> T;
  for(int tt = 0; tt < T; ++tt){
    int N, M;
    cin >> N >> M;

    for(int i = 0; i < N; ++i){
      cin >> s[i];
    }

    sort(s, s+N);

    int cnt = 0;
    int f = 0, t = N-1;
    while(f <= t){
      if(f == t){
        ++cnt;
        break;
      }

      // cout << f << "," << t << endl;

      if(s[f] + s[t] <= M){
        ++f;
        --t;
      }
      else{
        --t;
      }
      ++cnt;
    }

    cout << "Case #" << tt+1 << ": " << cnt << endl;
  }

  return 0;
}
