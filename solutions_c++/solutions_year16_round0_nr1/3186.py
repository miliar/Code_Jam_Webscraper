/*
  Google Code Jam
  Qualification Round 2016

  Problem A. Counting Sheep

  Small input
  7 points

  Large input
  8 points

  Bleatrix Trotter the sheep has devised a strategy that helps her fall
  asleep faster. First, she picks a number N. Then she starts naming N,
  2*N, 3*N, and so on. Whenever she names a number, she thinks about all
  of the digits in that number. She keeps track of which digits
  (0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) she has seen at least once so far
  as part of any number she has named. Once she has seen each of the ten
  digits at least once, she will fall asleep.

  Bleatrix must start with N and must always name (i+1)*N directly after
  i*N. For example, suppose that Bleatrix picks N = 1692. She would
  count as follows:

  N = 1692. Now she has seen the digits 1, 2, 6, and 9.
  2N = 3384. Now she has seen the digits 1, 2, 3, 4, 6, 8, and 9.
  3N = 5076. Now she has seen all ten digits, and falls asleep.

  What is the last number that she will name before falling asleep? If
  she will count forever, print INSOMNIA instead.

  Input

  The first line of the input gives the number of test cases, T. T test
  cases follow. Each consists of one line with a single integer N, the
  number Bleatrix has chosen.

  Output

  For each test case, output one line containing Case #x: y, where x is
  the test case number (starting from 1) and y is the last number that
  Bleatrix will name before falling asleep, according to the rules
  described in the statement.

  Limits

  1 <= T <= 100.

  Small dataset
  0 <= N <= 200.

  Large dataset
  0 <= N <= 1e6.

  Sample

  Input

  5
  0
  1
  2
  11
  1692

  Output

  Case #1: INSOMNIA
  Case #2: 10
  Case #3: 90
  Case #4: 110
  Case #5: 5076


  In Case #1, since 2 * 0 = 0, 3 * 0 = 0, and so on, Bleatrix will never
  see any digit other than 0, and so she will count forever and never
  fall asleep. Poor sheep!

  In Case #2, Bleatrix will name 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. The 0
  will be the last digit needed, and so she will fall asleep after 10.

  In Case #3, Bleatrix will name 2, 4, 6... and so on. She will not see
  the digit 9 in any number until 90, at which point she will fall
  asleep. By that point, she will have already seen the digits
  0, 1, 2, 3, 4, 5, 6, 7, and 8, which will have appeared for the first
  time in the numbers 10, 10, 2, 30, 4, 50, 6, 70, and 8, respectively.

  In Case #4, Bleatrix will name
  11, 22, 33, 44, 55, 66, 77, 88, 99, 110 and then fall asleep.

  Case #5 is the one described in the problem statement. Note that it
  would only show up in the Large dataset, and not in the Small dataset.
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

/* gcj 2016 Qualification Problem A. Counting Sheep */

const int inf = 1e9;
const int maxc = 1e7;
bool digit[10];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("foo", "rt", stdin);
#endif
    int t=0,T; cin >> T;
    while (T--) {
        memset(digit,false,sizeof(digit));
        LL N; cin >> N;
        LL X = N;
        LL ans = inf;
        FOR(_,0,maxc) {
            LL Y = X;
            while (Y) {
                const int d = Y % 10;
                digit[d] = true;
                Y /= 10;
            }
            bool good = true;
            FOR(i,0,10)
                good &= digit[i];
            if (good) {
                ans = X;
                break;
            }
            X += N;
        }
        printf("Case #%d: ",++t);
        if (ans == inf)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",ans);
    }
    return 0;
}
