#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdint>
#include <vector>

typedef __int128 Int;

//*
#define TRACE(cmd)
//*/

/*
#define DO_TRACE
#define TRACE(cmd) std::clog << cmd << std::endl
//*/

std::string solve(int n, int j);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        int n, j;
        std::cin >> n >> j;
        std::cout << "Case #" << t << ": " << solve(n,j) << std::endl;
    }
    return 0;
}

struct Solution {
    Int P[11][32];
    std::vector<Int> primes;

    Solution() {
        for (int i=2; i<=10; ++i) {
            P[i][0] = 1;
            for (int j=1; j<32; ++j) {
                P[i][j] = P[i][j-1];
                P[i][j] *= i;
#ifdef DO_TRACE
                intmax_t *dbg = reinterpret_cast<intmax_t*>(&P[i][j]);
                TRACE(intmax_t(*dbg) << " " << intmax_t(*(dbg + 1)));
#endif
            }
            TRACE(" should be 0: " << intmax_t(P[i][31]%P[i][1]));
            TRACE(" should be 1: " << ((P[i][31] / P[i][1]) == P[i][30]));
        }
        sieve();
        TRACE("solution ready");
    }

    void sieve() {
        TRACE("sieve");
#define SQRT_MAX_PRIME (8*1024)
#define MAX_PRIME (SQRT_MAX_PRIME*SQRT_MAX_PRIME)
        std::vector<bool> s(MAX_PRIME, true);
        s[0] = s[1] = false;
        for (int i=2; i<= SQRT_MAX_PRIME; ++i) {
            if (!s[i]) continue;
            primes.push_back(i);
            for (int j=i<<1; j<MAX_PRIME; j+=i) {
                s[j] = false;
            }
        }
    }

    Int eval(int b, Int *v, int l) {
        Int ret = 0; 
        Int *p = P[b];
        for (int i=0; i<l; ++i) {
            ret += p[i] * v[i];
        }
        return ret;
    }
    std::string solve(int n, int j) {
        std::stringstream ss;

        Int sqMax = 1;
        sqMax <<= 33;

        Int v[33] = {0}; // v[32] is just for safety, see while(true) below
        v[0]  = 1;
        v[n-1] = 1;

        int found = 0;
        while (found != j) {
            Int proof[11] = {0};
            for (int i=2; i<=10; ++i) {
                Int e = eval(i, v, n);
                for (int j=1; j<primes.size(); ++j) {
                    if ((e % primes[j] == 0) && e != primes[j]) {
                        proof[i] = primes[j];
                        break;
                    }
                }
                if (proof[i] == 0) {
                    TRACE("failed for base " << i << "  " << intmax_t(e));
                    break;
                }
            }

            bool validProof = true;
            for (int i=2; i<= 10; ++i) {
                if (proof[i] == 0) {
                    validProof = false;
                    break;
                }
            }

            if (validProof) {
                // print
                ss << std::endl;
                for (int i=0; i<n; ++i) {
                    ss << intmax_t(v[n-1-i]);
                }
                for (int i=2; i<=10; ++i) {
                    ss << " " << intmax_t(proof[i]);
                }
                ++found;
            }

            // next
            int i = 1;
            while (true) {
                ++v[i];         // we start with carry
                if (v[i] > 1) {
                    v[i++] = 0; // we still have carry
                } else {
                    break;      // carry stopped
                }
            } // we'd better find what we want until last carry
        }
        return ss.str();
    }
};

std::string solve(int n, int j) {
    static Solution s;
    return s.solve(n,j);
}



