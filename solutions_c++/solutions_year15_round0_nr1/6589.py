#include <iostream>
using namespace std;

char SI[1001], CC;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c++)
    {
        printf("Case #%d: ", c);
        scanf("%d%s", &CC, SI);

        int res = 0;
        int from = SI[0] - '0';
        for (int i = 1; i < CC + 1; i++)
        {
            if (i <= from)
            {
                from += SI[i] - '0';
            }
            else if (SI[i] != '0')
            {
                res += i - from;
                from += res + SI[i] - '0';
            }
        }
        printf("%d\n", res);
    }
}