#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <ostream>
#include <queue>
#include <cmath>
#include <climits>
#include <utility>
#include <fstream>
#include <memory>
#include <sstream>
#include <set>
#include <iterator>
#include <iomanip>
#include <map>
#include <stack>
using namespace std;
#define FOR(a, b, n) for(int (a) = (b); (a) < (n); ++(a))
#define FORE(a, b, n) for(int (a) = (b); (a) <= (n); ++(a))
#define ITE(a, v) for(auto (a) = v.begin(); (a) != v.end(); ++(a))
#define LL long long
#define ALL(v) v.begin(),v.end()
#define ZERO(v) memset(v, 0, sizeof v)
#define NEG(v)  memset(v, -1, sizeof v)
#define F first
#define S second
#define LD long double
#define pw(x) (1LL << (x))
#define sqr(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define MOD 1000000007
#define PI 3.141592653589793
#define PII pair<LL, LL>
#define INF 0x3f3f3f3f
#define FUL(x) memset(x, 0x3f, sizeof(x));
#define debug(args...) {cerr << #args << " = "; errDebug(args); cerr << endl;}
void errDebug() {}
template<typename T, typename... Args>
void errDebug(T a, Args... args) {
    cerr << a << ' ';
    errDebug(args...);
}
LL n;
LL dp[10][10];
LL solve()
{
    if(n == 0)
        return -1;
    FUL(dp);
    FORE(i,1,100)
    {
        LL val = n * i;
        int start = 0;
        while(val)
        {
            dp[start][val % 10] = min(dp[start][val % 10], n * i);
            start++;
            val /= 10;
        }
    }
    LL res = 0;
    FOR(i,0,10)
    {
        LL tmp = INF;
        FOR(j,0,10)
        tmp = min(tmp, dp[j][i]);
        res = max(res,tmp);
    }
    return res;
}
int main() {
    int T;
    cin >> T;
    FOR(h,0,T)
    {
        cin >> n;
        printf("Case #%d: ", h + 1);
        LL res = solve();
        if(res == -1)
            cout << "INSOMNIA" << endl;
        else
            cout << res << endl;
    }
    return 0;
}