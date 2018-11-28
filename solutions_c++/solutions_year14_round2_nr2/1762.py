// {{{ Headers
// vim:filetype=cpp:foldmethod=marker:foldmarker={{{,}}}

#include <cassert>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <deque>
#include <functional>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <fstream>
#include <iostream>
#include <sstream>

#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;
// }}}

typedef long long int64;
const int INF = 0x3f3f3f3f;
template <class T> inline int len (const T &a) { return a.size (); }

int
main () {
#ifdef LOCALHOST
    freopen ("test.in", "r", stdin);
    // freopen ("test.out", "w", stdout);
#endif
    int T, a, b, k;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf ("%d %d %d", &a, &b, &k);
        int64 ret = 0;
        for (int i = 0; i < a; i++)
            for (int j = 0; j < b; j++)
                if ((i & j) < k) ret++;
        printf ("Case #%d: %lld\n", t, ret);
    }

    return 0;
}

