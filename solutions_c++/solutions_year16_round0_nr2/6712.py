#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int cs = 1; cs <= n; ++cs) {
        int result = 0;

        char str[128];
        scanf("%s", str);

        int prev = 'x';

        for (int i = 0; str[i] != '\0'; ++i) {
            if (str[i] != prev) {
                prev = str[i];
                ++result;
            }
        }

        if (prev == '+') --result;

        printf("Case #%d: %d\n", cs, result);
    }
}
