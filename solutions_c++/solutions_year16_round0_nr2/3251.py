/*
  Google Code Jam
  Qualification Round 2016

  Problem B. Revenge of the Pancakes

  Small input
  10 points

  Large input
  10 points

  The Infinite House of Pancakes has just introduced a new kind of
  pancake! It has a happy face made of chocolate chips on one side
  (the "happy side"), and nothing on the other side (the "blank side").

  You are the head waiter on duty, and the kitchen has just given you a
  stack of pancakes to serve to a customer. Like any good pancake
  server, you have X-ray pancake vision, and you can see whether each
  pancake in the stack has the happy side up or the blank side up. You
  think the customer will be happiest if every pancake is happy side up
  when you serve them.

  You know the following maneuver: carefully lift up some number of
  pancakes (possibly all of them) from the top of the stack, flip that
  entire group over, and then put the group back down on top of any
  pancakes that you did not lift up. When flipping a group of pancakes,
  you flip the entire group in one motion; you do not individually flip
  each pancake. Formally: if we number the pancakes 1, 2, ..., N from
  top to bottom, you choose the top i pancakes to flip. Then, after the
  flip, the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N. Pancakes
  1, 2, ..., i now have the opposite side up, whereas pancakes
  i+1, i+2, ..., N have the same side up that they had up before.

  For example, let's denote the happy side as + and the blank side as -.
  Suppose that the stack, starting from the top, is --+-. One valid way
  to execute the maneuver would be to pick up the top three, flip the
  entire group, and put them back down on the remaining fourth pancake
  (which would stay where it is and remain unchanged). The new state of
  the stack would then be -++-. The other valid ways would be to pick up
  and flip the top one, the top two, or all four. It would not be valid
  to choose and flip the middle two or the bottom one, for example; you
  can only take some number off the top.

  You will not serve the customer until every pancake is happy side up,
  but you don't want the pancakes to get cold, so you have to act fast!
  What is the smallest number of times you will need to execute the
  maneuver to get all the pancakes happy side up, if you make optimal
  choices?

  Input

  The first line of the input gives the number of test cases, T. T test
  cases follow. Each consists of one line with a string S, each
  character of which is either + (which represents a pancake that is
  initially happy side up) or - (which represents a pancake that is
  initially blank side up). The string, when read left to right,
  represents the stack when viewed from top to bottom.

  Output

  For each test case, output one line containing Case #x: y, where x is
  the test case number (starting from 1) and y is the minimum number of
  times you will need to execute the maneuver to get all the pancakes
  happy side up.

  Limits

  1 <= T <= 100.
  Every character in S is either + or -.

  Small dataset
  1 <= length of S <= 10.

  Large dataset
  1 <= length of S <= 100.

  Sample

  Input

  5
  -
  -+
  +-
  +++
  --+-

  Output

  Case #1: 1
  Case #2: 1
  Case #3: 2
  Case #4: 0
  Case #5: 3

  In Case #1, you only need to execute the maneuver once, flipping the
  first (and only) pancake.

  In Case #2, you only need to execute the maneuver once, flipping only
  the first pancake.

  In Case #3, you must execute the maneuver twice. One optimal solution
  is to flip only the first pancake, changing the stack to --, and then
  flip both pancakes, changing the stack to ++. Notice that you cannot
  just flip the bottom pancake individually to get a one-move solution;
  every time you execute the maneuver, you must select a stack starting
  from the top.

  In Case #4, all of the pancakes are already happy side up, so there is
  no need to do anything.

  In Case #5, one valid solution is to first flip the entire stack of
  pancakes to get +-++, then flip the top pancake to get --++, then
  finally flip the top two pancakes to get ++++.
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
#include <iomanip>
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

/* g++ -g -std=c++0x */
/* g++ -g -std=c++11 */

using namespace std;

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
typedef pair<int,int>   PII;
typedef set<int>        SI;
typedef vector<bool>    VB;
typedef vector<double>  VD;
typedef vector<int>     VI;
typedef vector<string>  VS;

/* check if a key is in container C */
template <class C>
inline bool in_(const typename C::key_type& k, const C& A)
{ return A.find(k) != A.end(); }

/* gcj 2016 Qualification Problem B. Revenge of the Pancakes */
/*
 * Flip all pancakes in order, find the min number of flips.
 */

const int inf = 1e9;
const int maxn = 110;
/* dp(i,side); there seem to be no overlapping, dp[] is not used */
int dp[maxn][2];
int A[maxn];

int dfs(const int i, const int side, const int A[])
{
    if (i == 0)
        return A[i] == side ? 0 : 1;
    int& ans = dp[i][side];
    if (ans == -1) {
        if (A[i] == side)
            ans = dfs(i-1,side,A);
        else
            ans = dfs(i-1,side^1,A) + 1;
        assert(ans >= 0);
    }
    return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int t=0,T; cin >> T;
    while (T--) {
        memset(dp,-1,sizeof(dp));
        string S; cin >> S;
        const int n = S.size();
        FOR(i,0,n)
            A[i] = S[i] == '-' ? 0 : 1;
        const int ans = dfs(n-1,1,A);
        printf("Case #%d: %d\n",++t,ans);
    }
    return 0;
}
