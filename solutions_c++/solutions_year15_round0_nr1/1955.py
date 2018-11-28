#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        int n;
        int sum = 0;
        scanf("%d", &n);
        char cur;
        int res = 0;
        for (int i = 0; i <= n; ++i) {
            cin >> cur;
            if (sum < i && cur != '0') {
                res += i - sum;
                sum = i;
            }
            sum += cur - '0';
        } 
        printf("Case #%d: %d\n", test, res);
    }
}