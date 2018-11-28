#define LARGE
//#define SMALL

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

using namespace std;

int t, T;
string s;
const int L = 'Z'-'A'+1;
const int D = 10;
int i, j, n, A[L];
int num[D];

int main()
{
#if defined(LARGE)
    freopen("../A-large.in", "r", stdin);
    freopen("../A-large.out", "w", stdout);
#elif defined(SMALL)
    freopen("../A-small-attempt0.in", "r", stdin);
    freopen("../A-small.out", "w", stdout);
#else
    freopen("input.txt", "r", stdin);
#endif

    cin >> T;

    for(t = 0; t < T; ++t)
    {
        for (i = 0; i < L; ++i) A[i] = 0;
        for (i = 0; i < D; ++i) num[i] = 0;

        cin >> s;
        n = s.length();
        for (i = 0; i < n; ++i) ++A[s[i]-'A'];
        if (A['X'-'A'] != 0)
        {
            num[6] = A['X'-'A'];
            A['S'-'A'] -= A['X'-'A'];
            A['I'-'A'] -= A['X'-'A'];
            A['X'-'A'] = 0;
        }
        if (A['S'-'A'] != 0)
        {
            num[7] = A['S'-'A'];
            A['E'-'A'] -= 2*A['S'-'A'];
            A['V'-'A'] -= A['S'-'A'];
            A['N'-'A'] -= A['S'-'A'];
            A['S'-'A'] = 0;
        }
        if (A['Z'-'A'] != 0)
        {
            num[0] = A['Z'-'A'];
            A['E'-'A'] -= A['Z'-'A'];
            A['R'-'A'] -= A['Z'-'A'];
            A['O'-'A'] -= A['Z'-'A'];
            A['Z'-'A'] = 0;
        }
        if (A['G'-'A'] != 0)
        {
            num[8] = A['G'-'A'];
            A['E'-'A'] -= A['G'-'A'];
            A['I'-'A'] -= A['G'-'A'];
            A['H'-'A'] -= A['G'-'A'];
            A['T'-'A'] -= A['G'-'A'];
            A['G'-'A'] = 0;
        }
        if (A['V'-'A'] != 0)
        {
            num[5] = A['V'-'A'];
            A['F'-'A'] -= A['V'-'A'];
            A['I'-'A'] -= A['V'-'A'];
            A['E'-'A'] -= A['V'-'A'];
            A['V'-'A'] = 0;
        }
        if (A['F'-'A'] != 0)
        {
            num[4] = A['F'-'A'];
            A['O'-'A'] -= A['F'-'A'];
            A['U'-'A'] -= A['F'-'A'];
            A['R'-'A'] -= A['F'-'A'];
            A['F'-'A'] = 0;
        }
        if (A['W'-'A'] != 0)
        {
            num[2] = A['W'-'A'];
            A['T'-'A'] -= A['W'-'A'];
            A['O'-'A'] -= A['W'-'A'];
            A['W'-'A'] = 0;
        }
        if (A['O'-'A'] != 0)
        {
            num[1] = A['O'-'A'];
            A['N'-'A'] -= A['O'-'A'];
            A['E'-'A'] -= A['O'-'A'];
            A['O'-'A'] = 0;
        }
        if (A['I'-'A'] != 0)
        {
            num[9] = A['I'-'A'];
            A['N'-'A'] -= 2*A['I'-'A'];
            A['E'-'A'] -= A['I'-'A'];
            A['I'-'A'] = 0;
        }
        if (A['T'-'A'] != 0)
        {
            num[3] = A['T'-'A'];
            A['H'-'A'] -= A['T'-'A'];
            A['R'-'A'] -= A['T'-'A'];
            A['E'-'A'] -= 2*A['T'-'A'];
            A['T'-'A'] = 0;
        }
        cout << "Case #" << t+1 << ": ";
        for (i = 0; i < D; ++i)
        {
            for (j = 0; j < num[i]; ++j) cout << i;
        }
        cout << "\n";
    }

    return 0;
}
