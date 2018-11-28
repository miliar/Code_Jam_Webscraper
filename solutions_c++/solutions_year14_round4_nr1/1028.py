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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <cstring>
#include <ctime>
#include <cassert>

#define REP(k,a) for(int k = 0; k < (a); ++k)
#define FOR(k,a,b) for(int k=(a); k < (b); ++k)
#define FRE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define SZ(x) ((int)((x).size()))
#define ALL(c) (c).begin(), (c).end()
#define CLR(c) memset((c), 0, sizeof(c))
#define VCLR(v) fill((v).begin(), (v).end(), 0)
#define PB push_back
#define MP make_pair
#define DBG(x) std::cerr << #x" = " << x << std::endl
#define I1 first
#define I2 second

const int INF = 1000000000;

using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<double> VD;
typedef vector<vector<double> > VVD;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<pair<int,int> > VII;
typedef long long LL;
typedef long double LD;

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        int N, X;
        cin >> N >> X;
        VI szs(N);
        for (int i = 0; i < N; ++i)
        {
            cin >> szs[i];
        }

        sort(ALL(szs));

        int start = 0, end = N-1;
        int cnt = 0;

        while (start <= end)
        {
            if (szs[start] + szs[end] <= X)
            {
                ++start;
                --end;
            }
            else
            {
                --end;
            }

            ++cnt;
        }

        printf("Case #%d: %d\n", t+1, cnt);
    }
    return 0;
}
