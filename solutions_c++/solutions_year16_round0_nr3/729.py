#include<bits/stdc++.h>
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
using namespace std;

const int MAXN = (1 << 20) + 11;
const int MAXP = MAXN / 10;
int sieve[MAXN];
int primes[MAXP], primec = 0;

unordered_set<string> was;

int main() {
    #ifdef LOCAL
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif    	   	

    sieve[0] = sieve[1] = true;
    for (int i = 2; i < MAXN; ++i) if (!sieve[i]) {
        assert(primec < MAXP);
        primes[primec++] = i;
        if (ll(i) * i < MAXN)
            for (int j = i * i; j < MAXN; j += i)
                sieve[j] = i;
    }
    cerr << primes[primec - 1] << endl;


    const int PC = 100;
    assert(PC <= primec);
    std::random_device rd;
    std::mt19937 mt(rd());
    std::uniform_int_distribution<int> dist(0, 1);

    int T;
    cin >> T;
    for (int __it = 1; __it <= T; ++__it) {
        cout << "Case #1:\n";
        int n, maxc;
        cin >> n >> maxc;

        vector<char> bin(n + 1);
        vector< vector<int> > vals(11, vector<int>(PC + 1));
        vector<int> out(11);

/*        for (int x = (1 << (n - 1)) + 1; x < (1 << n); x += 2) {
            int y = x, digCount = 0;
            while (y) {
                bin[digCount++] = y % 2;
                y /= 2;
            }
            assert(digCount == n);
            bin[n] = 0;
            reverse(bin.begin(), bin.begin() + n);
*/
        while (1)  {
            bin[0] = 1;
            bin[n - 1] = 1;
            for (int i = 1; i + 1 < n; ++i) {
                bin[i] = dist(mt);
            }

            for (int base = 2; base <= 10; ++base)
                for (int pi = 0; pi < PC; ++pi)
                    vals[base][pi] = 0;
            
            for (int i = 0; i < n; ++i) {
                for (int base = 2; base <= 10; ++base) {
                    for (int pi = 0; pi < PC; ++pi) {
                        vals[base][pi] = (vals[base][pi] * base + bin[i]) % primes[pi];
                    }
                }                      
            }

            bool ok = true;
            for (int base = 2; base <= 10; ++base) {
                bool baseok = false;
                for (int pi = 0; pi < PC; ++pi) {
                    if (vals[base][pi] == 0) {
                        out[base] = primes[pi];
                        baseok = true;
                        break;
                    }
                }
                if (!baseok) {
                    ok = false;
                    break;
                }
            }

            if (ok) {
                for (int i = 0; i < n; ++i) bin[i] += '0';
                bin[n] = 0;
                if (was.find(bin.data()) == was.end()) {
                    cout << bin.data();
                    for (int i = 2; i < 11; ++i) cout << " " << out[i];
                    cout << endl;

                    was.insert(bin.data());
                    if (was.size() == maxc) {
                        break;
                    }
                }
            }
        }
    }


    return 0;
}
