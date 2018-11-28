#define _CRT_SECURE_NO_DEPRECATE

#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <ctime>
using namespace std;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


bool is_pal(ll n)
{

    ll a = n, b = 0;

    while (a != 0)
    {
        b = b * 10 + (a % 10);
        a /= 10;
    }

    return (n == b);
}

bool is_square(ll n, ll &r)
{
    r = ll(sqrt(n + 0.9));
    return (r * r == n);
}


int T;
int a, b;


int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("c_output.txt", "w", stdout);

    // ll n = 0, r;
    // while (1)
    // {
    //     n++;
    //     if (!is_square(n, r))
    //         continue;
    //     if (is_pal(n) && is_pal(r))
    //         printf("%lld * %lld = %lld\n", r, r, n);
    // }

    scanf("%d", &T);
    FOR(test, 1, T)
    {
        scanf("%d %d", &a, &b);
        int res = 0, k;

        k = 1; if (a <= k && k <= b) res++;
        k = 4; if (a <= k && k <= b) res++;
        k = 9; if (a <= k && k <= b) res++;
        k = 121; if (a <= k && k <= b) res++;
        k = 484; if (a <= k && k <= b) res++;

        printf("Case #%d: %d\n", test, res);
    }

    return 0;
}
