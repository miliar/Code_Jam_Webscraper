#include <iostream>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[]) {
    int e;
    cin >> e;
    for (int l = 0; l < e; l++) {
        int i;
        cin >> i;
        if (i) {
            int n = 0;
            int ni;
            unsigned int b = 0b1111111111;
            while (b) {
                n++;
                ni = n * i;
                int k = ni;
                while (k) {
                    int q = k % 10;
                    unsigned int l = 0b1 << q;
                    b = b & ~l;
                    k = k / 10;
                }
            }
            cout << "Case #" << l + 1 << ": " << ni << endl;
        } else {
            cout << "Case #" << l + 1 << ": INSOMNIA" << endl;
        }
    }
    return 0;
}
