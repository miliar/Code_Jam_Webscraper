#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int main()
{
  int T;
  scanf("%d", &T);

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    lglg N;

    scanf("%lld", &N);

    lglg NN = N;

    vector<bool> done(10, false);
    string s;

    int i;

    for(i = 0; i < 5000; ++i) {
      s = to_string(NN);
      for(char c : s) {
        if(c >= '0' && c <= '9') {
          done[c - '0'] = true;
        }
      }

      if(all_of(done.begin(), done.end(), [](bool b){return b;})) {
        printf("%lld\n", NN);
        break;
      }

      NN += N;
    }

    if(i == 5000) {
      printf("INSOMNIA\n");
    }

  }

  return 0;
}
