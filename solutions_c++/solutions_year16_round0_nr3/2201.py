#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;

// Using the GNU Multiple Precision Arithmetic Library
#include <gmp.h>
#include <gmpxx.h>

void next(string& num) {
    for (int i = num.size()-1; i >= 0; i--) {
        num[i] = num[i] == '0' ? '1' : '0';
        if (num[i] == '1')
            return;
    }
    assert(false);
}

bool isjamcoin(const string& s) {
    for (int b = 2; b <= 10; b++) {        
        mpz_class test(s.c_str(), b);
        int r = mpz_probab_prime_p(test.get_mpz_t(), 20);
        if (r > 0) return false;
    }
    return true;
}

vector<string> certificate(const string& s) {
    vector<string> cert;
    for (int b = 2; b <= 10; b++) {
        mpz_class test(s.c_str(), b);
        mpz_class divisor(2);
        int it_limit = 100000;
        for (int it = 1; it <= it_limit; it++) {
            if (mpz_divisible_p(test.get_mpz_t(), divisor.get_mpz_t())) {
                cert.push_back(divisor.get_str());
                break;
            }
            if (it == it_limit) {
                // This one is too hard. Assume that we have enough other jamcoins.
                cerr << "gave up\n";
                return vector<string>();
            }
            mpz_nextprime(divisor.get_mpz_t(), divisor.get_mpz_t());
        }
    }
    return cert;
}

int main() {
    int T = 0, N = 0, J = 0;
    cin >> T >> N >> J;
    cout << "Case #1:\n";
    
    string s(N-2, '0');
    while (J > 0) {
        string candidate = '1' + s + '1';
        if (isjamcoin(candidate)) {
            cerr << "finding cert for " << candidate << "... ";
            vector<string> cert = certificate(candidate);
        
            if (cert.size() != 0) {
                cerr << "done" << endl;
                
                cout << candidate << " ";
                for (string c: cert) cout << c << " ";
                cout << endl;
                J--;
            }
        }
        next(s);
    }
    
    return 0;
}
