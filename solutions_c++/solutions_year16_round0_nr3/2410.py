#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

typedef long long LL;
typedef unsigned int UL;
using namespace std;

const int upp = 100000000;
vector<UL> primes;
bool flags[upp];

void init() {
    fill (flags, flags + upp, true);
    flags[0] = flags[1] = false;
    for (int i = 2; i < upp; i ++) if (flags[i]) {
        for (int j = i +  i; j < upp; j += i) flags[j] = false;
        primes.push_back(i);
    }
    //cout << primes.size() << endl;
    //cout << primes[primes.size()-1] << endl;
}

inline LL convert(UL N, UL base) {
    return N == 0 ? 0 : convert(N >> 1, base) * base + (N & 1);
}

int main () {
    init();
	int cases;
	cin >> cases;
	for (int tc = 1; tc <= cases; tc ++) {
	    cout << "Case #" << tc << ":" << endl;
        int N, J;
        cin >> N >> J;

        //for (int base = 2; base <= 10; base++) cout << convert(N, base) << " " ;
        //cout << endl;
        //return 0;

        UL extra = (1 << (N - 1)) + 1;
        UL up = 1 << (N - 2);

        for (int i = 0; i < up; i ++) {
            UL candidate = extra + (i << 1);
            bool ok = true;
            vector<UL> divisor;
            for (UL base = 2; base <= 10; base ++) {
                LL num = convert(candidate, base);
                bool pr = true;
                for (int x = 0; x < primes.size() && num > primes[x]; x ++) if (num % primes[x] == 0) {
                    divisor.push_back(primes[x]);
                    pr = false;
                    break;
                }
                if (pr) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                std::bitset<32> out(candidate);
                cout << out.to_string().substr(32-N);
                for (int d = 0; d < divisor.size(); d ++) cout << " " << divisor[d];
                cout << endl;
                if (--J == 0) break;
            }
        }
    }
}
