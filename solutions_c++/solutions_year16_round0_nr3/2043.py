#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <array>

using namespace std;

using ll = long long;
using ull = unsigned long long;
constexpr ll MAX_PRIMES = 1E8;

vector<ll> primes;
vector<vector<ll>> powers(11);
void init()
{
    vector<int> crossed(MAX_PRIMES);
    ll m = sqrt(MAX_PRIMES+0.5);
    for (ll i = 2; i <= m; ++i) if (!crossed[i]) {
        for (ll j = i*i; j < MAX_PRIMES; j += i)
            crossed[j] = 1;
    }

    for (ll i = 2; i < MAX_PRIMES; ++i) if (!crossed[i]) {
        primes.push_back(i);
#ifdef DEBUG
        cout << i << "\n";
#endif
    }

    for (int base = 2; base <= 10; ++base) {
        ll res = 1;
        for (int exp = 0; exp <= 16; ++exp) {
#ifdef DEBUG
            cout << res << " ";
#endif
            powers[base].push_back(res);
            res *= base;
        }
#ifdef DEBUG
        cout << "\n";
#endif
    }

}

int FindFactor(const array<ll,2> &n, ll b)
{
    for (auto f: primes) {
        if (n[1] == 0) {
            if (f*f > n[0]) return 0;
            if (n[0] % f == 0) // f divided n
                return f;
        }
        else {
            auto reminder_first = n[0] % f;
            auto reminder_second = n[1] % f;
            auto base_reminder = b % f;
            auto reminder = (reminder_first + reminder_second * base_reminder) % f;
            if (reminder == 0) // divide evenly and n cannot be equal to f due to fact that n[1] has leading '1'
                return f;
        }
    }

    return 0; // probably a prime; if n too large, not deterministic
}

int main()
{
    init();
    int T; cin >> T;
    for (int cas = 1; cas <= T; ++cas) {
        cout << "Case #" << cas << ":\n";

        int N, J; cin >> N >> J;

        ll jamcoin = 1LL | (1LL << (N-1));
        ll limit = 1LL << N;

        // try all possible jamcoins
        for (int coin_count = 0; coin_count < J && jamcoin < limit; jamcoin += 2) {
            vector<array<ll,2>> reinterpreted(11, {0,0});
            vector<ll> nontrivial_factors(11);
            bool all_non_prime = true;
            string s_jc;

            for (ll i = 1, pos = 0; i < limit; i <<= 1, pos++) {
                if (jamcoin & i) {// it is a one
                    s_jc += '1';
                    for (int b = 2; b <= 10; ++b) {
                        if (pos < 16) // within bit range 0--15
                            reinterpreted[b][0] += powers[b][pos];
                        else // bit range 16--31
                            reinterpreted[b][1] += powers[b][pos-16];
                    }
                }
                else
                    s_jc += '0';
            }

            for (int b = 2; b <= 10; ++b) {
                nontrivial_factors[b] = FindFactor(reinterpreted[b], powers[b][16]);
                if (nontrivial_factors[b] == 0) {
                    all_non_prime = false;
                    break;
                }
            }
            if (all_non_prime) {
                coin_count++;
                reverse(s_jc.begin(), s_jc.end());
                cout << s_jc;
                for (int b = 2; b <= 10; ++b)
                    cout << " " << nontrivial_factors[b];
                cout << "\n";
            }
        }
    }

    return 0;
}

