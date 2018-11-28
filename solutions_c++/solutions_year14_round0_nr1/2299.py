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
  /* Precalxc */

  int tests_count;
  scanf("%d\n", &tests_count);
  for (int test_number = 1; test_number <= tests_count; ++test_number) {
    printf("Case #%d: ", test_number);
    /* Clear all! */
    
    /* Solution */
    int rowFirst, rowSecond;
    vvi first(4, vi(4)), second(4, vi(4));
    scanf("%d", &rowFirst);
    --rowFirst;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
        scanf("%d", &first[i][j]);
    scanf("%d", &rowSecond);
    --rowSecond;
    for (int i = 0; i < 4; i++)
      for (int j = 0; j < 4; j++)
        scanf("%d", &second[i][j]);
    vi one = first[rowFirst];
    vi two = second[rowSecond];
    sort(all(one));
    sort(all(two));
    int p1 = 0, p2 = 0;
    vi eq;
    while (p1 < sz(one) && p2 < sz(two)) {
      if (one[p1] == two[p2])
        eq.pb(one[p1]), ++p1, ++p2;
      else
      if (one[p1] < two[p2])
        ++p1;
      else
        ++p2;
    }
    if (!sz(eq))
      puts("Volunteer cheated!");
    else
    if (sz(eq) > 1)
      puts("Bad magician!");
    else
      printf("%d\n", eq[0]);
  }
  return 0;
}

