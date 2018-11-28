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
        int count = 0;
        string s;
        cin >> s;
        int l = (int)s.size() - 1;
        while (l > -1) {
            while (l > -1 && s[l] == '+')
                --l;
            if (l < 0)
                break;
            int i = 0;
            while (s[i] == '+')
                ++i;
            for (int j = 0; j < i; ++j)
                s[j] = '-';
            if (i)
                ++count;
            for (int i = 0; i <= l / 2; ++i)
                swap(s[i], s[l - i]);
            for (int i = 0; i <= l; ++i)
                if (s[i] == '+')
                    s[i] = '-';
                else
                    s[i] = '+';
            ++count;
        }
        printf("Case #%d: %d\n", iii, count);
    }
    return 0;
}
