#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int a;
        vector<int> x(16);
        for (int it = 0; it < 2; ++it) {
            cin >> a;
            for (int i = 0; i < 4; ++i)
                for (int j = 0; j < 4; ++j) {
                    int t;
                    cin >> t;
                    --t;                
                    if (i == a - 1)
                        x[t]++; 
                }
        }
        int fl = 0;
        int pos = -1;
        for (int i = 0; i < 16; ++i)
            if (x[i] >= 2)
                ++fl, pos = i;
        if (fl == 0)
            printf("Case #%d: Volunteer cheated!\n", test);
        if (fl == 1)
            printf("Case #%d: %d\n", test, pos + 1);
        if (fl >= 2)
            printf("Case #%d: Bad magician!\n", test);
    }
    return 0;
}
