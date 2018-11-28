#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <complex> 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

#define sf(n)         scanf("%lf",&n)
#define fill(a,v)     memset(a, v, sizeof a)
#define bitcount      __builtin_popcount
#define all(x)        x.begin(), x.end()
#define pb(z)       push_back( z )
#define gcd           __gcd

bool isNum(char c) { return ('0' <= c && c <= '9'); }
template<typename T>
T read(T &res) {
  res = 0; char c, neg = 0;
  do { c=getchar(); } while (!isNum(c) && c != '-');
  if (c == '-') { neg = 1; c = getchar(); }
  while (isNum(c)) { res = res * 10 + c-'0'; c = getchar(); }
  return neg ? -res : res;
}

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define readInt read<int>
#define readLL read<ll>

//37ae83cb1254dc6d8f3f075ebd91cb

int main() {
  int T; cin>>T;
  for (int ti=1; ti <= T; ti++) {
    int D; cin>>D;
    vector<int> q;
    for (int i=0; i < D; i++) {
      int pi;
      cin>>pi;
      q.push_back(pi);
    }
    
    int maxQ = *max_element(all(q));
    int bestTime = maxQ;
    
    for (int eat=1; eat <= maxQ; eat++) {
      int timeToEat = eat;
      for (int i=0; i < (int)q.size(); i++) {
        if (q[i] > eat) {
          int pauses = (q[i] + eat - 1) / eat - 1;
          timeToEat += pauses;
        }
      }
      // cout << "timeEating=" << eat << " timeToFinish=" << timeToEat << " pauses=" << (timeToEat - eat) << endl;
      bestTime = min(bestTime, timeToEat);
    }
    
    cout << "Case #" << ti << ": " << bestTime << endl;
  }
}
