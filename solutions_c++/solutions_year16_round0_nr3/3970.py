#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <unordered_set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

const int B = 27397, MOD = 1e9 + 7;
const int B1 = 33941, MOD1 = 1e9 + 9;

int N, J;

unordered_set <llint> S; 

llint div(llint x) {
  for (int i = 2; (llint) i * i <= x; ++i) 
    if (x % i == 0) 
      return i;
  return 1; 
}

llint to_base(llint mask, llint b) {
  llint p = 1, ret = 0;
  for (int i = 0; i < N; ++i) {
    if ((mask & (1LL << i)))
      ret += p;
    p *= b;
  }
  return ret; 
}

inline void print_mask(llint mask) {
  for (int i = N - 1; i >= 0; --i)
    if ((mask & (1LL << i)))
      printf("1");
    else
      printf("0");
  printf(" ");
}

int main(void) {

  srand(time(NULL));
  printf("Case #1:\n");

  int T; scanf("%d", &T);
  scanf("%d%d", &N, &J);
 
  while (J > 0) {
    
    llint mask = 0;
    
    for (int i = 0; i < N; ++i) 
      if (rand() & 1) 
        mask |= (1LL << i);
  
    mask |= 1;
    mask |= 1LL << (N - 1);

    if (S.find(mask) != S.end())
      continue;

    S.insert(mask);

    vector <llint> ret; 
    for (int i = 2; i <= 10; ++i) {
      llint d = div(to_base(mask, i));
      if (d == 1) 
        break;
      else
        ret.push_back(d);
    }

    if ((int) ret.size() == 9) {
      print_mask(mask);
      for (llint d : ret) 
        printf("%lld ", d);
      printf("\n");
      --J;
    }
      
  }

  return 0;

}

