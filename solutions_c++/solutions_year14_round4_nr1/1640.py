#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <bitset>
//#include <unordered_set>
//#include <unordered_map>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
typedef long long llong;
typedef pair<llong, llong> pll;
typedef unsigned long long ullong;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.14159265359;
#define y1 Y1
#define y0 alalal1231

vector<int> x;

int main()
{
#ifdef MYLOCAL
    freopen("/home/vladimir/code/pain/input.txt", "rt", stdin);
    freopen("/home/vladimir/code/pain/output.txt", "wt", stdout);
#endif

    int t;
    scanf("%d", &t);
    for (int _i = 1; _i <= t; ++_i)
    {
        int n, cap;
        scanf("%d %d", &n, &cap);
        x.resize(n);

        for (int i = 0; i < n; ++i)
            scanf("%d", &x[i]);
        sort(x.begin(), x.end());

        int ans = 0;

        while (!x.empty())
        {
            int a = x.back();
            x.pop_back();
            auto it = upper_bound(x.begin(), x.end(), cap - a);
            if (it != x.begin())
                x.erase(--it);
            ++ans;
        }

        printf("Case #%d: %d\n", _i, ans);
    }

    return 0;
}
