#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef complex<ld> pt;
typedef vector<pt> pol;
typedef vector<int> vi;
typedef long long ll;


const int B = 32;
const int J = 500;
set<ll> seen;
ll hornermod(const bitset<B>&x, ll b, ll p) {
    ll lastx = x[x.size()-1];
    for(int i=x.size()-2; i>=0; i--) {
        lastx = (b * lastx + (ll)(x[i])) % p;
    }
    return lastx;
}
int main() {
    cout << "Case #1:" << endl;
    ios::sync_with_stdio(0);
    ll s = 10000;
    vector<ll> sieve(s, 1);
    ll k = 2;
    vector<ll> primes;
    while(k < s) {
        for(ll i=k*2; i<s; i+=k) {
            sieve[i] = 0;
        }
        if(primes.size() < 100) primes.push_back(k);
        else break;
        while(sieve[++k] == 0);
    }
    cerr << "sieve computed" << endl;
    ll mincoin = 1LL << (B-1);
    default_random_engine generator;
    uniform_int_distribution<ll> distribution(mincoin/2, mincoin);
    vector<ll> factors(9, 0);
    for(int i=0; i<J; i++) {
        bool works = false;
        while(!works) {
            ll lol = distribution(generator);
            lol = 2*lol + 1;
            //if(sieve[lol]) continue;
            if(seen.count(lol)) continue;
            auto bs = bitset<B>(lol);
            ll popcnt =__builtin_popcount(lol);
            //if(popcnt %3) continue; // ensure divisible by 3 in base 10
            //if(popcnt %2) continue; // ensure divisible by 2 in odd bases
            bool divisible = false;
            for(ll b = 2; b <=10; b++) {
                divisible = false;
                for(auto p : primes) {
                    if(hornermod(bs, b, p) == 0) {
                        factors[b-2] = p;
                        divisible = true;
                        break;
                    }
                }
                if(!divisible) break;
            }
            if(!divisible) continue;
            seen.insert(lol);
            cout << bs;
            for(auto f : factors) {
                cout << " " << f;
            }
            cout << endl;
            works = true;
        }
    }
    

    return 0;    
}
