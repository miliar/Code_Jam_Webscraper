#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int maxs = 200;

int T;
char s[maxs];


int main() {
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        scanf(" %s", s);
        int n = strlen(s);
        int k = 0;
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1])
                k++;
        }
        int ans;
        if (s[0] == '-') {
            if (k % 2 == 0) {
                ans = k + 1;
            }
            else {
                ans = k;
            }
        }
        else {
            if (k % 2 == 0) {
                ans = k;
            }
            else {
                ans = k + 1;
            }
        }
        printf("Case #%d: %d\n", test + 1, ans);
    }
    return 0;
};
