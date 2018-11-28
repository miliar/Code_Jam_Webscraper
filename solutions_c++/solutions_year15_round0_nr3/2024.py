#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>
#include <cassert>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

const int ONE = 0;
const int I = 1;
const int J = 2;
const int K = 3;

int mt[4][4] = { {ONE, I, J, K}, {I, ONE, K, J}, {J, K, ONE, I}, {K, J, I, ONE} };
int ms[4][4] = { { 1, 1, 1, 1 }, { 1, -1, 1, -1 }, { 1, -1, -1, 1 }, { 1, 1, -1, -1 } };

const int MAX_L = 10005;

int str[MAX_L];
int act[MAX_L];
int acs[MAX_L];

bool solve()
{
    ll L, X;
    cin >> L >> X;

    for (int i = 0; i < L; ++i)
    {
        char c;
        cin >> c;
        switch (c)
        {
        case 'i':
            str[i] = I;
            break;
        case 'j':
            str[i] = J;
            break;
        case 'k':
            str[i] = K;
            break;
        default:
            assert(false);
        }
    }

    for (int i = 1; i < X; ++i)
    {
        for (int j = 0; j < L; ++j)
        {
            str[j + L * i] = str[j];
        }
    }

    int n = L * X;
    act[0] = str[0];
    acs[0] = 1;
    for (int i = 1; i < n; ++i)
    {
        act[i] = mt[act[i - 1]][str[i]];
        acs[i] = ms[act[i - 1]][str[i]] * acs[i - 1];
    }

    if (act[n - 1] != ONE || acs[n - 1] != -1)
    {
        return false;
    }

    for (int i = 0; i < n; ++i)
    {
        if (act[i] != I || acs[i] != 1)
        {
            continue;
        }

        for (int j = i + 1; j < n - 1; ++j)
        {
            if (act[j] == K && acs[j] == 1)
            {
                return true;
            }
        }
    }

    return false;
}

int main()
{
#ifdef DEBUGAGA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
#elif defined(CONTEST)
    freopen(CONTEST ".in", "r", stdin);
    freopen(CONTEST ".out", "w", stdout);
#endif

    int tests;
    cin >> tests;

    for (int tc = 0; tc < tests; ++tc)
    {
        cout << "Case #" << tc + 1 << ": " << (solve() ? "YES" : "NO") << endl;
    }

    return 0;
}