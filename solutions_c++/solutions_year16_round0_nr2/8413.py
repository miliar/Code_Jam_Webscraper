#include <bits/stdc++.h>
using namespace std;


int n_test;
int n;
char s[1010];

int main() {

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &n_test);
    for (int test = 1; test <= n_test; ++test) {
        scanf("%s", s + 1);
        n = strlen(s + 1);

        int res = 0;
        for (int i = 1; i <= n; i++)
            if (s[i] != s[i + 1])
                ++res;
        if (s[n] == '+') --res; 
        printf("Case #%d: %d\n", test, res);
    }

    return 0;
}