#include <iostream>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <time.h>
#include <stdio.h>

using namespace std;

using ll = __int128;
using ull = unsigned long long;
template<typename T> using vv = vector<vector<T>>;
using pii = pair<int, int>;
using pll = pair<long long, long long>;

inline ll nl() { ll n; scanf("%I64d ", &n); return n; }
inline int ni() { int n; scanf("%d ", &n); return n; }
vector<int> v;

struct point {
    ll x, y;
};


vector<int> get_dig(ll a) {
    vector<int> res;
    while (a > 0) {
        res.push_back(a % 10);
        a /= 10;
    }

    return res;
}

void random(vector<ll> &v) {
    v[0] = 1;
    v[v.size() - 1] = 1;
    for (int i = 1; i < v.size() - 1; ++i) {
        if ((double) rand() / RAND_MAX > 0.5) {
            v[i] = 1;
        }
        else {
            v[i] = 0;
        }
    }
}

ll go(vector<ll> &v, int s) {
    ll pw = 1;
    ll res = 0;

    for (int i = v.size() - 1; i >= 0; --i) {
        res += v[i] * pw;
        pw *= s;
    }

    return res;
}

vector<ll> GetPrimeVector(int n)
{

    vector<char> ans(n + 1, true);
    ans[1] = false;
    for ( int i = 2; i*i <= n; i++ )
        if (ans[i])
            for (int j = i * i; j <= n; j += i)
                ans[j] = false;
    vector<ll> res;
    for (int i = 2; i <= n; i++)
        if (ans[i]) res.push_back(i);
    return res;
}

//#define LOCAL

ll dec(vector<ll> &v) {
    ll res = 0;
    ll st = 1;
    for (int i = 0; i < v.size(); ++i) {
        res += v[i] * st;
        st *= 10;
    }

    return res;
}

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    srand(time(NULL));
    cin.tie(0);
    int n;
    cin >> n;

    cout << "Case #1:" << endl;

    cin >> n;

    long long kol;
    cin >> kol;

    vector<ll> v(n);

    auto primes = GetPrimeVector(1e5);
    set<vector<ll>> used;

    while (kol) {
        random(v);
        if (used.find(v) != used.end()) {
            continue;
        }
        else {
            used.insert(v);
        }
        vector<int> del;
        for (int i = 2; i <= 10; ++i) {
            ll x = go(v, i);
            for (int j = 0; j < primes.size(); ++j) {
                if (!(x % primes[j]) && primes[j] < x) {
                    del.push_back(primes[j]);
                    break;
                }
            }

            if (del.size() == 9) {
                --kol;
                for (auto a : v) {
                    cout << (int)a;
                }

                for (auto a : del) {
                    cout << " " << (int)a;
                }
                cout << endl;
            }
        }
    }
}