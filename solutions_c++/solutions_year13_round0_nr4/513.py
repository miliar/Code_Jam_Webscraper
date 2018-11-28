#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>


using namespace std;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
int _a;
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) a.begin(), a.end()


typedef long long ll;
typedef pair< ll , ll > PLL;
typedef vector< PLL > vpll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;
typedef vector< PII > vpii;

multiset<int> have[1<<20];
string best[1<<20];
multiset<int> provides[20];

void solveCase() {
  int n, k;
  k = GETINT; n = GETINT;
  int mx = (1 << n);
  int need[n];
  FOR(i, mx) have[i].clear();
  FOR(i, mx) best[i] = "";
  FOR(i, n) provides[i].clear();

  for (int i = 0; i < k; i++) have[0].insert(GETINT);
  for (int i = 0; i < n; i++) {
    need[i] = GETINT;
    int count = GETINT;
    for(int j = 0; j < count; j++) provides[i].insert(GETINT);
  }

  for (unsigned int mask = 1; mask < mx; mask++) {
    best[mask] = "z";
    int bitcount = __builtin_popcount(mask);
    best[mask] = "z";
    for (int i = 0; i < n; i++) {
      char c = 'a' + i;
      int prev = mask ^ (1 << i);
      if (prev > mask ||
          best[prev] == "z" ||
          have[prev].find(need[i]) == have[prev].end() ||
          best[mask] < (best[prev] + c)) continue;

      best[mask] = best[prev] + c;
      have[mask] = have[prev];
      have[mask].erase(have[mask].find(need[i]));
      for (multiset<int>::iterator it = provides[i].begin(); it != provides[i].end(); it++) {
        have[mask].insert(*it);
      }
    }
  }

  if (best[mx-1] == "z") printf(" IMPOSSIBLE\n");
  else {
    istringstream in(best[mx-1]);
    for (int i = 0; i < n; i++) {
      char c;
      in >> c;
      printf(" %d", (c - 'a') + 1);
    }
    printf("\n");
  }
}

int main() 
{
  int t = GETINT;
  for (int test = 1; test <= t; test++) {
    printf("Case #%d:", test);
    solveCase();
  }
  return 0;
}
