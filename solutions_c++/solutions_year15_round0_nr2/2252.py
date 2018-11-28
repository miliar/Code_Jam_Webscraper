/*
  Problem B. Infinite House of Pancakes

  Small input
  9 points

  Large input
  12 points

  At the Infinite House of Pancakes, there are only finitely many
  pancakes, but there are infinitely many diners who would be willing to
  eat them! When the restaurant opens for breakfast, among the
  infinitely many diners, exactly D have non-empty plates; the ith of
  these has Pi pancakes on his or her plate. Everyone else has an empty
  plate.

  Normally, every minute, every diner with a non-empty plate will eat one
  pancake from his or her plate. However, some minutes may be special.
  In a special minute, the head server asks for the diners' attention,
  chooses a diner with a non-empty plate, and carefully lifts some number
  of pancakes off of that diner's plate and moves those pancakes onto one
  other diner's (empty or non-empty) plate. No diners eat during a
  special minute, because it would be rude.

  You are the head server on duty this morning, and it is your job to
  decide which minutes, if any, will be special, and which pancakes will
  move where. That is, every minute, you can decide to either do nothing
  and let the diners eat, or declare a special minute and interrupt the
  diners to make a single movement of one or more pancakes, as described
  above.

  Breakfast ends when there are no more pancakes left to eat. How
  quickly can you make that happen?

  Input

  The first line of the input gives the number of test cases, T. T test
  cases follow. Each consists of one line with D, the number of diners
  with non-empty plates, followed by another line with D space-separated
  integers representing the numbers of pancakes on those diners' plates.

  Output

  For each test case, output one line containing "Case #x: y", where x
  is the test case number (starting from 1) and y is the smallest number
  of minutes needed to finish the breakfast.

  Limits

  1 ≤ T ≤ 100.
  Small dataset

  1 ≤ D ≤ 6.
  1 ≤ Pi ≤ 9.
  Large dataset

  1 ≤ D ≤ 1000.
  1 ≤ Pi ≤ 1000.
  Sample

  Input

  3
  1
  3
  4
  1 2 1 2
  1
  4

  Output

  Case #1: 3
  Case #2: 2
  Case #3: 3
*/

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
//#include <regex>
//#include <tr1/memory>

/* compilation flags: */
/* g++ -g -std=c++0x google_codejam_T.cpp */
/* g++ -g -std=c++11 google_codejam_T.cpp */

using namespace std;
//using namespace std::tr1;

// std::ios::sync_with_stdio(false);

// freopen("input.txt", "rt", stdin);
// freopen("output.txt", "wt", stdout);

#define ALL(c)          (c).begin(), (c).end()
#define ALLR(c)         (c).rbegin(), (c).rend()
#define FOR(i,a,b)      for (__typeof(a) i=(a); i < (b); ++i)
#define FORR(i,a,b)     for (__typeof(a) i=(a); i > (b); --i)
#define FOR_ALL(i,c)    for (__typeof((c).begin()) i=(c).begin();   \
                             i != (c).end(); ++i)
#define FOR_ALLR(i,c)   for (__typeof((c).rbegin()) i=(c).rbegin(); \
                             i != (c).rend(); ++i)
#define SZ(array)       (sizeof(array)/sizeof(array[0]))
#define lc(x)           (x<<1)     /* 2*x */
#define rc(x)           (x<<1 | 1) /* 2*x+1 */
#define lowbit(x)       (x & (-x)) /* 0b10100 -> 0b100 */

typedef long long       LL;
typedef map<int,int>    MII;
typedef set<int>        SI;
typedef vector<int>     VI;
typedef vector<string>  VS;
typedef pair<int,int>   PII;

/* gcj 2015 qualify - Problem B. Infinite House of Pancakes */
/*
 */

bool P(int mid, const VI& A)
{
    /* split days into 2 parts */
    int x;                      /* x days for reduce */
    int y;                      /* y days for eat */
    for (x = 0; x < mid; x++) { /* need to try all case */
        y = mid - x;
        int days = 0;
        FOR_ALL(a,A) if (*a > y) {
            days += *a/y - 1;
            if (*a % y != 0)
                days += 1;
        }
        if (days <= x)
            return true;
    }
    return false;
}

int solve(VI A)
{
    int lo,hi; lo = 1; hi = 1005;
    while (lo < hi) {
        int mid = lo + (hi-lo)/2;
        if (P(mid,A))
            hi = mid;
        else
            lo = mid+1;
    }
    if (P(lo,A) == false)
        assert(0);
    return lo;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int T; scanf("%d",&T);
    int t = 0;
    while (T--) {
        int D; cin >> D;
        VI A(D);
        FOR(i,0,D) cin >> A[i];
        int ans = solve(A);
        printf("Case #%d: ",++t);
        printf("%d\n", ans);
    }
    return 0;
}
