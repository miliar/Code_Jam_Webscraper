#include <iostream>
#include <cstdio>

using namespace std;

char ppl[1001], space;
int c, t, tot, need;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &c);
    for (int x = 1; x <= c; x++)
    {
        scanf("%d", &t);
        tot = 0;
        need = 0;
        scanf("%c", &space);
        for (int y = 0; y <= t; y++)
        {
            scanf("%c", &ppl[y]);
            ppl[y] -= '0';

            if (tot < y)
            {
                need += y - tot;
                tot = y;
            }
            tot += (int)ppl[y];
        }
        printf("Case #%d: %d\n", x, need);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
