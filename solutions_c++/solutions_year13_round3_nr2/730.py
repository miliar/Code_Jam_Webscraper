// vim:set sw=4 et smarttab:
// Round 1C 2013

#include <cstdio>
#include <cstdlib>

void print(int count, char plus, char minus)
{
    for (int i = 0; i < count; ++i)
        printf("%c%c", minus, plus);
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        printf("Case #%d: ", tc);
        if (x > 0)
            print(x, 'E', 'W');
        else if (x < 0)
            print(-x, 'W', 'E');
        if (y > 0)
            print(y, 'N', 'S');
        else if (y < 0)
            print(-y, 'S', 'N');
        printf("\n");
    }
}
