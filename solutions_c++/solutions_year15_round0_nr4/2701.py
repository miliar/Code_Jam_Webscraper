#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

// #define DEBUG
#ifdef DEBUG
#define PRINT(a, b) printf("%d, %d\n", (a), (b))
#define SHOW(a, b, c) printf("input: %d, %d, %d\n", a, b, c)
#else
#define PRINT(a, b)  
#define SHOW(a, b, c)  
#endif


void solve() {
    int t = 0;
    while (cin >> t) {
        for (int i=0; i<t; i++) {
            int a, b, c;
            cin >> a >> b >> c;
            SHOW(a, b, c);
            int max_row = ceil(a / 2.0);
            int max_col = a - max_row + 1;
            if (max_row < max_col) {
                swap(max_row, max_col);
            }
            PRINT(max_row, max_col);
            if (b < c) {
                swap(b, c);
            }
            PRINT(b, c);
            char *name = "GABRIEL";
            if ((b * c) % a != 0) {
                name = "RICHARD";
            }
            else if (max_row > b || max_col > c) {
                name = "RICHARD";
            }
            else if (a == 4 && c <= 2) {
                name = "RICHARD";
            }
            printf("Case #%d: %s\n", i+1, name);
        }
    }
}


int main()
{
    solve();
    return 0;
}
