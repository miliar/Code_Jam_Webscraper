#include <unordered_map>
#include <cstring>
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
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <unordered_set>

using namespace std;

#define TASKI "in.txt"
#define TASKO "o.txt"
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back
#define mp make_pair
#define _map unordered_map
#define _set unordered_set
#define sz(x) ((int)(x).size())
#define it(x) (x).begin(), (x).end()
#define rt(x) (x).rbegin(), (x).rend()

#define TIMESTAMP(x)  eprintf("[" #x "] Time = %.5lfs\n",clock()*1.0/CLOCKS_PER_SEC)

#ifdef DEBUG
struct __timestamper {
  ~__timestamper() {
    TIMESTAMP(end);
  }
} __Timestamper;
#else
struct __timestamper {};
#endif

typedef long double ld;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;
typedef pair<ll, ll> pll;
typedef vector<pii> vpi;

int ad[1010];

int main(void) {
  #ifdef DEBUG
  freopen(TASKI, "r", stdin);
  freopen(TASKO, "w", stdout);
  #endif
  
  int tc, cs = 1;
  for (scanf("%d", &tc); tc--; cs++) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; scanf("%d", &ad[i++]));
    sort(ad, ad + n);
    int res = ad[n - 1];
    int time = 2;
    while (time < res) {
      int tmp = 0;
      for_each(ad, ad + n, [&](int x) { tmp += (x - 1) / time; });
      res = min(tmp + time, res);
      time++;
    }
    printf("Case #%d: %d\n", cs, res);
  }
  return 0;
}
