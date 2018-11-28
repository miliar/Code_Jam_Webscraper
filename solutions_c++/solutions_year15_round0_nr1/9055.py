#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    char a[2005];
    int n;
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    for (int l = 0; l < t; l++) {
        scanf("%d %s", &n, a);
        printf("Case #%d: ", l+1);
        int i;
        int s = 0;
        int c = 0;
        for (i = 0; i < n+1; i++) {
            if (s >= i) {
                s += a[i]-'0';
            } else {
                if (a[i] != 48) {
                    c += (i-s);
                    s = i + a[i]-'0';
                }
            }
        }
        printf("%d\n", c);
    }

    return 0;
}
