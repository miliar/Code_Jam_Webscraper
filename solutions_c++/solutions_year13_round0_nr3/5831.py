#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

// 1 4 9 121 484

int t, a, b;

int solve() {
    int a_part = 5;
    if (a > 1)
        a_part = 4;
    if (a > 4) 
        a_part = 3;
    if (a > 9) 
        a_part = 2;
    if (a > 121)
        a_part = 1;
    if (a > 484)
        a_part = 0;
    int b_part = 0;
    if (b < 484)
        b_part = 1;
    if (b < 121)
        b_part = 2;
    if (b < 9)
        b_part = 3;
    if (b < 4)
        b_part = 4;
    if (b < 1)
        b_part = 5;
    return a_part - b_part;
}

void output(int t, int result) {
    cout << "Case #" << t << ": " << result << endl;
}

int main() {
    scanf("%d", &t);
    for (int i = 0; i < t; i ++) {
        scanf("%d%d", &a, &b);
        output(i+1, solve());
    }
    return 0;
}
