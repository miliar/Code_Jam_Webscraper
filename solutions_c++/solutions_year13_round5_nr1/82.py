#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

ll x[55], b;
int n;

double solve()
{
    vector<int> bet(37,0);
    double res = 0.0;
    FOR(i, 0, b)
    {
        int mn = x[0], ind = 0;
        FOR(j, 1, 37)
        {
            if(mn > x[j])
            {
                mn = x[j];
                ind = j;
            }
        }
        x[ind]++;
        bet[ind]++;

        mn = x[0];
        FOR(j, 1, 37)
        {
            if(mn > x[j])
            {
                mn = x[j];
            }
        }

        int all = 0;
        FOR(j, 0, 37)
        {
            if(x[j] == mn)
            {
                all++;
            }
        }

        double tmp = 0.0;

        FOR(j, 0, 37)
        {
            if(x[j] == mn)
            {
                tmp += 36.0 * bet[j] / (double)all;
            }
        }

        FOR(j, 0, 37) tmp -= bet[j];

        if(res < tmp) res = tmp;
    }

    return res;
}

int main()
{
    freopen("Asmall.in", "r", stdin);
    //freopen("Asmall.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> b >> n;
        memset(x, 0, sizeof(x));
        FOR(i, 0, n) cin >> x[i];
        cout << "Case #" << testNo << ": " << fixed << setprecision(20) << solve() << endl;
    }
}



