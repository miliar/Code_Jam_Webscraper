#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <unordered_map>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const double eps = 1e-10;
const int inf = 1000000000;

const int N = 100005;
const int mo = 1000000000 + 7;

void work()
{
    long long k, c, s;
    cin >> k >> c >> s;
    long long a = 1;
    while (c > 1)
    {
        a *= k;
        --c;
    }
    k = 1 - a;
    while (s--)
    {
        k += a;
        cout << ' ' << k;
    }
    cout << endl;
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d:", i);
        work();
    }
    return 0;
}
