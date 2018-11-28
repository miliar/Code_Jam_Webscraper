#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <stack>
#include <iterator>

#define x first
#define y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ld, ld> point;
typedef pair<ll, ll> pll;
typedef pair<ld, int> pdi;

const int N = (int)(5e3) + 7;
const int M = (int)(86400) + 7;
const ld eps = 1e-12;
const ll MOD = (ll)(1e9) + 9;
const ll INF = (ll)(1e18) + 7;
const ld PI = 3.14159265358979310000;

int main()
{
    freopen("people.in", "r", stdin);
    freopen("people.out", "w", stdout);
    int tt;
    cin >> tt;
    for (int iii = 0; iii < tt; ++iii)
    {
        int n;
        cin >> n;
        char x;
        cin >> x;
        int kol = (int)(x - '0'), ans = 0;
        for (int i = 1; i <= n; ++i)
        {
            if (kol < i)
            {
                ans += i - kol;
                kol = i;
            }
            cin >> x;
            kol += (int)(x - '0');
        }
        printf("Case #%d: %d\n", iii + 1, ans);
    }
    return 0;
}
