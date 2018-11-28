#define TASKNAME "text"
#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cassert>
#include <functional>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
 
#define EPS (1e-9)
#define INF int(1e9)
#define INFLONG (long long)(1e18)
#define sqr(a) ((a) * (a))
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define abs(a) (((a) < 0) ? -(a) : (a))
#define sz(a) (int)a.size()
#define fst first
#define snd second
#define y1 osrughosduvgarligybakrybrogvba
#define y0 aosfigdalrowgyalsouvgrlvygalri                               
#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef vector <pii> vpii;

int main() {
  freopen(TASKNAME".in", "r", stdin);
  freopen(TASKNAME".out", "w", stdout);
  /* Precalc */

  int tests_count;
  scanf("%d\n", &tests_count);
  for (int test_number = 1; test_number <= tests_count; ++test_number) {
    printf("Case #%d: ", test_number);
    /* Clear all! */
    
    /* Solution */
    int n;
    set <int> one, two;
    set <int> one2, two2;
    double x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
      scanf("%lf", &x);
      int y = int(x * 1000000);
      one.insert(y);
      one2.insert(y);
    }
    for (int i = 0; i < n; i++) {
      scanf("%lf", &x);
      int y = int(x * 1000000);
      two.insert(y);
      two2.insert(y);
    }

    vi ans(2, 0);
    for (int it = 0; it < n; it++) {
      set <int>::iterator iter = two.end();
      --iter;
      int biggest = *iter;
      if (*one.begin() > biggest) {
        ans[0] += sz(one);
        break;
      }
      if (*one.rbegin() > biggest) {
        one.erase(one.lower_bound(biggest));
        two.erase(iter);
        ans[0]++;
      } else {
        one.erase(one.begin());
        two.erase(iter);
      }
    }

    for (int it = 0; it < n; it++) {
      set <int>::iterator iter = two2.end();
      --iter;
      int biggestTwo = *iter;
      iter = one2.end();
      --iter;
      int biggestOne = *iter;
      ans[1] += biggestOne > biggestTwo;
      if (biggestOne > biggestTwo) {
        one2.erase(biggestOne);
        two2.erase(two2.begin());
      } else {
        one2.erase(biggestOne);
        two2.erase(biggestTwo);
      }
    }
    printf("%d %d\n", ans[0], ans[1]);
  }
  eprintf("%.5lf\n", double(clock()) / CLOCKS_PER_SEC);
  return 0;
}

