#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

void mark(int& cnt, bool *dig, int x) {
    while (x > 0) {
        if (!dig[x%10]) {
            cnt++;
            dig[x%10] = true;
        }
        x /= 10;
    }
}


string solve(int x) {
    if (x == 0) return "INSOMNIA";

    bool dig[10];
    memset(dig, 0, sizeof(dig));

    int b = 0;
    int cnt = 0;
    for (int i = 0; i < 1000; i++) {
        b += x;
        mark(cnt, dig, b);
        if (cnt == 10) {
            char ans[100];
            sprintf(ans, "%d", b);
            return ans;
        }
    }
    // exit(1);
    return "INSOMNIA";
}

int main() {
    int T;

    scanf("%d", &T);

    for (int i = 1; i <= T; i++) {
        int n;
        cin >> n;
        cout << "Case #" << i << ": " << solve(n) << endl;
    }

    return 0;
}
