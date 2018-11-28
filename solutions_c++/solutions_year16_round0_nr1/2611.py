#include <iostream>
#include <bitset>

using namespace std;
typedef long long int i64;
typedef bitset<10u> DigitSet;

void AddAll(i64 n, DigitSet& seen) {
    while (n != 0) {
        int d = n % 10;
        seen.set(d);
        n /= 10;
    }
}

i64 LastNumber(i64 n) {
    DigitSet seen;
    i64 x = 0;
    do {
        x += n;
        AddAll(x, seen);
    } while (!seen.all());
    return x;
}

int main() {
    int num_tests;
    cin >> num_tests;
    for (int test = 1; test <= num_tests; test++) {
        i64 n;
        cin >> n;
        cout << "Case #" << test << ": ";
        if (n == 0) cout << "INSOMNIA\n";
        else cout << LastNumber(n) << "\n";
    }
    return 0;
}
