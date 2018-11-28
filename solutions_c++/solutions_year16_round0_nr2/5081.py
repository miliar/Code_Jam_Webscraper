#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char pancakes[100+5];

int main() {
    freopen("/Users/ChaiDuo/Code/Codejam/B/B.in", "r", stdin);
    freopen("/Users/ChaiDuo/Code/Codejam/B/B.out", "w", stdout);

    int ncase;
    scanf("%d", &ncase);

    for (int _ = 1; _ <= ncase; _++)
    {
        scanf("%s", pancakes);
        int res = 0;
        int i = strlen(pancakes) - 1;

        while (i >= 0)
        {
            if (pancakes[i] == '-')
            {
                for (int j = i; j >= 0; j--)
                {
                    pancakes[j] = (pancakes[j] == '-')? '+': '-';
                }
                res++;
            }
            i--;
        }

        printf("Case #%d: ", _);
        printf("%d\n", res);
    }


    return 0;
}