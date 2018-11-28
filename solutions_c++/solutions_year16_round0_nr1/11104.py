#include <iostream>
#include <cstdio>
using namespace std;

int main (int argc, char *argv[]) {
    int nc, n;
    cin >> nc;
    for (int i = 0; i < nc; i++) {
        cin >> n;
        cout << "Case #" << (i + 1) << ": ";
        if (n > 0) {
            int flags = 0, tot = 0, num = 0;
            while (flags != 1023) {
                num += n;
                tot = num;
                while (tot > 0) {
                    int digit = tot % 10;
                    flags = flags | (1 << digit);
                    tot = tot / 10;
                }
            }
            cout << num << "\n";
        } else {
            cout << "INSOMNIA\n";
        }
    }
}
