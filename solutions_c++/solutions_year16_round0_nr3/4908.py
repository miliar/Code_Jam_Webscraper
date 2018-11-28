#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

vector<size_t> divisors;

size_t base(bitset<32> jamcoin, size_t n, size_t b) {
    size_t total = 0, p = 1;
    for (size_t i = 0; i < n; i++) {
        total += p * jamcoin[i];
        p *= b;
    }
    return total;
}

size_t divisor(size_t n, size_t b) {
    size_t s = (size_t) (ceil(sqrt((double) n)) + 0.5);
    for (size_t i = b + 1; i <= s; i++) {
        if (n % i == 0) return i;
    }
    return 0;
}

bool valid(bitset<32> jamcoin, size_t n) {
    divisors.clear();
    for (size_t i = 2; i <= 10; i++) {
        divisors.push_back(divisor(base(jamcoin, n, i), i));
        if (divisors.back() == 0) return false;
    }
    return true;
}

int main() {
    size_t T, N, J;
    cin >> T;
    for (size_t t = 0; t < T; t++) {
        cout << "Case #" << t + 1 << ":" << endl;
        cin >> N >> J;
        size_t value = (1 << (N - 1)) + 1;
        for (size_t i = 0; i < J; i++) {
            value += 2;
            bitset<32> jamcoin(value);
            if (valid(jamcoin, N)) {
                for (size_t j = N; j > 0; j--) {
                    cout << jamcoin[j - 1];
                }
                for (size_t j = 0; j < divisors.size(); j++) {
                    cout << " " << divisors[j];
                }
                cout << endl;
            } else {
                i--;
            }
        }
    }
}
