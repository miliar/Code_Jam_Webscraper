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

int N;
ll A, a[111];

int solve()
{
    int res = 0;
    sort(a, a + N);
    FOR(i, 0, N)
    {
        if(a[i] < A) A += a[i];
        else if(A == 1) return res + N - i;
        else
        {
            int cnt = 0;
            ll A2 = A;
            while(A2 <= a[i])
            {
                cnt++;
                A2 += A2 - 1;
            }
            if(cnt >= N - i) return res + N - i;
            else
            {
                res += cnt;
                A = A2 + a[i];
            }
        }
    }
    return res;
}

int main()
{
    freopen("Asmall.in", "r", stdin);
    freopen("Asmall.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> A >> N;
        FOR(i, 0, N) cin >> a[i];
        cout << "Case #" << testNo << ": " << solve() << endl;
    }
}
