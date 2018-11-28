#include <iostream>
#include <unordered_map>
#include <bitset>
#include <vector>

using namespace std;

typedef unsigned long long ullong;
typedef unordered_map<bitset<32>, vector<ullong> > table;

uint J;
ullong count = 0;

table jamcoins;



void precompute() {
    
}

ullong divisor(bitset<32>& bits, int base) {
    for (int i = 2; i < 10000; ++i) {
        
        int p[32] = {0};
        p[0] = 1;
        for (int j = 1; j < 32; ++j) {
            p[j] = ( p[j/ 2] * p[j / 2]);
            p[j] = (p[j] * ((j % 2) ? base : 1)) % i;
        }
        ullong x = 0;
        for (int j = 31; j >= 0; --j)
            x += p[j] * bits[j];
        // x = (x*base + bits[j]) % i;
        // cout << bits << ' ' << base << ' ' << i << ' ' << x << '\n';
        if (x % i == 0) {
            return i;
        }
    }
    return 0;
}

void isanyprime(bitset<32>& bits) {
    ++count;
    vector<ullong> divs;
    // ullong y = bits.to_ullong();
    for (int i = 2; i < 11; ++i) {
        // cout << "Num: " << x << '\n';
        ullong div = divisor(bits, i);
        // cout << "Div: " << div << '\n';
        if (div != 0) {
            // cout << "Num: " << y << " in base " << i << ' ' << x  << " is " << div << '\n';
            // cout << bits << ' '<a< div << '\n';
            divs.push_back(div);
        } else {
            return;
        }
    }
    // cerr << bits << ' ' << divs[0] << '\n';
    jamcoins[bits] = divs;
}

void calc(bitset<32>& bits, int pos) {
    if (pos > 30 || jamcoins.size() >= J) {
        return;
        // isanyprime(bits);
    }
    else {
        calc(bits, pos + 1);
        if (jamcoins.size() >= J)
            return;
        bits.flip(pos);
        isanyprime(bits);
        calc(bits, pos + 1);
        bits.flip(pos);
        // if (jamcoins.size() >= J)
        // return;
    }
}

void test() {
    for (table::iterator it = jamcoins.begin(); it != jamcoins.end(); ++it) {
        bitset<32> b = it->first;
        int i = 2;
        for (vector<ullong>::iterator pt = it->second.begin(); pt != it->second.end(); ++i, ++pt) {
            int p[32] = {0};
            p[0] = 1;
            for (int j = 1; j < 32; ++j) {
                p[j] = ( p[j/ 2] * p[j / 2]);
                p[j] = (p[j] * ((j % 2) ? i : 1)) % *pt;
            }
            ullong x = 0;
            for (int j = 31; j >= 0; --j)
                x += p[j] * b[j];
            if (x % *pt != 0) {
                cerr << "Ooops " << x << ' ' << *pt << '\n';
                break;
            }
        }
    }
}

int main() {
    int t, n;
    cin >> t >> n >> J;

    bitset<32> bits;
    bits.set(0);
    bits.set(31);

    calc(bits, 1);
    //cout << "Count: " << count << '\n';
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ":\n";
        for (table::iterator it = jamcoins.begin(); it != jamcoins.end(); ++it) {
            cout << it->first;
            for (int j = 0; j < 9; ++j)
                cout << ' ' << it->second[j];
            cout << '\n';
        }
    }

    test();
}
