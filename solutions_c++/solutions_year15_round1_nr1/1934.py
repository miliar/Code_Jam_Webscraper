#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <climits>

using namespace std;

#define FOR(k,a,b) for(int k=(a); k < (b); k++)
#define FORE(k,a,b) for(int k=(a); k <= (b); k++)
#define REP(k,a) for(int k=0; k < (a); k++)

#define ALL(c) (c).begin(), (c).end()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define RANGE(lb, x, ub) ((lb) <= (x) && (x) < (ub))

#define dump(x) cerr << #x << ": " << (x) << endl;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;

const int INF = 1000 * 1000 * 1000;
const double EPS = 1e-10;


int main()
{
    int T; cin >> T;
    REP(tcase, T) {
        int n; cin >> n;
        VI ms(n); REP(i, n) cin >> ms[i];

        int res1 = 0;
        FOR(i, 1, n) {
            if(ms[i-1] > ms[i]) res1 += ms[i-1] - ms[i];
        }

        int max_interval = 0;
        FOR(i, 1, n) {
            if(ms[i-1] > ms[i])
                max_interval = max(max_interval, ms[i-1] - ms[i]);
        }
        int res2 = 0;
        int on_plate = ms[0];
        FOR(i, 1, n) {
            res2 += min(max_interval, ms[i-1]);
        }

        printf("Case #%d: %d %d\n", tcase+1, res1, res2);
    }

    return 0;
}
