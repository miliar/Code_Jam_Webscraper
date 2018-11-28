#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char pancakes[100+5];

int main() {
    freopen("/Users/ChaiDuo/Code/Codejam/D/D.in", "r", stdin);
    freopen("/Users/ChaiDuo/Code/Codejam/D/D.out", "w", stdout);

    int ncase;
    scanf("%d", &ncase);

    for (int _ = 1; _ <= ncase; _++)
    {
        int k, c, s;
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d: ", _);
        for (int i = 1; i <= s-1; i++)
        {
            printf("%d ", i);
        }
        printf("%d\n", s);
    }


    return 0;
}