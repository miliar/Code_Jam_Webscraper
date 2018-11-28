#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int n, test, ans, t;
char a[10000];

int main()
{
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++) {
        scanf("%d %s", &n, a);
        int ans = 0, curr = 0;
        for (int i = 0; i <= n; i++) {
            if (i > curr) {
                ans += i - curr;
                curr = i;
            }
            curr += a[i] - '0';
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}
