#include <iomanip>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define foreach(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)

typedef std::vector< std::string > VS;
typedef std::vector<int> VI;
typedef long long ll;

using namespace std;

char dp[1<<4][1<<4];


static int M, N;

static bool _good(int wmask, int dmask)
{
    char& ret = dp[wmask][dmask];
    if (ret >= 0)
        return (bool)ret;
    for (int i = 0; i < 4; i++)
        if (wmask & (1 << i)) {
            int av = (M >> (i*N)) & dmask;
            if (av == 0)
                return ret = 0;
            for (int j = 0; j < 4; j++)
                if (av & (1 << j))
                    if (!_good(wmask ^ (1 << i), dmask ^ (1 << j)))
                        return ret = 0;
        }

    return ret = 1;
}

static
bool good(int m, int n)
{
    M = m;
    N = n;
    return _good((1 << n) - 1, (1 << n) - 1);
}

int solve(const vector<VI>& a)
{
    int n = a.size();
    int amask = 0;
    int ret = n * n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            amask |= (a[i][j] << (i * n + j));
    for (int m = 0; m < (1 << (n*n)); m++) {
        if ((m & amask) != amask)
            continue;
        int q = __builtin_popcount(m ^ amask);
        if (q >= ret)
            continue;
        memset(dp, -1, sizeof(dp));
        if (good(m, n))
            ret = q;
    }
    return ret;
}

int main(int argc, const char* argv[]) {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<VI> a(N);
        for (int i = 0; i < N; i++) {
            string s;
            cin >> s;
            for (int j = 0; j < N; j++)
                a[i].push_back(s[j] - '0');
        }
        cout << "Case #" << t << ": " << solve(a) << endl;
    }
    return 0;
}
