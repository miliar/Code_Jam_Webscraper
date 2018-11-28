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

using namespace std;

int T;
long long N;

int update(long long n, vector<int>& vis) {
  while(n > 0) {
    vis[n%10] = true;
    n /= 10;
  }
  int sum = 0;
  REP(i,SIZE(vis)) sum += vis[i];
  return sum;
}

int main(void) {
  cin >> T;
  REP(t,T) {
    cin >> N;
    vector<int> vis(10, false);
    int done = 0;
    for(long long i=1; i < 1000; ++i) {
      if (update(i*N, vis) == 10) {
        done = i*N;
        break;
      }
    }
    cout << "Case #" << t+1 << ": ";
    if (done!=0) cout << done << endl;
    else cout << "INSOMNIA" << endl;
  }
  return 0;
}
