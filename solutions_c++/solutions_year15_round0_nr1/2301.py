/*
  Problem A. Standing Ovation

  Small input
  7 points

  Large input
  10 points

  It's opening night at the opera, and your friend is the prima donna
  (the lead female singer). You will not be in the audience, but you
  want to make sure she receives a standing ovation -- with every
  audience member standing up and clapping their hands for her.

  Initially, the entire audience is seated. Everyone in the audience
  has a shyness level. An audience member with shyness level Si will
  wait until at least Si other audience members have already stood up
  to clap, and if so, she will immediately stand up and clap. If Si = 0,
  then the audience member will always stand up and clap immediately,
  regardless of what anyone else does. For example, an audience member
  with Si = 2 will be seated at the beginning, but will stand up to clap
  later after she sees at least two other people standing and clapping.

  You know the shyness level of everyone in the audience, and you are
  prepared to invite additional friends of the prima donna to be in the
  audience to ensure that everyone in the crowd stands up and claps in
  the end. Each of these friends may have any shyness value that you
  wish, not necessarily the same. What is the minimum number of friends
  that you need to invite to guarantee a standing ovation?

  Input

  The first line of the input gives the number of test cases, T. T test
  cases follow. Each consists of one line with Smax, the maximum shyness
  level of the shyest person in the audience, followed by a string of
  Smax + 1 single digits. The kth digit of this string (counting
  starting from 0) represents how many people in the audience have
  shyness level k. For example, the string "409" would mean that there
  were four audience members with Si = 0 and nine audience members with
  Si = 2 (and none with Si = 1 or any other value). Note that there will
  initially always be between 0 and 9 people with each shyness level.

  The string will never end in a 0. Note that this implies that there
  will always be at least one person in the audience.

  Output

  For each test case, output one line containing "Case #x: y", where x
  is the test case number (starting from 1) and y is the minimum number
  of friends you must invite.

  Limits

  1 ≤ T ≤ 100.
  Small dataset

  0 ≤ Smax ≤ 6.
  Large dataset

  0 ≤ Smax ≤ 1000.
  Sample

  Input

  4
  4 11111
  1 09
  5 110011
  0 1

  Output

  Case #1: 0
  Case #2: 1
  Case #3: 2
  Case #4: 0

  In Case #1, the audience will eventually produce a standing ovation on
  its own, without you needing to add anyone -- first the audience
  member with Si = 0 will stand up, then the audience member with Si = 1
  will stand up, etc.

  In Case #2, a friend with Si = 0 must be invited, but that is enough
  to get the entire audience to stand up.

  In Case #3, one optimal solution is to add two audience members with
  Si = 2.

  In Case #4, there is only one audience member and he will stand up
  immediately. No friends need to be invited.
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

/* gcj 2015 qualify - Problem A. Standing Ovation */
/*
 */

bool P(int x, const VI& A)
{
    int n = A.size();
    FOR(i,0,n) {
        if (i > x && A[i])
            return false;
        x += A[i];
    }
    return true;
}

int solve(const VI& A)
{
    int lo,hi; lo = 0; hi = 1005;
    while (lo < hi) {
        int mid = lo + (hi-lo)/2;
        if (P(mid,A))
            hi = mid;
        else
            lo = mid + 1;
    }
    if (P(lo,A) == false)
        assert(false);
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
        int S; cin >> S;
        string s; cin >> s;
        S++;
        VI A(S);
        FOR(i,0,S) {
            int d = s[i] - '0';
            A[i] = d;
        }
        int ans = solve(A);
        printf("Case #%d: ",++t);
        printf("%d\n", ans);
    }
    return 0;
}
