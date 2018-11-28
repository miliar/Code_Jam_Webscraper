#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

#define PB push_back
#define MP make_pair
#define INF 0x3f3f3f3f

#define TWO(x) ((LL)1 << (x))
#define HAS(x, t) ((x) & TWO(t))
#define LOW(x) ((x) & (-(x)))
#define REP(i, n) for (LL i = 0, _n = (n); i < _n; ++i)
#define REP3(i, l, r) for (LL i = (l), _r = (r); i < _r; ++i)
#define REP4(i, l, r, s) for (LL i = (l), _r = (r), _s = (s); i < _r; i += _s)
#define CLR(x, c) memset(x, (c), sizeof(x))
#define CMAX(x, y) do {if (x < (y)) x = (y); } while (0);
#define CMIN(x, y) do {if (x > (y)) x = (y); } while (0);

int main()
{
    int t, nc = 0;
    cin >> t;
    while (t--)
    {
        int n;
        string str;
        cin >> n >> str;
        int sum = 0, ans = 0;
        for (int i = 0; i <= n; ++i)
        {
            int x = str[i] - '0';
            ans += max(i - (sum + ans), 0);
            sum += x;
        }
        cout << "Case #" << ++nc << ": " << ans << endl;
    }
    return 0;
}
