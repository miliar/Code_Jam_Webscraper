#include <iostream>

using namespace std;

static const int done = 0x3ff;

static inline int max_count(int n) {
    n *= 9;
    int count = 1;
    while (n) {
        n /= 10;
        count *= 10;
    }
    return count;
}

static inline void set_digits(int &digits, int n) {
    while (n) {
        digits |= (1 << (n % 10));
        n /= 10;
    }
}

int main(int argc, char *argv[]) {
    int t, n, i;
    cin >> t;
    for (i = 0; i < t; i++) {
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        int count = max_count(n);
        int digits = 0;
        int tmp = n;
        while (count--) {
            set_digits(digits, tmp);
            if (digits == done) {
                cout << tmp;
                break;
            }
            tmp += n;
        }
        if (digits != done) {
            cout << "INSOMNIA";
        }
        cout << endl;
    }
    return 0;
}
