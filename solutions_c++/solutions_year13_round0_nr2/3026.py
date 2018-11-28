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
#include <ctime>
#include <cstring>
#include <complex>
#define MINF 0xc0c0c0c0
#define INF 0x3f3f3f3f
#define MOD 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef complex<ll> pt;

int T, R, C, lawn[100][100], goal[100][100];

int main()
{
    ios::sync_with_stdio(0);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    for (int z = 1; z <= T; ++z)
    {
        cin >> R >> C;
        for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            cin >> goal[i][j], lawn[i][j] = 100;
        for (int i = 0; i < R; ++i)
        {
            int cut = 0;
            for (int j = 0; j < C; ++j)
                cut = max(cut, goal[i][j]);
            for (int j = 0; j < C; ++j)
                lawn[i][j] = min(lawn[i][j], cut);
        }
        for (int j = 0; j < C; ++j)
        {
            int cut = 0;
            for (int i = 0; i < R; ++i)
                cut = max(cut, goal[i][j]);
            for (int i = 0; i < R; ++i)
                lawn[i][j] = min(lawn[i][j], cut);
        }
        bool good = true;
        for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
            if (goal[i][j] != lawn[i][j])
                good = false;
        cout << "Case #" << z << ": " << (good ? "YES" : "NO") << endl;\
    }
}
