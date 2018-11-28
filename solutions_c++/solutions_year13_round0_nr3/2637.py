#include <vector>
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
# include <cstring>
# include <queue>
# define ll long long
# define pb push_back
# define x first
# define y second
# define inf 1000000007

using namespace std;

vector <int> v;
vector <int> ::iterator c,d;

bool ispal (int a) {
    string s;
    stringstream ss;
    int i, sz;

    ss << a;
    ss >> s;
    sz = s.size() - 1;

    bool pass = 1;
    for (i = 0; i < sz-i; i++)
        if (s[i] != s[sz-i]) {
            pass = 0;
            break;
        }
    return pass;
}

int main()
{
    int t, tc = 0, i, j, k, a, b;

    for (i = 1; i <= 32; i++)
    {
        j = i*i;
        if (j > 1000) continue;
        if (ispal (i) && ispal (j))
            v.pb(j);
    }

    freopen ("C-small-attempt0.in", "r", stdin);
    freopen ("C-small-attempt0.txt", "w", stdout);

    cin >> t;
    while (tc < t) {
        ++tc;

        cin >> a >> b;

        c = upper_bound(v.begin(),v.end(),b);
        d = lower_bound(v.begin(),v.end(),a);

        printf("Case #%d: %d\n", tc, c-d);
    }
    return 0;
}

