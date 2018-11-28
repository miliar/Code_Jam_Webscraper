#include <iostream>

#define DIGITS 10

using std::cin;
using std::cout;
using std::endl;

bool status[DIGITS];

void init() {
    for (int i = 0; i < DIGITS; i++)
        status[i] = false;
}

bool sleeping() {
    for (int i = 0; i < DIGITS; i++)
        if (!status[i]) return false;
    return true;
}

void update(unsigned long long n) {
    int d;

    while (n) {
        d = n % 10;
        if (!status[d])
            status[d] = true;
        n /= 10;
    }
}

int main() {
    int T, prev;
    unsigned long long n, cn, m;
    bool isInfy;
    
    cin >> T;
    for (int i = 1; i <= T; i++) {
        prev = 0;
        cin >> n;

        init();

        isInfy = false;
        prev = 0;
        m = 1;
        while (!sleeping()) {
            cn = m * n;
            if (cn == prev) {
                isInfy = true;
                break;
            }

            update(cn);

            //cout << "n = " << cn << endl;
            prev = cn;
            m++;
        }

        if (isInfy)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else
            cout << "Case #" << i << ": " << cn << endl;
    }

    return 0;
}
