#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

int32_t count(uint32_t n) {
    if(n == 0) {
        return -1;
    }

    uint32_t seen = 0, current = 0, tmp, digit;

    while(seen != 0x3ff) {
        current += n;

        tmp = current;
        while(tmp > 0) {
            digit = tmp % 10;
            seen |= 1 << digit;
            tmp /= 10;
        }
    }

    return current;
}

int main(int argc, char **argv) {
    uint32_t t;
    cin >> t;

    vector<uint32_t> n(t);
    for(uint32_t i = 0; i < t; i++) {
        cin >> n[i];
    }

    int32_t y;
    for(uint32_t i = 0; i < t; i++) {
        y = count(n[i]);

        cout << "Case #" << i + 1 << ": ";
        if(y < 0) {
            cout << "INSOMNIA";
        }
        else {
            cout << y;
        }
        cout << endl;
    }

    return 0;
}
