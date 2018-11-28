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
        int N; double V, X; cin >> N >> V >> X;
        vector<double> rs(N), cs(N); REP(i, N) cin >> rs[i] >> cs[i];

        vector<double> bs(N); REP(i, N) bs[i] = rs[i] * (X - cs[i]);

        if(N == 1) {
            if(cs[0] != X) {
                printf("Case #%d: IMPOSSIBLE\n", tcase+1);
            }
            else {
                printf("Case #%d: %.8lf\n", tcase+1, V / rs[0]);
            }
            continue;
        }

        if(((cs[0] < X) && (cs[1] < X)) || ((X < cs[0]) && (X < cs[1]))) {
            printf("Case #%d: IMPOSSIBLE\n", tcase+1);
        }
        else if(cs[0] == X && cs[1] == X) {
            printf("Case #%d: %.8lf\n", tcase+1, V / (rs[0] + rs[1]));
        }
        else {
            double det = rs[0] * bs[1] - rs[1] * bs[0];
            double t1 = (V * bs[1]) / det;
            double t2 = -(V * bs[0]) / det;
            
            printf("Case #%d: %.8lf\n", tcase+1, max(t1, t2));
        }

    }

    return 0;
}
