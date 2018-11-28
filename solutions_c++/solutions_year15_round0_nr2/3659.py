#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <set>

using namespace std;

int n, test, answ, ans, t;
int a[10000];

int main()
{
    freopen("in.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    scanf("%d", &t);
    for(int test = 1; test <= t; test++) {
        answ = 1000000000;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for (int j = 1; j <= 1000; j++) {
            ans = 0;
            for (int i = 0; i < n; i++) {
                ans += a[i] / j;
                if (a[i] % j == 0)
                    ans--;
            }
            ans += j;
            answ = min(answ, ans);
        }
        printf("Case #%d: %d\n", test, answ);
    }
    return 0;
}
