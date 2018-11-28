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

#define len(x)  (int((x).size()))
#define append push_back
#define pp make_pair
#define ff(a, b)    for (int a = 0; a < int(b); ++a)
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
using pLi = pair<LL, int>;
typedef priority_queue<pLi, vector<pLi>, greater<pLi> > priority_q;

const LL INF = 9223372036854775807LL;
//const int INF = 2147483647;
   




int main() {
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    //cout << '\n';
    
    int T;
    cin >> T;
    fff (icase, 1, 1+T) {
        printf("Case #%d: ", icase);

        priority_q pq;

        vector<pLi> hikers;

        int N;
        cin >> N;
        int crosses = 0;
        ii (N) {
            int D, H, M;
            cin >> D >> H >> M;
            crosses += H;
            kk (H) {
                pq.push(pp((360LL - D)*(M+k), len(hikers)));
                hikers.append(pp(360LL*(M+k), D));
            }
        }
        if (len(hikers) == 1) {
            printf("0\n");
            continue;
        }

        sort(all(hikers));
        LL slow_dist = (360 - hikers[1].yy) * (hikers[1].xx);
        LL fast_dist = (360 - hikers[0].yy + 360) * (hikers[0].xx);
        int rr = (fast_dist <= slow_dist ? 1 : 0);


        printf("%d\n", rr);
    }

    return 0;
}


