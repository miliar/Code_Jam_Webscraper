#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

char s[110];

int toInt(char c)
{
    return c == '+' ? 0 : 1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int q;
    scanf("%d\n", &q);
    for (int t = 1; t <= q; ++t)
    {
        printf("Case #%d: ", t);
        scanf("%s", s);
        int n = strlen(s);
        int turnsCount = 0;
        for (int i = n - 1; i >= 0; --i)
        {
            if ((toInt(s[i]) + turnsCount) % 2)
            {
                turnsCount++;
            }
        }
        printf("%d\n", turnsCount);
    }
    return 0;
}