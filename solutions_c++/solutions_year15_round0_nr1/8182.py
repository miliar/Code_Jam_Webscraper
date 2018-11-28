#include <cstdio>

using namespace std;

int main()
{
    int t;
    char s[1001];
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        int ret = 0, sMax, tot;
        scanf("%d ", &sMax);
        for (int j = 0; j <= sMax; j++)
        {
            scanf("%c", &s[j]);
        }
        tot = s[0] - '0';
        for (int j = 1; j <= sMax; j++)
        {
            if (j > tot)
            {
                ret += j - tot;
                tot += j - tot;
            }
            tot += s[j] - '0';
        }
        printf("Case #%d: %d\n", i, ret);
    }
}
