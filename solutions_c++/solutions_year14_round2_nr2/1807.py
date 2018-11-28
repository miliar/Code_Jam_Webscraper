#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(void) {
    int t;
    cin >> t;
    for (int _t = 0; _t < t; _t++) {
        int a, b, k;
        cin >> a >> b >> k;
        int c = 0;
        for (int _a = 0; _a < a; _a++) {
            for (int _b = 0; _b < b; _b++) {
                if ((_a & _b) < k) c++;
            }
        }
        printf("Case #%d: %d\n", _t + 1, c);
    }
}
