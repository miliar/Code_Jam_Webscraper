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
calc (string s, string key) {
    vector <int> u, v;
    int cnt = 0;
    for (int i = 1; i < len (key); i++)
        if (key [i] == key [i - 1]) cnt++;
        else {
            u.push_back (cnt);
            cnt = 0;
        }
    u.push_back (cnt);
    cnt = 0;
    for (int i = 1; i < len (s); i++)
        if (s [i] == s [i - 1]) cnt++;
        else {
            v.push_back (cnt);
            cnt = 0;
        }
    v.push_back (cnt);
    int ret = 0;
    for (int i = 0; i < len (v); i++) ret += abs (v [i] - u [i]);
    return ret;
}

int
main () {
#ifdef LOCALHOST
    freopen ("test.in", "r", stdin);
    // freopen ("test.out", "w", stdout);
#endif
    int T, N;
    string s, t;
    scanf ("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf ("%d", &N);
        set <string> S;
        vector <string> v;
        for (int i = 0; i < N; i++) {
            cin >> s;
            v.push_back (s);
            string t = s;
            t.erase (unique (t.begin (), t.end ()), t.end ());
            S.insert (t);
        }
        if (len (S) != 1) printf ("Case #%d: Fegla Won\n", t);
        else {
            int ret = calc (v [0], v [1]);
            // int ret = INF;
            // for (int i = 0; i < len (v); i++) {
                // string key = v [i];
                // int cnt = 0;
                // for (int j = i + 1; j < len (v); j++) cnt += calc (v [j], key);
                // ret = min (ret, cnt);
            // }
            printf ("Case #%d: %d\n", t, ret);
        }
    }

    return 0;
}

