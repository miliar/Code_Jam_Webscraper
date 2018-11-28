#include <iostream>
#include <vector>
#define SET_BIT(n, k) (n | (1ULL << (k)))
using namespace std;

vector<unsigned long long> _select(unsigned long long n_sel, unsigned long long start) {

    vector<unsigned long long> empty;
    empty.push_back(0);
    if (n_sel == 0) {
        return empty;
    }
    
    if (start < 1) {
        return vector<unsigned long long>();
    }

    vector<unsigned long long> selected;
    vector<unsigned long long> firstselect = _select(n_sel, start - 2);
    for (vector<unsigned long long>::iterator it = firstselect.begin(); it != firstselect.end(); ++it) {
        selected.push_back(*it);
    }

    vector<unsigned long long> secondselect = _select(n_sel - 1, start - 2);
    for (vector<unsigned long long>::iterator it = secondselect.begin(); it != secondselect.end(); ++it) {
        unsigned long long val = SET_BIT(*it, start);
        selected.push_back(val);
    }
    
    return selected;
}

void print_bitwise(unsigned long long n) {

    if (n == 0) {
        return;
    }
    print_bitwise(n >> 1);
    cout << (n & 1);
}

long set_bitlength(unsigned long long n) {

    unsigned long long count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

int main() {

    unsigned long long T, n, m;
    cin >> T >> n >> m;
    const char DIVISORS[] = "3 2 3 2 7 2 3 2 3";
    unsigned long long start = (1ULL << (n - 1)) + 1;

    cout << "Case #1:\n";
    vector<unsigned long long> combos;
    for (unsigned long  long k = 2; k <= n - 2; k += 3) {
        vector<unsigned long long> selected = _select(k, n - 2);
        for (vector<unsigned long long>::iterator it = selected.begin(); it != selected.end(); ++it) {
            combos.push_back(*it);
        }
    }

    for (unsigned long long i = 0; i < combos.size(); ++i) {
        for (unsigned long long j = 0; j < combos.size(); ++j) {
            if (set_bitlength(combos[i]) == set_bitlength(combos[j])) {
                unsigned long long val = start | combos[i] | (combos[j] >> 1ULL);
                print_bitwise(val);
                cout << " " << DIVISORS << "\n";
                m--;
            }
            if (m == 0) break;
        }
        if (m == 0) break;
    }
}
