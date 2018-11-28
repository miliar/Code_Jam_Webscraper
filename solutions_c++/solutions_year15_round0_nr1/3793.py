#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    int test;
    scanf("%d", &test);
    for ( int t = 1; t <= test; t++)
    {
        int n, res = 0, ans = 0;
        scanf(" %d ", &n);
        for ( int i = 0; i <= n; i++)
        {
            char cc;
            scanf("%c", &cc);
            int c = cc - '0';

            if (res < i && i != 0) {
                ans += i - res;
                res += i  - res;
            }
            res += c;
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}