#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <iterator>
#include <queue>
#include <algorithm>

#define mp make_pair
#define pb push_back
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> point;
typedef pair<pll, pll> seg;
typedef vector<int> lnum;

const int N = (int)(2e5) + 7;
const int M = (int)(1e6) + 7;
const int K = (int)(1e4) + 7;
const int BLOCK_SIZE = 320;
const ld eps = 1e-9;
const ll INF = (ll)(1e9) + 7;
const ll MOD = (ll)(1e9) + 7;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ttt;
    cin >> ttt;
    for (int iii = 1; iii <= ttt; ++iii) {
        ll x;
        cin >> x;
        if (!x) {
            printf("Case #%d: INSOMNIA\n", iii);
            continue;
        }
        ll k = 0;
        int a[10] = {0};
        for (int j = 0; j < 1000000; ++j) {
            k += x;
            ll q = k;
            while (q) {
                a[q % 10] = 1;
                q /= 10;
            }
            int f = 0;
            for (int i = 0; i < 10; ++i)
                if (!a[i])
                    f = 1;
            if (!f) {
                printf("Case #%d: %lld\n", iii, k);
                break;
            }
        }
    }
    return 0;
}
