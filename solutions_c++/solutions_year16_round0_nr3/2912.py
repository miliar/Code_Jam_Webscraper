#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

typedef long long ll;

vector< ll > primes;

ll getDivisor(ll x) {
    for(int i = 0; i < primes.size(); ++i) {
        if(x % primes[i] == 0) {
            return primes[i];
        }
    }
    return x;
}

void initEratosphen() {
    ll lim = 1000 * 1000;
    vector< bool > isPrime(lim, true);
    for(ll i = 2; i < lim; ++i) {
        if(isPrime[i]) {
            primes.push_back(i);
            for(ll j = i*i; j < lim; j += i) {
                isPrime[j] = false;
            }
        }
    }
}

ll getValue(const vector<ll> &x, ll base) {
    ll a = 0;
    for(int i = x.size()-1; i >= 0; --i) {
        a = a * base + x[i];
    }
    return a;
}

int ansLimit;
vector < ll > curAns;
vector< pair< vector< ll >, vector< ll > > > ans;
void gen(int len) {
    if(ans.size() < ansLimit) {
        if(len) {
            curAns[len] = 0;
            gen(len-1);
            curAns[len] = 1;
            gen(len-1);
        } else {
            vector< ll > divs;
            for(int base = 2; base <= 10; ++base) {
                ll val = getValue(curAns, base);
                ll divisor = getDivisor(val);
                if(val == divisor) {
                    return;
                }
                divs.push_back(divisor);
            }
            ans.push_back(make_pair(curAns, divs));
//            cerr << "found!\n";
//            cerr << "[DEBUG] Base 10 value = "  << getValue(curAns, 2) << "\n";
        }
    }
}

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-large-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        initEratosphen();

        int n, j;
        cin >> n >> j;

        ans.clear();
        curAns.assign(n, 1);
        ansLimit = j;
        gen(n-3);
        assert(ans.size() == j);
        //cerr << ans.size() << '\n';

        cout << "Case #" << t << ":\n";
        for(int i = 0; i < j; ++i) {
            for(int k = n-1; k >= 0; --k) {
                cout << ans[i].first[k];
            }
            for(int k = 0; k < 9; ++k) {
                cout << ' ' << ans[i].second[k];
            }
            cout << endl;
        }
    }

    return 0;
}
