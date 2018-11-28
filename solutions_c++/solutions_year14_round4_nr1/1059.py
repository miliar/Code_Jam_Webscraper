
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <array>
#include <tuple>
#include <utility>
#include <cctype>
#include <typeinfo>
using namespace std;

#define pp make_pair
#define ss size()
#define append push_back
#define ff(a, b)    for (int a = 0; a < int(b); ++a)
#define oo(a, b)    for (int a = 1; a < int(b); ++a)
#define ii(n)    ff(i, n)
#define kk(n)    ff(k, n)
#define mm(n)    ff(m, n)
#define fff(a, b, c) for (int a = int(b); a < int(c); ++a)
#define iii(a, b) fff(i, a, b)
#define kkk(a, b) fff(k, a, b)
#define mmm(a, b) fff(m, a, b)
#define xx first
#define yy second
#define bb begin()
#define ee end()
#define all(x)  (x).bb, (x).ee
#define ite(v)   decltype((v).bb)
#define fe(i, v) for(ite(v) i = (v).bb; i != (v).ee; ++i)
#define err(...)    { fprintf(stderr, __VA_ARGS__); fflush(stderr); }

using LL = long long;
using pii = pair<int, int>;

const int INF = 2147483647;




int main() {
    
    int T;
    cin >> T;
    ff (icase, T) {
        int N, X;
        cin >> N >> X;
        vector<int> ns(N, 0);
        ii (N)
            cin >> ns[i];
        sort(all(ns));
        reverse(all(ns));
        int re = 0;
        vector<bool> used(N, false);
        ii (N) {
            if (used[i])
                continue;
            used[i] = true;
            kkk (i+1, N) {
                if (!used[k] && ns[i] + ns[k] <= X) {
                    used[k] = true;
                    break;
                }
            }
            re += 1;
        }


        printf("Case #%d: %d\n", icase+1, re);
    }

    return 0;
}









