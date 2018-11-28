#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <iostream>
#include <complex>
#include <sstream>
using namespace std;
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
 
#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)
#define ALL(v) (v).begin(), (v).end()
 
#define pb push_back
#define mp make_pair
#define st first
#define nd second

vector<pair<LL, LL>> hikers;

void scase() {
  hikers.clear();
  
  int N;
  scanf("%d", &N);
  REP(i,N) {
    int D, H, M;
    scanf("%d%d%d", &D, &H, &M);
    REP(j, H) {
      hikers.push_back(mp(2 * (360 - D) * (LL)(M + j), 2 * 360 * (LL)(M + j)));
    }
  }
  
  int result = hikers.size();
  
  priority_queue<pair<LL, LL>, vector<pair<LL, LL>>, greater<pair<LL, LL>>> slow;
  priority_queue<pair<LL, LL>, vector<pair<LL, LL>>, greater<pair<LL, LL>>> next;
  REP(i, hikers.size()) slow.push(hikers[i]);
  
  int overtook = 0;
  while (overtook < result) {
    LL T = min(
      slow.empty() ? next.top().st : slow.top().st,
      next.empty() ? slow.top().st : next.top().st
    );
    while (!slow.empty() && slow.top().st == T) {
      pair<LL, LL> p = slow.top();
      slow.pop();
      next.push(mp(p.st + p.nd, p.nd));
    }
    while (next.top().st == T) {
      ++overtook;
      pair<LL, LL> p = next.top();
      next.pop();
      next.push(mp(p.st + p.nd, p.nd));
    }
    result = min(result, overtook + (int)slow.size());
  }

  printf("%d\n", result); 
}

int main() {
  int Z;
  scanf("%d", &Z);
  REP(z,Z) {
    printf("Case #%d: ", z+1);
    scase();
  }
}    
