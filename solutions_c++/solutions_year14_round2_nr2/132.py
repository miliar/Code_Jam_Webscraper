#include <iostream>

using namespace std;

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int a, b, k;
        cin >> a >> b >> k;
        int ans = 0;
        for (int i = 0; i < a; ++i)
            for (int j = 0; j < b; ++j)
                if ((i & j) < k)
                    ++ans;
        printf("Case #%d: %d\n", test, ans);
    }
}
